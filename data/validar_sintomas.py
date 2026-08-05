# -*- coding: utf-8 -*-
"""
Linter clinico de MASFRAME v2 — valida symptoms.json contra los CONTRATOS que el
frontend (TreatmentPage.tsx) y el backend imponen al dato.
Cada bug historico = un contrato aqui. Crece cada vez que aparece un tipo nuevo.

Uso:  python validar_sintomas.py            (valida data/symptoms.json)
      python validar_sintomas.py <ruta>     (valida archivo alternativo)
      python validar_sintomas.py --sim      (añade simulacion Paqui por sintoma)

Exit 0 = sin ERRORES; 1 = hay ERRORES
"""
import json, os, re, sys, operator, unicodedata

RUTA = next((a for a in sys.argv[1:] if not a.startswith("--")),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "symptoms.json"))
SIM  = "--sim" in sys.argv

REQUIRED = ["symptom_id","specialty_id","kpi_name","kpi_unit","kpi_question","kpi_formula",
            "kpi_objective","kpi_recovery_mode","capa_1_options","capa_2_decision",
            "capa_2_options","justi_capa6","input_a","input_b","inputs"]
RECOVERY = {"financiero","conteo","estructural"}
C2_HERR  = {"", "retencion", "margen"}
GENERIC_COLS = {"Elemento / paso a trabajar", "Elemento / paso a trabajar "}
ACTION_PLAN_OK = {"CIR-S1"}  # unico sintoma donde la plantilla generica es correcta por diseno

def c2_family(dec):
    n=(dec or "").lower()
    if "dafo" in n: return "dafo"
    if "abc" in n: return "abc"
    if "árbol" in n or "arbol" in n: return "arbol"
    if "regla" in n: return "regla"
    if "semáforo" in n or "semaforo" in n: return "semaforo"
    if "carga" in n or "capacidad" in n: return "carga"
    return "matriz"

GATE_OK = {"dafo","abc","arbol","regla","semaforo","carga","matriz"}

def labels(s):
    out=[("input_a",s.get("input_a","")),("input_b",s.get("input_b",""))]
    for i,it in enumerate(s.get("inputs",[]) or []):
        if isinstance(it,dict): out.append((f"inputs[{i}].label", it.get("label","")))
    return out

# ── Motor de evaluacion de formulas (replica de evaluarFormula del frontend) ──────
def evaluar_formula(formula, contexto):
    """Evalua formula con + - * / ( ) y referencias a claves del contexto.
    Devuelve (resultado_float, None) o (None, mensaje_error).
    """
    expr = formula
    # sustituir claves (mas largas primero para evitar sustitucion parcial)
    for clave in sorted(contexto.keys(), key=len, reverse=True):
        val = contexto[clave]
        if val is None: return None, f"clave '{clave}' es None en contexto"
        expr = expr.replace(clave, str(float(val)))
    # verificar que solo quedan tokens aritmeticos seguros
    if not re.fullmatch(r"[\d.+\-*/()\s]+", expr):
        return None, f"formula con tokens no permitidos tras sustitucion: {expr!r}"
    try:
        result = eval(expr, {"__builtins__": {}})  # noqa: S307 — solo +,-,*,/,()
        return float(result), None
    except ZeroDivisionError:
        return None, "division por cero"
    except Exception as e:
        return None, str(e)

def lint_capa3(s, E, W):
    """Contratos del motor nativo (Fase 6): capa_3_plan."""
    sid = s.get("symptom_id","")
    cp  = s.get("capa_3_plan")
    if not cp or not isinstance(cp, dict):
        W.append("capa_3_plan ausente o no es dict")
        return

    # todos los recursos r1-r6 deben existir
    for rk in ["r1","r2","r3","r4","r5","r6"]:
        if rk not in cp:
            E.append(f"capa_3_plan.{rk} ausente")

    for rk, recurso in cp.items():
        if not isinstance(recurso, dict): continue
        tipo = recurso.get("tipo","")
        prefix = f"capa_3_plan.{rk}"

        if tipo == "nativa":
            _lint_nativa(sid, prefix, recurso, E, W)

        elif tipo == "calculadora":
            _lint_calculadora(sid, prefix, recurso, E, W)

        elif tipo not in ("nativa","calculadora"):
            E.append(f"{prefix}.tipo desconocido: {tipo!r} (solo 'nativa' o 'calculadora')")

