#!/usr/bin/env python3
"""Mide en data/symptoms.json dos tipos de seccion candidatas a limpiar (§LXI.C). Solo lectura.

B: la seccion no baja una decision a C4 y no aporta al KPI (ni columna con contribuye_valor*,
   suma_si, cuenta_unicos_si, ni calculada que sume, ni origen_margen ni celebrar_total).
D: la seccion tiene una columna calculada que solo es un paso intermedio (la usa otra formula
   y no suma).

Son CANDIDATAS: una persona tiene que mirar cada una antes de tocar nada. Uso:
    python scripts/medir_secciones_catalogo.py
"""
import json
import re
import sys
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "data" / "symptoms.json"
ACCION = re.compile(r"acci[oó]n|mejora|plan\b|acuerdo|ajuste|paso\b|tarea|decisi[oó]n|siguiente", re.I)  # = ACCION_REGEX de TreatmentPage.tsx
VALOR = ("contribuye_valor", "contribuye_valor_si", "suma_si", "cuenta_unicos_si")


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    sintomas = d if isinstance(d, list) else d.get("symptoms", list(d.values()))
    total, B, D = 0, [], []
    for x in sintomas:
        if not isinstance(x, dict) or "capa_3_plan" not in x:
            continue
        for rama, r in x["capa_3_plan"].items():
            if not isinstance(r, dict) or not r.get("secciones"):
                continue
            for i, s in enumerate(r["secciones"], 1):
                total += 1
                cols = s.get("columnas") or []
                tit = (s.get("titulo") or f"seccion {i}")[:60]
                baja = any(c.get("es_decision") or c.get("tipo") == "decision"
                           or (ACCION.search(str(c.get("etiqueta", ""))) and c.get("tipo") in ("texto", "opciones")) for c in cols)
                valor = (any(any(k in c for k in VALOR) or (c.get("tipo") == "calculada" and not c.get("no_sumar")) for c in cols)
                         or "origen_margen" in s or s.get("celebrar_total"))
                ref = (x.get("symptom_id"), rama, i, tit)
                if not baja and not valor:
                    B.append(ref + (len(cols),))
                inter = [c["clave"] for c in cols if c.get("tipo") == "calculada" and c.get("clave") and c.get("no_sumar")
                         and any(o is not c and o.get("tipo") == "calculada" and re.search(r"\b" + re.escape(c["clave"]) + r"\b", str(o.get("formula", ""))) for o in cols)]
                if inter:
                    D.append(ref + (inter,))
    print(f"Secciones medidas: {total}")
    print(f"\nB · sin decision y sin aportar al KPI: {len(B)}")
    for sid, rama, i, tit, n in B:
        print(f"  {sid:10s} {rama}.s{i}  {tit!r}  ({n} campos)")
    print(f"\nD · con un calculo intermedio: {len(D)}")
    for sid, rama, i, tit, inter in D:
        print(f"  {sid:10s} {rama}.s{i}  {tit!r}  intermedio: {', '.join(inter)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
