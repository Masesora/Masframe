#!/usr/bin/env python3
"""Cuenta la lista de espera de tratamientos no disponibles («Quirófano Ocupado»), por síntoma.
Solo lectura. Sirve para decidir qué especialidad se abre después: la demanda real, no la intuición.

Uso (PowerShell):
    $env:MONGO_URI = "<cadena de conexion>"      # solo en esa ventana; no la pegues en chats
    python scripts/contar_lista_espera.py
"""
import os
import sys
from collections import Counter

from pymongo import MongoClient


def main():
    uri = os.environ.get("MONGO_URI")
    if not uri:
        sys.exit("Falta la variable MONGO_URI (solo en esa ventana, sin pegarla en chats).")
    col = MongoClient(uri)["masesora"]["lista_espera"]
    docs = list(col.find({"activo": True}, {"_id": 0, "email": 1, "sintomas": 1, "created_at": 1}))
    print(f"Personas en la lista de espera: {len(docs)}")
    por_sintoma = Counter(s for d in docs for s in d.get("sintomas", []))
    print("\nPersonas por síntoma pedido (de más a menos):")
    for s, n in por_sintoma.most_common():
        print(f"  {n:3d}  {s}")
    por_esp = Counter(s.split("-S")[0] for s in por_sintoma.elements())
    print("\nPor especialidad (prefijo del id):")
    for e, n in por_esp.most_common():
        print(f"  {n:3d}  {e}")


if __name__ == "__main__":
    main()