def _lint_nativa(sid, prefix, recurso, E, W):
    secciones = recurso.get("secciones", [])
    if not secciones:
        E.append(f"{prefix}: tipo nativa sin secciones")
        return

    ec_seen = {}  # entidad_compartida -> primera seccion que la define

    for i, sec in enumerate(secciones):
        sp = f"{prefix}.sec[{i}]"
        cols = sec.get("columnas", [])
        fi   = sec.get("filas_iniciales", 0)

        if not cols:
            E.append(f"{sp}: sin columnas")
            continue
        if len(cols) < 2:
            W.append(f"{sp}: solo {len(cols)} columna (minimo recomendado: 2)")
        if fi <= 0:
            W.append(f"{sp}: filas_iniciales={fi} (el usuario no verá filas al abrir)")

        # plantilla generica en sintoma que no es plan de accion
        if sid not in ACTION_PLAN_OK:
            first_label = cols[0].get("etiqueta","")
            if first_label in GENERIC_COLS:
                W.append(f"{sp}: usa plantilla generica ('Elemento / paso a trabajar') — revisar si el contenido es especifico al proposito del sintoma")

        # recoger claves de columnas inputables (para validar formulas)
        claves_input = {}
        claves_calc  = {}
        tipos_validos = {"texto","numero","opciones","calculada"}
        for c in cols:
            clave    = c.get("clave","")
            etiqueta = c.get("etiqueta","")
            ctipo    = c.get("tipo","texto")

            if ctipo not in tipos_validos:
                E.append(f"{sp} col '{etiqueta}': tipo desconocido {ctipo!r}")

            if ctipo == "opciones":
                opts = c.get("opciones")
                if not opts or not isinstance(opts, list) or len(opts) == 0:
                    E.append(f"{sp} col '{etiqueta}': tipo opciones sin opciones[]")

            if clave and ctipo != "calculada":
                claves_input[clave] = 10.0   # valor simulado

            if ctipo == "calculada":
                if not clave:
                    E.append(f"{sp} col '{etiqueta}': calculada sin clave")
                if not c.get("formula"):
                    E.append(f"{sp} col '{etiqueta}': calculada sin formula")

        # validar formulas de columnas calculadas
        for c in cols:
            if c.get("tipo") != "calculada": continue
            clave   = c.get("clave","")
            formula = c.get("formula","")
            etiqueta= c.get("etiqueta","")
            if not formula: continue

            # contexto disponible: claves_input + calculadas anteriores
            contexto = {**claves_input, **claves_calc}
            resultado, err = evaluar_formula(formula, contexto)
            if err:
                if "division por cero" in err:
                    W.append(f"{sp} col '{etiqueta}': formula puede dividir por cero con valores reales: {formula!r}")
                else:
                    E.append(f"{sp} col '{etiqueta}': formula invalida — {err} — formula={formula!r}")
            else:
                claves_calc[clave] = resultado  # disponible para calculadas siguientes

            # tokens no soportados por evaluarFormula del frontend
            for tok in ["ceil","round","max","min","Math","if","abs"]:
                if re.search(r'\b' + tok + r'\b', formula):
                    E.append(f"{sp} col '{etiqueta}': formula usa '{tok}' — evaluarFormula del frontend solo soporta + - * / ( ): {formula!r}")

            # claves referenciadas existen?
            tokens_formula = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", formula)
            for tok in tokens_formula:
                if tok not in claves_input and tok not in claves_calc:
                    E.append(f"{sp} col '{etiqueta}': formula referencia clave '{tok}' que no existe en esta seccion: {formula!r}")

        # entidad_compartida: la primera columna de cada seccion que la declara debe
        # tener la misma etiqueta (o clave) que las otras secciones que comparten entidad
        ec = sec.get("entidad_compartida")
        if ec:
            if ec not in ec_seen:
                ec_seen[ec] = (i, cols[0].get("etiqueta",""))
            else:
                prev_i, prev_label = ec_seen[ec]
                cur_label = cols[0].get("etiqueta","")
                if cur_label.strip() != prev_label.strip():
                    W.append(f"{prefix}.sec[{i}]: entidad_compartida='{ec}' pero primera columna '{cur_label}' difiere de sec[{prev_i}] '{prev_label}' — el frontend las vincula por posicion, asegurate de que son la misma entidad")

