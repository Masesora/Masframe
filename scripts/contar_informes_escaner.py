#!/usr/bin/env python3
"""Cuenta los informes del Escaner de Salud Empresarial (colección `clients`), por semana,
EXCLUYENDO los expedientes de prueba. Solo lectura.

Un informe = un expediente del Escaner (tiene `scores_areas`). Se excluyen los que parecen de
prueba: email o empresa con «prueba», «test», «ejemplo», «claude», correos @masesora.* y los que
pases con --excluir. Se enseña la lista de excluidos para que se vea qué se ha dejado fuera.

Uso (PowerShell):
    $env:MONGO_URI = "<cadena de conexion>"      # solo en esa ventana; no la pegues en chats
    python scripts/contar_informes_escaner.py
    python scripts/contar_informes_escaner.py --desde 2026-11-15 --excluir maria@ejemplo.com
"""
import argparse
import datetime
import os
import re
import sys
from collections import Counter

from pymongo import MongoClient

PATRON_PRUEBA = re.compile(r"prueba|test|ejemplo|claude|@masesora\.", re.I)


def es_prueba(doc, extra):
    email = str(doc.get("email", "")).lower()
    empresa = str(doc.get("empresa", ""))
    return email in extra or bool(PATRON_PRUEBA.search(email) or PATRON_PRUEBA.search(empresa))


def enmascarar(email):
    user, _, dom = str(email).partition("@")
    return (user[:2] + "***@" + dom) if dom else "***"


def semana_iso(fecha):
    iso = fecha.isocalendar()
    return f"{iso[0]}-S{iso[1]:02d}"


def contar(docs, extra=()):
    extra = {e.lower() for e in extra}
    incluidos, excluidos = [], []
    for d in docs:
        (excluidos if es_prueba(d, extra) else incluidos).append(d)
    por_semana = Counter(semana_iso(d["created_at"]) for d in incluidos if d.get("created_at"))
    return incluidos, excluidos, por_semana


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--desde", help="fecha AAAA-MM-DD a partir de la cual contar")
    ap.add_argument("--excluir", nargs="*", default=[], help="emails adicionales a excluir")
    ap.add_argument("--db", default=os.environ.get("MONGO_DB_NAME", "masesora"))
    args = ap.parse_args()
    uri = os.environ.get("MONGO_URI")
    if not uri:
        print("Falta la variable de entorno MONGO_URI.", file=sys.stderr)
        return 1
    filtro = {"scores_areas": {"$exists": True}}
    if args.desde:
        filtro["created_at"] = {"$gte": datetime.datetime.fromisoformat(args.desde)}
    cli = MongoClient(uri, serverSelectionTimeoutMS=15000)
    cli.admin.command("ping")
    docs = list(cli[args.db]["clients"].find(filtro, {"email": 1, "empresa": 1, "created_at": 1}))
    incluidos, excluidos, por_semana = contar(docs, args.excluir)
    print(f"Informes del Escaner (sin pruebas): {len(incluidos)}")
    for sem in sorted(por_semana):
        print(f"  {sem}: {por_semana[sem]}")
    print(f"\nExcluidos como prueba: {len(excluidos)}")
    for d in excluidos:
        print(f"  - {enmascarar(d.get('email'))} · {d.get('empresa', '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
