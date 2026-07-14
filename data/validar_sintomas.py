# -*- coding: utf-8 -*-
"""
Linter clinico de MASFRAME — valida symptoms.json contra los CONTRATOS que el
frontend (TreatmentPage.tsx) y el backend imponen al dato.
Cada bug historico = un contrato aqui. Crece cada vez que aparece un tipo nuevo.
Uso:  python validar_sintomas.py   (exit 0 = sin ERRORES; 1 = hay ERRORES)
"""
import json, os, re, sys

RUTA = sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "symptoms.json")
REQUIRED = ["symptom_id","specialty_id","kpi_name","kpi_unit","kpi_question","kpi_formula",
            "kpi_objective","kpi_recovery_mode","capa_1_options","capa_2_decision",
            "capa_2_options","justi_capa6","input_a","input_b","inputs"]
RECOVERY = {"financiero","conteo","estructural"}
C2_HERR  = {"", "retencion", "margen"}

def c2_family(dec):
    n=(dec or "").lower()
    if "dafo" in n: return "dafo"
    if "abc" in n: return "abc"
    if "árbol" in n or "arbol" in n: return "arbol"
    if "regla" in n: return "regla"
    if "semáforo" in n or "semaforo" in n: return "semaforo"
    if "carga" in n or "capacidad" in n: return "carga"
    return "matriz"
# familias cuyo gate C2->C3 esta soportado en el frontend (tras el fix)
GATE_OK = {"dafo","abc","arbol","regla","semaforo","carga","matriz"}

def labels(s):
    out=[("input_a",s.get("input_a","")),("input_b",s.get("input_b",""))]
    for i,it in enumerate(s.get("inputs",[]) or []):
        if isinstance(it,dict): out.append((f"inputs[{i}].label", it.get("label","")))
    return out