def _lint_calculadora(sid, prefix, recurso, E, W):
    campos    = recurso.get("campos", [])
    resultados= recurso.get("resultados", [])

    if not campos:
        E.append(f"{prefix}: calculadora sin campos")
    if not resultados:
        E.append(f"{prefix}: calculadora sin resultados")

    # claves de campos (inputs)
    ctx = {}
    for c in campos:
        clave = c.get("clave","")
        if not clave:
            E.append(f"{prefix} campo '{c.get('etiqueta','')}': sin clave")
        else:
            ctx[clave] = 10.0   # valor simulado
        # precarga_desde_c0 (SS.XV.B, sesion 5 ago 2026): solo estos 2 literales existen en
        # session.c0.inputs — el frontend no valida esto en runtime, un valor distinto no
        # precarga nada y falla en silencio, asi que se corta aqui.
        pc0 = c.get("precarga_desde_c0")
        if pc0 is not None and pc0 not in ("input_a", "input_b"):
            E.append(f"{prefix} campo '{c.get('etiqueta','')}': precarga_desde_c0={pc0!r} invalido (solo 'input_a' o 'input_b')")

    # validar resultados
    for r in resultados:
        clave   = r.get("clave","")
        formula = r.get("formula","")
        etiqueta= r.get("etiqueta","")
        rtipo   = r.get("tipo","calculada")

        if rtipo == "calculada":
            if not clave:
                E.append(f"{prefix} resultado '{etiqueta}': calculada sin clave")
            if not formula:
                E.append(f"{prefix} resultado '{etiqueta}': calculada sin formula")
            else:
                resultado, err = evaluar_formula(formula, ctx)
                if err:
                    if "division por cero" in err:
                        W.append(f"{prefix} resultado '{etiqueta}': formula puede dividir por cero: {formula!r}")
                    else:
                        E.append(f"{prefix} resultado '{etiqueta}': formula invalida — {err} — {formula!r}")
                else:
                    if clave: ctx[clave] = resultado

                for tok in ["ceil","round","max","min","Math","if","abs"]:
                    if re.search(r'\b' + tok + r'\b', formula):
                        E.append(f"{prefix} resultado '{etiqueta}': usa '{tok}' no soportado por evaluarFormula: {formula!r}")

                tokens_formula = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", formula)
                for tok in tokens_formula:
                    if tok not in ctx:
                        E.append(f"{prefix} resultado '{etiqueta}': formula referencia clave '{tok}' no definida en campos ni resultados previos: {formula!r}")

        # alimenta_valor: solo en resultados € genuinos
        if r.get("alimenta_valor") and r.get("unidad") not in ("eur", None):
            W.append(f"{prefix} resultado '{etiqueta}': alimenta_valor=true pero unidad='{r.get('unidad')}' (se espera 'eur' para conectar a C4/C5)")

    # semaforo: reglas en orden descendente de min
    sem = recurso.get("semaforo",{})
    if sem:
        reglas = sem.get("reglas",[])
        mins   = [r.get("min",0) for r in reglas if isinstance(r,dict)]
        if mins != sorted(mins, reverse=True):
            E.append(f"{prefix} semaforo.reglas no estan en orden DESCENDENTE de 'min' — la primera regla cuyo min<=valor gana (el frontend itera de arriba abajo): {mins}")
        sobre = sem.get("sobre","")
        if sobre and sobre not in ctx:
            E.append(f"{prefix} semaforo.sobre='{sobre}' no es clave de ningun resultado")

