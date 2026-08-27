# -*- coding: utf-8 -*-
"""
auditar_sintoma.py — diagnostico mecanico de un sintoma o de una especialidad entera.

Automatiza todas las comprobaciones que en la sesion del 22 ago 2026 se hicieron a mano,
una a una, durante horas. Es el PASO 2 del validador (el 1 es la cadena clinica, que es
juicio y no se automatiza; el 3 es la propuesta de criterio).

    python data/auditar_sintoma.py NEURO-S1
    python data/auditar_sintoma.py NEURO          # los 3 de la especialidad
    python data/auditar_sintoma.py --todos

Sale 0 si no hay defectos BLOQUEANTES, 1 si los hay. Los AVISO no cortan.
NO toca ningun fichero: solo lee y reporta.
"""
import io, json, os, re, sys, unicodedata

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "symptoms.json")

# El mismo regex del motor (TreatmentPage.tsx, ACCION_REGEX). Si cambia alli, cambia aqui.
ACCION = re.compile(r"acci[oó]n|mejora|plan\b|acuerdo|ajuste|paso\b|tarea|decisi[oó]n|siguiente", re.I)

# Registro del copy: lo entienden Manoli, Paqui y Felipe, y aun asi suena profesional.
JERGA = ["okr", "key result", "kpi", "funnel", "roi", "lead", "pipeline", "stakeholder",
         "benchmark", "core", "target", "input ", "output", "dafo", "kaizen"]
COLOQUIAL = ["me pongo", "te lo curras", "un poquito", "rollo", "chungo", "movida", "cacharro"]
# Ni una falta de respeto. El dueno no es el problema: el problema es que nadie le ha dado el
# sistema. Cualquier texto que le culpe, insinue dejadez o le haga justificarse esta PROHIBIDO --
# y es bloqueante, no aviso. (23 ago 2026, NEURO-S1.r2: "Podria dejar si te centraras" salio a
# produccion; "estas llamando imbecil a mis clientes".)
CULPA = ["si te centraras", "si te centrases", "si te lo tomaras", "si te lo tomases",
         "si le dedicaras", "si le dedicases", "si te esforzaras", "si te esforzases",
         "deberias", "tendrias que haber", "no le prestas", "lo tienes abandonado",
         "por no haber", "por dejadez", "descuidado", "no te preocupas", "te falta interes"]
TRIMESTRE_Q = re.compile(r"\bQ[1-4]\b|pr[oó]ximo Q\b|\bQ\b")

VACIAS = set("""a al algo ante antes aqui asi aun aunque bien cada como con contra cual cuales
cuando de del desde donde dos e el ella ellas ello ellos en entre era eran es esa esas ese eso
esos esta estan estar estas este esto estos ha hace hacer hacia hasta hay la las le les lo los
mas me mi mis mucho muy nada ni no nos nuestra nuestro o para pero poco por porque que se sea
segun ser si sin sobre solo son su sus tambien tampoco tan tanto te tener tengo tiene tienen
todo todos tu tus un una uno unos y ya yo total al del""".split())


