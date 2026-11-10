#!/usr/bin/env python3
"""Copia de seguridad de MongoDB Atlas (plan gratuito, sin copias automaticas).

Vuelca TODAS las colecciones de la base a ficheros .jsonl (un documento por linea,
en JSON extendido de MongoDB: conserva fechas e ids) y escribe un manifiesto con el
numero de documentos de cada una.

Uso (PowerShell):
    $env:MONGO_URI = "<cadena de conexion>"      # solo en esa ventana; no la pegues en chats
    python scripts/backup_mongo.py                # copia en  ~/backups-masesora/mongo-AAAA-MM-DD
    python scripts/backup_mongo.py --out D:/copias

Restaurar una coleccion (ejemplo):
    from bson import json_util; from pymongo import MongoClient
    docs = [json_util.loads(l) for l in open("clients.jsonl", encoding="utf-8")]
    MongoClient(URI)["masesora"]["clients"].insert_many(docs)

IMPORTANTE: las copias contienen datos personales. Guardalas en tu disco, no en una
carpeta compartida, y borra las antiguas (la politica de privacidad fija un maximo de
conservacion). Nunca subas esta carpeta a GitHub.
"""
import argparse
import datetime
import json
import os
import sys
from pathlib import Path

from bson import json_util
from pymongo import MongoClient


def volcar(db, destino: Path) -> dict:
    destino.mkdir(parents=True, exist_ok=True)
    resumen = {}
    for nombre in sorted(db.list_collection_names()):
        if nombre.startswith("system."):
            continue
        n = 0
        with open(destino / f"{nombre}.jsonl", "w", encoding="utf-8") as f:
            for doc in db[nombre].find({}):
                f.write(json_util.dumps(doc, ensure_ascii=False) + "\n")
                n += 1
        resumen[nombre] = n
        print(f"  {nombre}: {n} documentos")
    return resumen


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(Path.home() / "backups-masesora"), help="carpeta donde guardar las copias")
    ap.add_argument("--db", default=os.environ.get("MONGO_DB_NAME", "masesora"), help="nombre de la base")
    args = ap.parse_args()

    uri = os.environ.get("MONGO_URI")
    if not uri:
        print("Falta la variable de entorno MONGO_URI.", file=sys.stderr)
        return 1

    hoy = datetime.date.today().isoformat()
    destino = Path(args.out) / f"mongo-{hoy}"
    print(f"Copiando la base '{args.db}' en {destino}")
    cliente = MongoClient(uri, serverSelectionTimeoutMS=15000)
    cliente.admin.command("ping")   # falla pronto si la IP no esta permitida en Atlas
    resumen = volcar(cliente[args.db], destino)
    with open(destino / "_manifiesto.json", "w", encoding="utf-8") as f:
        json.dump({"fecha": hoy, "base": args.db, "colecciones": resumen}, f, indent=2, ensure_ascii=False)
    print(f"Hecho: {sum(resumen.values())} documentos en {len(resumen)} colecciones.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