# ── Contrato: contaminacion de catalogo (capa_2_options <-> capa_3_plan) ───────────
# Bug historico (sesion 5 ago 2026, ver §XXIII del plan y AUDITORIA_UX_30_SINTOMAS):
# capa_3_plan escrito para un sintoma distinto y pegado en el sitio equivocado —
# PSI-S3 traia herramientas de "cultura y valores", RES-S1 de "burnout individual",
# OPE-S1 de "procesos/Lean generico" (y antes, jul 2026, RES-S3 traia dependencia/
# backup en vez de conflicto/clima — §XVII.D). El motor no puede detectarlo solo
# (monta fielmente cualquier capa_3_plan que reciba), asi que el chequeo va aqui:
# solapamiento de vocabulario entre las 6 capa_2_options y los titulos/columnas de
# capa_3_plan. Es un AVISO heuristico, no un ERROR — puede haber falsos positivos
# legitimos (sintomas con mapeo mas indirecto, ej. DAFO), pero un ratio muy bajo
# siempre merece una revision humana.
CONTAMINACION_STOPWORDS = set("""
de la el en que un una y o no sin con para por tu su los las del al se si lo mas menos
este esta estos estas cada todo toda todos todas hay tiene tienes has he son sea ser
esta estas aunque como cual cuanto donde cuando quien mi mis tus sus nos les le da
das dan van voy vas ya muy poco pocos poca pocas mucho muchos mucha muchas otro otra
otros otras alguna algunas algun algunos ese esa esos esas eso algo nada nadie entre
sobre hasta desde porque pero bien mal ahi aqui alli asi solo solamente tener hacer
hace haces hacen puede pueden podria podrian debe deben deberia deberian sino tras
cabe segun mediante durante excepto salvo vez veces sido siendo estar estan sabe
""".split())

def _texto_significativo(txt):
    """Normaliza (sin acentos, minusculas) y devuelve el set de palabras de
    contenido (>=4 letras, fuera de la stopword list)."""
    plano = unicodedata.normalize("NFKD", txt or "").encode("ascii", "ignore").decode()
    palabras = re.findall(r"[a-zA-Z]{4,}", plano.lower())
    return {p for p in palabras if p not in CONTAMINACION_STOPWORDS}

def lint_contaminacion(s, W):
    c2 = s.get("capa_2_options", "")
    cp = s.get("capa_3_plan")
    if not isinstance(cp, dict) or not cp:
        return

    vocab_c2 = _texto_significativo(c2)
    if not vocab_c2:
        return

    partes_c3 = []
    for recurso in cp.values():
        if not isinstance(recurso, dict):
            continue
        partes_c3.append(recurso.get("titulo", ""))
        for sec in recurso.get("secciones", []) or []:
            partes_c3.append(sec.get("titulo", ""))
            for col in sec.get("columnas", []) or []:
                partes_c3.append(col.get("etiqueta", ""))
        for campo in recurso.get("campos", []) or []:
            partes_c3.append(campo.get("etiqueta", ""))
        for res in recurso.get("resultados", []) or []:
            partes_c3.append(res.get("etiqueta", ""))
    vocab_c3 = _texto_significativo(" ".join(partes_c3))

    overlap = vocab_c2 & vocab_c3
    ratio = len(overlap) / len(vocab_c2)
    if ratio < 0.15 or len(overlap) < 3:
        W.append(
            "posible CONTAMINACION de catalogo: capa_3_plan comparte muy poco vocabulario "
            f"con capa_2_options (solapan {len(overlap)}/{len(vocab_c2)} palabras clave, "
            f"{ratio:.0%}) — revisar si las 6 ramas de C3 responden de verdad a este sintoma "
            f"o se pegaron de otro. Palabras en comun: {sorted(overlap) or '(ninguna)'}"
        )