def norm(t):
    t = unicodedata.normalize("NFD", (t or "").lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def toks(t):
    return {w for w in re.findall(r"[a-z]{4,}", norm(t)) if w not in VACIAS}


def opts(s, campo):
    v = s.get(campo, "")
    if isinstance(v, list):
        return [x.strip() for x in v if x and x.strip()]
    return [x.strip() for x in v.split(";") if x.strip()]


class Informe:
    def __init__(self, sid, nombre):
        self.sid, self.nombre = sid, nombre
        self.bloq, self.avisos = [], []

    def B(self, donde, msg):
        self.bloq.append((donde, msg))

    def A(self, donde, msg):
        self.avisos.append((donde, msg))

    def pinta(self):
        estado = "🔴 BLOQUEADO" if self.bloq else ("🟠 con avisos" if self.avisos else "🟢 limpio")
        print(f"\n{'='*78}\n{self.sid} · {self.nombre}   {estado}\n{'='*78}")
        for donde, m in self.bloq:
            print(f"  🔴 {donde:<14} {m}")
        for donde, m in self.avisos:
            print(f"  🟠 {donde:<14} {m}")
        if not self.bloq and not self.avisos:
            print("  sin defectos mecanicos")


def auditar(s):
    r = Informe(s["symptom_id"], s.get("symptom_name", ""))
    plan = s.get("capa_3_plan") or {}
    c1, c2 = opts(s, "capa_1_options"), opts(s, "capa_2_options")
    vocab_c0 = toks(s.get("input_a", "")) | toks(s.get("input_b", ""))

    # ── 1. Cadena: 6 y 6, y una rama por opcion ────────────────────────────────
    if len(c1) != 6:
        r.B("C1", f"capa_1_options tiene {len(c1)} items, deben ser 6 (I-1)")
    if len(c2) != 6:
        r.B("C2", f"capa_2_options tiene {len(c2)} items, deben ser 6 (I-1)")
    for i in range(len(c2)):
        if f"r{i+1}" not in plan:
            r.B("C2->C3", f"la opcion {i+1} no tiene rama r{i+1}: el cliente la elige y no pasa nada")

    # ── 2. Alineacion 1:1 por significado (el motor une por POSICION) ──────────
    for i, (p, dec) in enumerate(zip(c1, c2)):
        sol = toks(p) & toks(dec)
        rama = plan.get(f"r{i+1}")
        titulo = rama.get("titulo", "") if isinstance(rama, dict) else ""
        sol_r = toks(dec) & toks(titulo)
        # El solape de vocabulario es un proxy MALO por si solo (SS.LV.F: la duplicacion y el
        # desalineamiento son de significado, no de palabras). Solo se reporta cuando falla la
        # cadena entera para el mismo indice -- ahi si suele haber algo. Y aun asi es "leelo",
        # nunca un veredicto.
        if len(sol) == 0 and titulo and len(sol_r) == 0:
            r.A("C1→C2→C3", f"#{i+1}: problema, decision y rama r{i+1} ('{titulo[:34]}') no comparten "
                            f"vocabulario en ningun salto -- LEELOS, puede que no hablen de lo mismo")

    # ── 3. Por rama y seccion ──────────────────────────────────────────────────
    rama_con_accion = set()
    for rk in sorted(plan, key=lambda k: (len(k), k)):
        v = plan[rk]
        if not isinstance(v, dict):
            continue
        tipo = v.get("tipo")
        if tipo != "nativa":
            r.A(rk, f"tipo '{tipo}': fuera del alcance de vista:tarjeta y de estas comprobaciones")
            continue
        for si, sec in enumerate(v.get("secciones", []), 1):
            d = f"{rk}.s{si}"
            cols = sec.get("columnas", []) or []
            claves = {c.get("clave") for c in cols if c.get("clave")}

            # 3a · una sola columna accionable
            # Mismo orden de resolucion que columnasDecision() en TreatmentPage.tsx (27 ago 2026):
            # es_decision manda; si no la hay, el regex; y entre varias candidatas gana la de
            # opciones cerradas. Solo es colision cuando el motor TAMPOCO puede desempatar --
            # avisar de las que ya resuelve seria gritar en falso.
            usables = [c for c in cols if c.get("tipo") != "calculada"]
            explicitas = [c["etiqueta"] for c in usables if c.get("es_decision")]
            if explicitas:
                acc = explicitas
                if len(explicitas) > 1:
                    r.B(d, f"{len(explicitas)} columnas con es_decision: C4 recibira varias -- {explicitas}")
            else:
                candidatas = [c for c in usables if ACCION.search(c.get("etiqueta", ""))]
                cerradas = [c for c in candidatas if c.get("tipo") in ("opciones", "decision")]
                acc = [c["etiqueta"] for c in (cerradas or candidatas)]
                if len(candidatas) > 1 and len(acc) > 1:
                    r.B(d, f"colision ACCION_REGEX sin desempate: {acc} -- C4 recibira la columna equivocada")
                elif len(candidatas) > 1:
                    r.A(d, f"varias casan el regex pero el motor desempata por opciones cerradas: {acc[0]} -- declara es_decision para no dejarlo al azar")
            if acc:
                rama_con_accion.add(rk)

            # 3b · el TOTAL tiene que significar UNA cosa
            suman = [c["etiqueta"] for c in cols
                     if c.get("tipo") in ("numero", "calculada") and not c.get("no_sumar")]
            cv = [c["etiqueta"] for c in cols if c.get("contribuye_valor")]
            if len(cv) > 1:
                r.B(d, f"{len(cv)} columnas contribuye_valor: el KPI cuenta de mas -- {cv}")
            if len(suman) > 1:
                r.B(d, f"el TOTAL suma {len(suman)} columnas distintas {suman} -- pon no_sumar en "
                       f"todas menos la que de verdad acumula")
            if suman and cv and suman != cv:
                r.A(d, f"el TOTAL ({suman}) no coincide con lo que alimenta el KPI ({cv})")
            for c in cols:
                if c.get("contribuye_valor") and not c.get("unidad") and c.get("tipo") == "numero":
                    r.A(d, f"'{c['etiqueta']}' suma al KPI sin `unidad`: el total sale sin €")

            # 3c · opciones pre-marcadas (sesgan antes de que toque nada)
            # filaVaciaHerramienta ya arranca en blanco las columnas que el motor reconoce como
            # accion o condicion. Avisar de esas seria gritar en falso: aqui solo las demas.
            protegida = lambda c: (ACCION.search(c.get("etiqueta", ""))
                                   or c.get("contribuye_valor_si") is not None
                                   or c.get("cuenta_unicos_si") is not None)
            prem = [c["etiqueta"] for c in cols
                    if c.get("tipo") == "opciones" and (c.get("opciones") or [""])[0] != ""
                    and not protegida(c)]
            if prem:
                r.B(d, f"opciones pre-marcadas por defecto: {prem} -- responde por el cliente")

            # 3d · formulas
            for c in cols:
                if c.get("tipo") != "calculada":
                    continue
                f = c.get("formula", "")
                malas = [t for t in re.findall(r"[a-z_][a-z0-9_]*", f) if t not in claves]
                if malas:
                    r.B(d, f"'{c['etiqueta']}': la formula '{f}' usa claves inexistentes {malas}")
                precargadas = {c2.get("clave") for c2 in cols if c2.get("precarga_desde_c0")}
                div = [x for x in re.findall(r"/\s*([a-z_][a-z0-9_]*)", f) if x not in precargadas]
                if div:
                    r.A(d, f"'{c['etiqueta']}': divide por {div} -- si el cliente deja ese campo a 0, "
                           f"sale un numero absurdo")

            # 3e · veredicto
            # Una seccion origen_margen no necesita veredicto propio: repite tal cual el que el
            # cliente ya vio en C2 (Pilar / Optimizable / Destructor), que es justo el punto del
            # formato -- C3 no recalcula, hereda.
            hay_numeros = any(c.get("tipo") in ("numero", "calculada") for c in cols)
            interp = sec.get("interpretacion")
            if not interp and not sec.get("origen_margen") and hay_numeros:
                r.A(d, "sin `interpretacion`: el cliente ve un numero y nadie le dice que significa")
            elif interp and interp.get("clave") not in claves:
                r.B(d, f"`interpretacion` apunta a la clave '{interp.get('clave')}', que no existe")

            # 3f · presentacion
            if sec.get("vista") != "tarjeta":
                r.A(d, "sin vista:'tarjeta': se pinta como tabla cruda")
            fi = sec.get("filas_iniciales")
            if fi and fi > 3:
                r.A(d, f"filas_iniciales={fi}: {fi} tarjetas en blanco al abrir. La repeticion se gana")
            if len(cols) > 8:
                r.A(d, f"{len(cols)} campos por fila: es un formulario, no una tarjeta")

            # 3g · confirmaciones (C4 pregunta '¿ya lo hiciste?')
            for c in cols:
                if c.get("tipo") != "opciones" or not ACCION.search(c.get("etiqueta", "")):
                    continue
                conf = c.get("confirmaciones") or {}
                reales = [o for o in (c.get("opciones") or []) if o]
                if not conf:
                    r.A(d, f"'{c['etiqueta']}' sin `confirmaciones`: C4 repetira la decision en vez "
                           f"de preguntar si ya se hizo")
                else:
                    faltan = [o for o in reales if o not in conf]
                    sobran = [k for k in conf if k not in reales]
                    if faltan or sobran:
                        r.B(d, f"`confirmaciones` descuadradas: faltan {faltan}, sobran {sobran}")

            # 3h · repreguntar lo que ya esta en C0
            for c in cols:
                if c.get("precarga_desde_c0") or c.get("tipo") == "calculada":
                    continue
                vc = toks(c.get("etiqueta", ""))
                com = vc & vocab_c0
                if len(vc) >= 2 and len(com) >= 2 and len(com) / len(vc) >= 0.66:
                    r.A(d, f"'{c['etiqueta']}' repregunta un dato de C0 {sorted(com)}: usa "
                           f"precarga_desde_c0")

            # 3i · registro del copy
            for c in cols:
                e = c.get("etiqueta", "")
                textos = [e] + [o for o in (c.get("opciones") or []) if o] \
                             + list((c.get("confirmaciones") or {}).values())
                for t in textos:
                    n = norm(t)
                    for j in JERGA:
                        if j in n:
                            r.A(d, f"jerga '{j}' en «{t[:52]}»")
                    for cq in COLOQUIAL:
                        if cq in n:
                            r.B(d, f"copy coloquial '{cq}' en «{t[:52]}» -- no suena profesional")
                    for cu in CULPA:
                        if cu in n:
                            r.B(d, f"FALTA DE RESPETO: '{cu}' en «{t[:52]}» -- el copy culpa al "
                                   f"dueno. El problema es que nadie le ha dado el sistema, no el")
                    if TRIMESTRE_Q.search(t):
                        r.A(d, f"«{t[:52]}» usa 'Q' -- di 'trimestre'")

    for rk, v in plan.items():
        if isinstance(v, dict) and v.get("tipo") == "nativa" and rk not in rama_con_accion:
            # Bloqueante desde el 27 ago 2026, no aviso. El cliente puede recorrer la rama entera,
            # rellenarla y salir de C3 sin que C4 reciba una sola tarea: el tratamiento no produce
            # plan. Y ahora ademas la puerta de C3 tiene que dejarlas pasar a proposito (no se le
            # puede exigir una decision a quien no tiene donde tomarla, tarjetaPuedeDecidir), asi
            # que si esto no fuera bloqueante el defecto quedaria escondido para siempre.
            if any(c.get("contramedidas") for sec in v.get("secciones", []) for c in sec.get("columnas", []) or []):
                continue  # baja a C4 por contramedidas, no por columna de decision
            r.B(rk, "ninguna columna de decision en toda la rama: el cliente la completa y C4 no recibe nada")

    # El diagnostico de C2 tambien es copy que ve el cliente, y es justo donde se colo la frase.
    for i, cfg in enumerate(s.get("c2_diagnostico") or []):
        if not cfg:
            continue
        textos = [cfg.get("hint", ""), cfg.get("placeholder", "")]                + [c.get("etiqueta", "") for c in cfg.get("campos", [])]                + [l.get("etiqueta", "") for l in cfg.get("lineas", [])]                + [(cfg.get("alerta") or {}).get("texto", "")]
        for t in textos:
            n = norm(t)
            for cu in CULPA:
                if cu in n:
                    r.B(f"c2.causa{i+1}", f"FALTA DE RESPETO: '{cu}' en «{t[:52]}»")
            # Un campo que pide una estimacion es un dato inventado: el veredicto que salga de ahi
            # no vale nada. Los dos numeros tienen que estar ya en su contabilidad.
            for est in ("podria", "seria razonable", "crees que", "estimado", "aproximad", "si te "):
                if est in n and t in [c.get("etiqueta", "") for c in cfg.get("campos", [])]:
                    r.B(f"c2.causa{i+1}", f"dato inventado: «{t[:52]}» pide una estimacion, no un "
                                          f"numero que el cliente tenga")

    # ── 4. KPI y modo ──────────────────────────────────────────────────────────
    modo = s.get("kpi_recovery_mode")
    if modo not in ("financiero", "estructural", "conteo", None):
        r.B("C6", f"kpi_recovery_mode invalido: {modo}")
    ALIMENTA = ("contribuye_valor", "contribuye_valor_si", "cuenta_unicos_si", "suma_si")
    tot_cv = sum(1 for v in plan.values() if isinstance(v, dict)
                 for sec in v.get("secciones", []) for c in sec.get("columnas", [])
                 if any(c.get(k) is not None for k in ALIMENTA))
    if modo in ("financiero", "conteo") and tot_cv == 0:
        r.B("C6", f"modo '{modo}' pero ninguna columna contribuye_valor: el KPI no puede moverse "
                  f"y el alta queda bloqueada")
    if modo == "estructural" and tot_cv > 0:
        r.A("C6", "modo 'estructural' con columnas contribuye_valor: en estructural el KPI se cierra "
                  "re-midiendo, esos euros no lo mueven")
    return r


def main():
    args = [a for a in sys.argv[1:] if a]
    if not args:
        print(__doc__)
        return 0
    datos = json.loads(io.open(RUTA, encoding="utf-8").read())
    if "--todos" in args:
        objetivo = datos
    else:
        q = args[0].upper()
        objetivo = [s for s in datos if s["symptom_id"] == q or s["symptom_id"].startswith(q + "-")]
    if not objetivo:
        print(f"No encuentro '{args[0]}'. Ej: NEURO-S1, NEURO, --todos")
        return 2

    print(f"Auditoria mecanica — {len(objetivo)} sintoma(s)")
    informes = [auditar(s) for s in objetivo]
    for i in informes:
        i.pinta()
    nb = sum(len(i.bloq) for i in informes)
    na = sum(len(i.avisos) for i in informes)
    print(f"\n{'='*78}\nRESULTADO: {nb} bloqueantes · {na} avisos "
          f"({sum(1 for i in informes if not i.bloq)}/{len(informes)} sin bloqueantes)")
    print("\nEsto es solo lo mecanico. La cadena clinica (PASO 0) y el juicio de negocio\n"
          "no se automatizan: van antes que esto y despues de esto.")
    return 1 if nb else 0


if __name__ == "__main__":
    sys.exit(main())