def lint(s):
    E=[]; W=[]
    sid=s.get("symptom_id","??")
    # --- claves requeridas ---
    for k in REQUIRED:
        if k not in s: E.append(f"falta el campo requerido '{k}'")
    # --- C2 options: string, 6 items ---
    c2=s.get("capa_2_options")
    if not isinstance(c2,str): E.append("capa_2_options no es string (el frontend hace .split(';'))")
    else:
        items=[x for x in (p.strip() for p in c2.split(";")) if x]
        if len(items)!=6: E.append(f"capa_2_options tiene {len(items)} items (deben ser 6)")
    # --- C1 options: 6 items ---
    c1=s.get("capa_1_options")
    if isinstance(c1,str):
        it1=[x for x in (p.strip() for p in c1.split(";")) if x]
        if len(it1)!=6: E.append(f"capa_1_options tiene {len(it1)} items (deben ser 6)")
        if isinstance(c2,str) and len(it1)!=len([x for x in (p.strip() for p in c2.split(';')) if x]):
            W.append("capa_1_options y capa_2_options no tienen el mismo nº de items (consonancia C1-C2)")
    else:
        E.append("capa_1_options no es string")
    # --- labels de input: '+' rompe el DesglosadorInput ---
    for campo,lab in labels(s):
        if not isinstance(lab,str): continue
        if lab=="—": continue
        if "+" in lab: E.append(f"{campo} contiene '+' -> el DesglosadorInput lo parte en sub-campos y rompe la etiqueta: {lab!r}")
        if ";" in lab: W.append(f"{campo} contiene ';' (riesgo con parsers): {lab!r}")
        if "\n" in lab: W.append(f"{campo} contiene salto de linea: {lab!r}")
    # --- kpi_formula: solo InputA/InputB y operadores ---
    f=s.get("kpi_formula","")
    if not isinstance(f,str) or "InputA" not in f:
        E.append(f"kpi_formula sospechosa (debe usar InputA[/InputB]): {f!r}")
    else:
        resto=f.replace("InputA","").replace("InputB","")
        if not re.fullmatch(r"[\d.,*/+\-() ]*", resto):
            E.append(f"kpi_formula con tokens no permitidos: {f!r}")
    # --- kpi_objective: direccion + numero ---
    obj=(s.get("kpi_objective") or "").strip()
    if not re.fullmatch(r"[<>≤≥]\s*\d+([.,]\d+)?\s*%?", obj):
        E.append(f"kpi_objective no parseable (debe empezar por <,>,≤,≥ y numero): {obj!r}")
    # --- recovery_mode ---
    rm=s.get("kpi_recovery_mode")
    if rm not in RECOVERY: E.append(f"kpi_recovery_mode invalido: {rm!r}")
    elif rm=="estructural":
        if not (s.get("input_revised_1") and s.get("input_revised_2")):
            W.append("estructural sin input_revised_1/2 (para la re-medicion de C6)")
    # --- c2_herramienta ---
    ch=s.get("c2_herramienta","")
    if ch not in C2_HERR: W.append(f"c2_herramienta no reconocido por el frontend: {ch!r}")
    # --- familia C2 con gate soportado ---
    fam=c2_family(s.get("capa_2_decision",""))
    if fam not in GATE_OK: E.append(f"familia C2 '{fam}' sin gate C2->C3 soportado")
    # --- single input pero formula usa InputB ---
    if s.get("input_b")=="—" and "InputB" in f:
        E.append("input_b es '—' (single input) pero kpi_formula usa InputB")
    # --- unit ---
    if not s.get("kpi_unit"): W.append("kpi_unit vacio")
    # --- justi_capa6 ---
    j6=s.get("justi_capa6","") or ""
    if len(j6)<40 or "OKR tracking" in j6:
        W.append("justi_capa6 demasiado corta o generica")
    # --- herramientas: capa_3_plan debe enlazar a los .html (si no, las 197 herramientas no salen) ---
    sid=s.get("symptom_id","")
    cp=s.get("capa_3_plan")
    cptxt=json.dumps(cp,ensure_ascii=False) if cp else ""
    herr_dir=os.path.join(os.path.dirname(os.path.abspath(RUTA)),"herramientas",sid)
    hay_files=os.path.isdir(herr_dir) and any(f.endswith(".html") for f in os.listdir(herr_dir))
    if (not cp) or (".html" not in cptxt):
        extra=" (pero SÍ existen los .html en disco)" if hay_files else " (y tampoco hay .html en disco)"
        W.append(f"capa_3_plan sin herramientas enlazadas -> las herramientas no aparecen en C4{extra}")
    # --- footgun x30: 'dia' en el objetivo dispara conversion en el semaforo ---
    if re.search(r"d[ií]a", obj, re.I):
        W.append(f"kpi_objective contiene 'dia' -> el frontend multiplica el score x30 (conversion mes->dia); casi siempre NO deseado: {obj!r}")
    # --- formato mixto en options (salto de linea rompe el conteo por ';') ---
    for campo in ("capa_1_options","capa_2_options"):
        v=s.get(campo)
        if isinstance(v,str) and "\n" in v:
            W.append(f"{campo} contiene salto de linea (formato mixto; el conteo por ';' puede fallar)")
    return E,W,fam

def main():
    d=json.load(open(RUTA,encoding="utf-8"))
    print(f"Linter clinico MASFRAME — {len(d)} sintomas\n"+"="*60)
    nE=nW=0; fam_count={}
    for s in d:
        E,W,fam=lint(s)
        fam_count[fam]=fam_count.get(fam,0)+1
        if E or W:
            print(f"\n[{s.get('symptom_id','??')}] {s.get('kpi_name','')}  (C2: {fam})")
            for e in E: print(f"   ❌ {e}"); 
            for w in W: print(f"   ⚠️  {w}")
        nE+=len(E); nW+=len(W)
    print("\n"+"="*60)
    print("COBERTURA de familias C2:", ", ".join(f"{k}:{v}" for k,v in sorted(fam_count.items())))
    print(f"RESULTADO: {nE} ERRORES · {nW} avisos")
    sys.exit(1 if nE else 0)

if __name__=="__main__":
    main()