# ── Contrato: clave duplicada entre secciones sin entidad_compartida ───────────────
# Bug historico (5 ago 2026, reportado por cliente real con captura de pantalla): en
# UCI-S1.r1 el producto ya estaba enlazado por entidad_compartida, pero "Coste unitario"
# se repetia entre secciones porque el mecanismo solo cubria la columna 0 (identidad),
# no el resto de la fila. El frontend ya hereda por 'clave' cuando SI hay
# entidad_compartida (TreatmentPage.tsx, SeccionTablaNativa) -- este chequeo encuentra
# los casos donde deberia haberla y no la hay. AVISO, no ERROR: 'clave' tambien se
# reutiliza legitimamente como nombre de variable de formula en secciones sin relacion
# real (ej. NEURO-S1.r4 reutiliza 'meta'/'valor_actual' en 3 Objetivos independientes) --
# siempre revisar el contenido antes de enlazar, nunca aplicar en automatico.
def lint_clave_sin_enlazar(s, W):
    cp = s.get("capa_3_plan")
    if not isinstance(cp, dict):
        return
    for rk, recurso in cp.items():
        if not isinstance(recurso, dict) or recurso.get("tipo") != "nativa":
            continue
        secciones = recurso.get("secciones", []) or []
        if len(secciones) < 2:
            continue
        claves_por_seccion = []
        for sec in secciones:
            claves_por_seccion.append({c.get("clave"): c.get("etiqueta")
                                        for c in sec.get("columnas", []) or [] if c.get("clave")})
        for i in range(len(secciones)):
            for j in range(i + 1, len(secciones)):
                comunes = set(claves_por_seccion[i]) & set(claves_por_seccion[j])
                if not comunes:
                    continue
                ec_i, ec_j = secciones[i].get("entidad_compartida"), secciones[j].get("entidad_compartida")
                if ec_i and ec_i == ec_j:
                    continue  # ya enlazadas: el frontend hereda automaticamente por clave
                pares = [(cl, claves_por_seccion[i][cl]) for cl in sorted(comunes)]
                W.append(
                    f"capa_3_plan.{rk}: sec[{i}] y sec[{j}] comparten clave(s) {pares} sin "
                    "entidad_compartida -- revisar si es el mismo dato (retecleo real) o "
                    "coincidencia de nombre de variable en formulas independientes"
                )

# ── Contrato: entidad candidata a enlazar, sin declarar ────────────────────────────
# Detecta el patron que ya se corrigio a mano en UCI-S1 r1/r3/r5 (5 ago 2026): secciones
# tituladas secuencialmente ("1. ... / 2. ... / 3. ...") con columna 0 en texto libre en
# todas, sin entidad_compartida -- suele ser el mismo flujo sobre la misma entidad
# (cliente/producto/proyecto) y el cliente reteclea el nombre en cada tabla. AVISO
# heuristico: en la revision manual de la sesion 5 ago, 7 de 10 candidatos con este mismo
# patron se DESCARTARON por representar conceptos distintos pese al titulo secuencial
# (ej. CARDIO-S2.r3 seccion 1 define etapas del pipeline, seccion 2 rastrea oportunidades
# -- no son la misma entidad). Nunca aplicar el enlace sin leer las columnas primero.
def lint_entidad_candidata(s, W):
    cp = s.get("capa_3_plan")
    if not isinstance(cp, dict):
        return
    for rk, recurso in cp.items():
        if not isinstance(recurso, dict) or recurso.get("tipo") != "nativa":
            continue
        secciones = recurso.get("secciones", []) or []
        if len(secciones) < 2:
            continue
        secuencial = all(re.match(r"^\s*\d+\.", sec.get("titulo", "") or "") for sec in secciones)
        if not secuencial:
            continue
        if any(sec.get("entidad_compartida") for sec in secciones):
            continue
        col0_tipos = [sec["columnas"][0].get("tipo") if sec.get("columnas") else None for sec in secciones]
        if not all(t == "texto" for t in col0_tipos):
            continue
        col0_labels = [sec["columnas"][0].get("etiqueta", "") for sec in secciones]
        W.append(
            f"capa_3_plan.{rk}: secciones con titulo secuencial y columna 0 en texto libre "
            f"sin entidad_compartida {col0_labels} -- candidato a enlazar SOLO si representan "
            "la misma entidad real (leer las columnas antes de aplicar, no a ciegas)"
        )

# ── Contrato: dato de capas anteriores repreguntado en C3 ──────────────────────────
# Estandar del propio proyecto (§XV.B del plan, escrito meses antes de este bug real):
# "Si hay datos en C2, C3 no puede llegar vacio -- pre-rellenar todo lo disponible."
# Nunca se habia verificado. Compara el vocabulario de cada columna/campo de
# capa_3_plan contra los labels de C0 (input_a/input_b/inputs[].label) -- si una columna
# comparte la MAYORIA de sus palabras de contenido con un input de C0, es candidata a
# precargarse en vez de repreguntarse. AVISO: coincidencia parcial de vocabulario no
# siempre implica que sea literalmente el mismo dato.
def lint_capas_previas_repetidas(s, W):
    vocab_c0 = set()
    for _, lab in labels(s):
        vocab_c0 |= _texto_significativo(lab)
    if not vocab_c0:
        return
    cp = s.get("capa_3_plan")
    if not isinstance(cp, dict):
        return
    for rk, recurso in cp.items():
        if not isinstance(recurso, dict):
            continue
        columnas = []  # (etiqueta, ya_resuelto)
        for sec in recurso.get("secciones", []) or []:
            for c in sec.get("columnas", []) or []:
                if c.get("tipo") == "calculada":
                    continue
                columnas.append((c.get("etiqueta", ""), False))  # tablas nativas: sin mecanismo de precarga aun
        for c in recurso.get("campos", []) or []:
            columnas.append((c.get("etiqueta", ""), bool(c.get("precarga_desde_c0"))))
        for etiqueta, ya_resuelto in columnas:
            if ya_resuelto:
                continue  # ya tiene precarga_desde_c0 -- el hallazgo ya se resolvio, no repetir el aviso
            vocab_col = _texto_significativo(etiqueta)
            if len(vocab_col) < 2:
                continue
            comunes = vocab_col & vocab_c0
            if len(comunes) >= 2 and len(comunes) / len(vocab_col) >= 0.66:
                W.append(
                    f"capa_3_plan.{rk} col '{etiqueta}': solapa fuerte con un input de C0 "
                    f"{sorted(comunes)} -- candidato a precargar en vez de repreguntar (estandar SS.XV.B)"
                )

# ── Simulacion Paqui ──────────────────────────────────────────────────────────────
def simular_paqui(s):
    """Simula un recorrido C0-C3 con valores tipicos y reporta anomalias."""
    lines = []
    sid = s.get("symptom_id","")
    ia_label = s.get("input_a","")
    ib_label = s.get("input_b","—")

    ia, ib = 50000.0, 35000.0   # valores genericos representativos

    formula = s.get("kpi_formula","")
    try:
        contexto = {"InputA": ia, "InputB": ib}
        expr = formula
        for k,v in sorted(contexto.items(), key=lambda x: -len(x[0])):
            expr = expr.replace(k, str(float(v)))
        kpi_val = eval(expr, {"__builtins__": {}})  # noqa: S307
        lines.append(f"  C0: {ia_label}={ia:,.0f}  {ib_label}={ib:,.0f}  >> KPI={kpi_val:.2f} {s.get('kpi_unit','')}")
        obj = (s.get("kpi_objective") or "").strip()
        m = re.fullmatch(r"([<>≤≥])\s*(\d+[.,]?\d*)\s*%?", obj)
        if m:
            op_map = {"<": operator.lt, ">": operator.gt, "≤": operator.le, "≥": operator.ge}
            op_sym, threshold = m.group(1), float(m.group(2).replace(",","."))
            cumple = op_map[op_sym](kpi_val, threshold)
            lines.append(f"  Objetivo: {obj}  >> {'CUMPLE (OK para inicio)' if cumple else 'NO cumple (estado patologico, correcto)'}")
    except Exception as e:
        lines.append(f"  ⚠️  Error simulando KPI: {e}")

    # simular calculadoras en capa_3_plan
    cp = s.get("capa_3_plan",{})
    if isinstance(cp, dict):
        for rk, recurso in cp.items():
            if not isinstance(recurso,dict): continue
            if recurso.get("tipo") == "calculadora":
                campos = recurso.get("campos",[])
                resultados = recurso.get("resultados",[])
                ctx = {c.get("clave","x"+str(i)): 10.0 for i,c in enumerate(campos) if c.get("clave")}
                out_parts = []
                for r in resultados:
                    formula = r.get("formula","")
                    clave   = r.get("clave","")
                    if not formula: continue
                    resultado, err = evaluar_formula(formula, ctx)
                    if err:
                        out_parts.append(f"{clave}=ERROR({err})")
                    else:
                        ctx[clave] = resultado
                        out_parts.append(f"{clave}={resultado:.2f}")
                if out_parts:
                    lines.append(f"  {rk} calculadora: {' | '.join(out_parts)}")
    return lines

# ── Lint principal ────────────────────────────────────────────────────────────────
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
    else:  # financiero / conteo
        if not s.get("input_revised_1") or not s.get("input_revised_2"):
            W.append(f"recovery_mode '{rm}' sin input_revised_1/2 (recomendado para re-medicion manual en C6)")
    # --- input_revised no deben ser identicos al original (indicar medicion post) ---
    r1=s.get("input_revised_1",""); r2=s.get("input_revised_2","")
    if r1 and r1==s.get("input_a",""):
        W.append("input_revised_1 identico a input_a — debe reflejar la medicion post-tratamiento")
    if r2 and r2==s.get("input_b",""):
        W.append("input_revised_2 identico a input_b — debe reflejar la medicion post-tratamiento")
    # --- NEURO-S1: KPI gameable (InputB lo fija el cliente) ---
    if sid=="NEURO-S1":
        W.append("NEURO-S1: InputB es auto-fijado por el cliente (objetivo de facturacion) — KPI gameable; el frontend ya avisa si InputB < InputA*1.15")
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
    # --- herramientas: capa_3_plan ---
    herr_dir=os.path.join(os.path.dirname(os.path.abspath(RUTA)),"herramientas",sid)
    if os.path.isdir(herr_dir):
        basura=[fn for fn in os.listdir(herr_dir) if not fn.endswith(".html")]
        if basura: E.append(f"archivos que no son .html en herramientas/{sid}: {basura}")
        MED=["paciente","historia-clinica","turno","derivacion","instalaciones",
             "seguimiento-alta","cancelaciones","tratamiento"]
        med=[fn for fn in os.listdir(herr_dir) if any(t in fn.lower() for t in MED)]
        if med: W.append(f"herramientas con vocabulario de clinica medica: {med[:4]}{'…' if len(med)>4 else ''}")
    # --- footgun x30: 'dia' en el objetivo ---
    if re.search(r"d[ií]a", obj, re.I):
        W.append(f"kpi_objective contiene 'dia' -> conversion mes->dia activa: {obj!r}")
    # --- formato mixto en options ---
    for campo in ("capa_1_options","capa_2_options"):
        v=s.get(campo)
        if isinstance(v,str) and "\n" in v:
            W.append(f"{campo} contiene salto de linea (formato mixto)")
    # --- CONTRATOS FASE 6: motor nativo ──────────────────────────────────────────
    lint_capa3(s, E, W)
    # --- contaminacion de catalogo (capa_2_options <-> capa_3_plan) ──────────────
    lint_contaminacion(s, W)
    # --- criterios sesion 5 ago 2026 (bug real "coste unitario" + estandar SS.XV.B) --
    lint_clave_sin_enlazar(s, W)
    lint_entidad_candidata(s, W)
    lint_capas_previas_repetidas(s, W)
    return E, W, fam

def main():
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    d=json.load(open(RUTA,encoding="utf-8"))
    print(f"Linter clinico MASFRAME v2 — {len(d)} sintomas\n"+"="*60)
    nE=nW=0; fam_count={}
    for s in d:
        E,W,fam=lint(s)
        fam_count[fam]=fam_count.get(fam,0)+1
        if E or W:
            print(f"\n[{s.get('symptom_id','??')}] {s.get('kpi_name','')}  (C2: {fam})")
            for e in E: print(f"   ERROR: {e}")
            for w in W: print(f"   AVISO: {w}")
        if SIM:
            sim_lines = simular_paqui(s)
            if sim_lines:
                if not (E or W):
                    print(f"\n[{s.get('symptom_id','??')}] {s.get('kpi_name','')}")
                for l in sim_lines: print(l)
        nE+=len(E); nW+=len(W)
    print("\n"+"="*60)
    print("COBERTURA de familias C2:", ", ".join(f"{k}:{v}" for k,v in sorted(fam_count.items())))
    print(f"RESULTADO: {nE} ERRORES · {nW} avisos")
    sys.exit(1 if nE else 0)

if __name__=="__main__":
    main()
