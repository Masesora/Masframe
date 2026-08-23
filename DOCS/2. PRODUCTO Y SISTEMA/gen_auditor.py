import json, re

with open(r'C:\Masframe\masesora_backend\data\symptoms.json', 'r', encoding='utf-8') as f:
    SYMS = json.load(f)

# ─── TOOL TAXONOMY ────────────────────────────────────────────────────────────
TOOL_TAX = {
    'Impacto vs Esfuerzo':                ('matrix_2x2',    'Matriz 2×2',            'El cliente ordena qué atacar primero por valor vs dificultad'),
    'Urgente vs Importante':              ('matrix_2x2',    'Matriz 2×2',            'El cliente separa lo urgente de lo estratégicamente importante'),
    'Urgente vs Importante (estratégico)':('matrix_2x2',    'Matriz 2×2 estratégica','El cliente separa urgente de importante en clave de dirección de negocio'),
    'Árbol de Decisiones':                ('decision_tree', 'Árbol de decisión',     'El cliente elige entre opciones mutuamente excluyentes con criterios'),
    'Análisis de Riesgos':                ('risk_table',    'Tabla de riesgos',      'El cliente evalúa probabilidad e impacto de cada riesgo'),
    'Analisis de riesgos':                ('risk_table',    'Tabla de riesgos',      'El cliente evalúa probabilidad e impacto de cada riesgo'),
    'Regla 5/25':                         ('priority_list', 'Lista de foco radical', 'El cliente elimina todo excepto 2-3 prioridades absolutas'),
    'DAFO de Diferenciación':             ('dafo',          'Análisis DAFO',         'El cliente mapea fortalezas diferenciales vs posición competitiva'),
    'DAFO de valor':                      ('dafo',          'Análisis DAFO de valor','El cliente analiza dónde crea valor real vs percibido'),
    'Radiografía de retención':           ('custom_calc',   'Calculadora de retención','El cliente cuantifica qué actividad/cliente destruye margen'),
    'Semáforo de Viabilidad':             ('custom_calc',   'Calculadora de viabilidad','El cliente calcula precio mínimo viable por servicio'),
    'Análisis de Carga':                  ('analysis',      'Análisis de carga operativa','El cliente identifica el origen del colapso de capacidad'),
    'Análisis de capacidad y carga':      ('analysis',      'Análisis de capacidad','El cliente cuantifica el tipo de irregularidad de su operación'),
    'VSM (mapa de flujo de cobro)':       ('flow_map',  'Mapa de flujo de valor',    'El cliente ve dónde se pierde tiempo en el ciclo de cobro'),
    'VSM (flujo operativo)':              ('flow_map',  'Mapa de flujo de valor',    'El cliente ve dónde se acumulan esperas y cuellos de botella'),
    'VSM financiero':                     ('flow_map',  'Mapa de flujo financiero',  'El cliente ve el ciclo completo de cierre contable'),
    'VSM de flujo operativo':             ('flow_map',  'Mapa de flujo de valor',    'El cliente ve dónde se acumula carga y dónde se pierde ritmo'),
    'Análisis causa-efecto':              ('cause_eff', 'Diagrama causa-efecto',     'El cliente identifica causas raíz del problema priorizado'),
    'Análisis causa–efecto':              ('cause_eff', 'Diagrama causa-efecto',     'El cliente identifica causas raíz del problema priorizado'),
    'Análisis causa efecto':              ('cause_eff', 'Diagrama causa-efecto',     'El cliente identifica causas raíz del problema priorizado'),
    'Análisis de estructura de costes':   ('fin_anal',  'Análisis de costes',        'El cliente ve qué coste concreto destruye su margen por línea'),
    'Ishikawa':                           ('cause_eff', 'Diagrama de Ishikawa',      'El cliente mapea todas las causas posibles de un fallo desde 6 dimensiones'),
    '5 Porqués':                          ('root_cause','5 Porqués',                 'El cliente llega a la causa raíz preguntando "por qué" cinco veces'),
    'Auditoría Comercial':                ('comm_audit','Auditoría comercial',        'El cliente ve qué canal genera oportunidades reales y cuál es ruido'),
    'Mapa de Canales':                    ('channel_m', 'Mapa de canales comerciales','El cliente ve en qué punto del pipeline se estanca la venta'),
    'Mapa de Credibilidad':               ('cred_map',  'Mapa de credibilidad',      'El cliente entiende qué le falta para que el mercado confíe en él'),
    'Mapa Estratégico':                   ('strat_map', 'Mapa estratégico',          'El cliente traduce su dirección elegida en objetivos y relaciones causa-efecto'),
    'Mapa de Prioridades':                ('prio_map',  'Mapa de prioridades',       'El cliente ve qué acciones mueven resultados de verdad vs qué consume tiempo'),
    'Mapa de carga fiscal':               ('fin_anal',  'Mapa de carga fiscal',      'El cliente ve exactamente qué impuesto y qué estructura le cuesta más'),
    'Mapa de Responsabilidades':          ('role_map',  'Mapa de responsabilidades', 'El cliente ve quién hace qué y dónde hay huecos o solapamientos'),
    'Mapa de Identidad':                  ('id_map',    'Mapa de identidad de marca','El cliente visualiza su esencia diferencial vs percepción actual'),
    'Mapa de Territorio':                 ('pos_map',   'Mapa de posicionamiento',   'El cliente ve su espacio competitivo y dónde hay huecos diferenciables'),
    'Mapa de Mensajes':                   ('msg_map',   'Mapa de mensajes',          'El cliente ve cómo habla su marca y dónde hay inconsistencias'),
    'Mapa de Tension':                    ('tens_map',  'Mapa de tensión',           'El cliente ve en qué momentos y por qué el equipo entra en modo crisis'),
    'SIPOC de roles':                     ('role_map',  'Tabla SIPOC de roles',      'El cliente mapea quién hace qué en cada etapa y dónde hay solapamientos o vacíos'),
    'Mapa de Energia':                    ('energy_m',  'Mapa de energía del equipo','El cliente ve dónde y cuándo el equipo pierde motivación e iniciativa'),
    'Mapa de competencias vs tareas reales':('comp_map','Mapa de competencias',      'El cliente ve qué hace cada persona vs qué podría hacer con su nivel real'),
    'Mapa de clima y fricciones':         ('climate_m', 'Mapa de clima y fricciones','El cliente ve dónde se concentran las tensiones y qué las alimenta'),
    'Customer Journey Map':               ('journey_m', 'Mapa de experiencia',       'El cliente recorre la experiencia de su cliente momento a momento'),
    'Mapa de emociones':                  ('emotion_m', 'Mapa de emociones',         'El cliente identifica señales emocionales que anuncian la desconexión del cliente'),
    'Kaizen de liquidez':                 ('kaizen',    'Plan Kaizen de liquidez',   'El cliente ejecuta mejoras de caja con responsable, acción y plazo'),
    'Kaizen operativo':                   ('kaizen',    'Plan Kaizen operativo',     'El cliente ejecuta mejoras de proceso con responsable y plazo'),
    'Kaizen administrativo':              ('kaizen',    'Plan Kaizen administrativo','El cliente ejecuta mejoras de gestión interna con responsable y plazo'),
    'Kaizen emocional':                   ('kaizen',    'Plan Kaizen emocional',     'El cliente actúa sobre los detonantes de tensión identificados'),
    'Kaizen de experiencia':              ('kaizen',    'Plan Kaizen de experiencia','El cliente mejora los momentos críticos del journey del cliente'),
    'Rediseño de portafolio':             ('redesign',  'Rediseño de portafolio',    'El cliente ajusta qué ofrece, a quién y a qué precio con datos reales'),
    'Rediseño de pricing y costes':       ('redesign',  'Rediseño de precio y costes','El cliente fija precio mínimo viable y corta los costes que erosionan el margen'),
    'Rediseño de intake':                 ('redesign',  'Rediseño del intake',       'El cliente transforma cómo entra la información para eliminar reprocesos'),
    'Rediseño de asignaciones':           ('redesign',  'Rediseño de asignaciones',  'El cliente mueve a cada persona al trabajo donde su nivel genera más valor'),
    'Rediseño de estructura fiscal':      ('redesign',  'Rediseño fiscal',           'El cliente implementa la estructura fiscal más eficiente para su situación'),
    'Rediseño de Criterios':              ('redesign',  'Protocolo de decisión',     'El cliente diseña nuevas reglas que reemplazan la improvisación'),
    'Rediseño de valor':                  ('redesign',  'Rediseño de valor',         'El cliente rediseña momentos de entrega para hacer el valor visible'),
    'Redistribución de autoridad':        ('auth_red',  'Mapa de autoridad',         'El cliente reasigna quién decide qué para eliminar cuellos de botella'),
    'Plan de calidad continua':           ('action_pl', 'Plan de calidad',           'El cliente ejecuta mejoras para cerrar las brechas que generan retrabajo'),
    'Plan de Activación':                 ('action_pl', 'Plan de activación',        'El cliente pone en marcha acciones concretas para avanzar el pipeline'),
    'Plan de Prueba de Valor':            ('action_pl', 'Plan de prueba de valor',   'El cliente prueba su propuesta con métricas reales antes de escalar'),
    'Plan de reactivación de equipo':     ('action_pl', 'Plan de reactivación',      'El cliente actúa sobre los factores que apagan la energía del equipo'),
    'Plan de retención':                  ('action_pl', 'Plan de retención',         'El cliente define acciones concretas para retener a personas clave'),
    'Plan de resolución de conflicto':    ('action_pl', 'Plan de resolución',        'El cliente gestiona el conflicto con criterio antes de que cueste más'),
    'Plan de reconducción':               ('action_pl', 'Plan de reconducción',      'El cliente recupera al cliente molesto con pasos concretos y en caliente'),
    'Arquitectura Comercial':             ('comm_arch', 'Arquitectura comercial',    'El cliente construye el motor de demanda que atrae el cliente adecuado'),
    'Definición de Objetivos':            ('def_tool',  'Definición de objetivos',   'El cliente convierte la dirección estratégica en compromisos con métricas y fechas'),
    'Definición de Agenda Estratégica':   ('def_tool',  'Agenda estratégica',        'El cliente protege tiempo para lo estratégico y filtra lo operativo'),
    'Definición de Roles':                ('def_tool',  'Definición de roles',       'El cliente clarifica quién decide qué y elimina la dependencia del dueño'),
    'Definición de Narrativa':            ('def_tool',  'Narrativa de marca',        'El cliente fija el mensaje que transmite su valor diferencial'),
    'Definición de Propuesta Única':      ('def_tool',  'Propuesta única',           'El cliente define en una frase por qué elegirle — y eso cierra ventas'),
    'Definición de Tono':                 ('def_tool',  'Guía de tono',              'El cliente establece cómo habla su marca para que sea reconocible'),
    'Nivelación de carga (Heijunka)':     ('heijunka',  'Nivelación de carga',       'El cliente distribuye la carga de forma sostenida para eliminar picos'),
}

COMPAT_C2_C3 = {
    'matrix_2x2':    ['flow_map','cause_eff','fin_anal','role_map','comm_audit','channel_m',
                      'strat_map','prio_map','id_map','pos_map','msg_map','tens_map',
                      'comp_map','climate_m','emotion_m','energy_m','cred_map'],
    'decision_tree': ['role_map','strat_map','climate_m','cred_map','fin_anal','comp_map','prio_map'],
    'risk_table':    ['root_cause','cause_eff','comm_audit','cred_map','emotion_m','five_why'],
    'priority_list': ['flow_map','cause_eff','tens_map','energy_m','msg_map','comm_audit'],
    'dafo':          ['pos_map','id_map','emotion_m','msg_map'],
    'custom_calc':   ['flow_map','fin_anal','cause_eff'],
    'analysis':      ['cause_eff','flow_map','comp_map','root_cause'],
}
COMPAT_C2_C3['risk_table'].append('five_why')

COMPAT_C3_C4 = {
    'flow_map':   ['kaizen','heijunka','redesign'],
    'cause_eff':  ['kaizen','redesign','action_pl'],
    'fin_anal':   ['redesign','kaizen','action_pl'],
    'root_cause': ['kaizen','action_pl','redesign'],
    'role_map':   ['auth_red','def_tool','redesign'],
    'strat_map':  ['def_tool','action_pl'],
    'prio_map':   ['def_tool','action_pl'],
    'comm_audit': ['comm_arch','action_pl'],
    'channel_m':  ['action_pl','comm_arch'],
    'cred_map':   ['action_pl','comm_arch'],
    'id_map':     ['def_tool'],
    'pos_map':    ['def_tool'],
    'msg_map':    ['def_tool'],
    'tens_map':   ['kaizen','redesign'],
    'energy_m':   ['action_pl','redesign'],
    'comp_map':   ['redesign','def_tool','auth_red'],
    'climate_m':  ['action_pl','redesign'],
    'journey_m':  ['kaizen','redesign','action_pl'],
    'emotion_m':  ['action_pl','redesign'],
}

def expected_justi2(c2_type, c2_name, c2_opts_sample):
    t = {
        'matrix_2x2':   f'La {c2_name} ordena cada palanca por impacto real vs esfuerzo para que el tratamiento entre donde más se mueve el KPI con el mínimo desgaste.',
        'decision_tree':f'El {c2_name} convierte las opciones de C1 en caminos mutuamente excluyentes para que cierres la dirección con datos, no con intuición.',
        'risk_table':   f'La {c2_name} convierte la percepción de amenaza en jerarquía medible para que el tratamiento entre donde mayor daño potencial hay.',
        'priority_list':f'La {c2_name} elimina todo excepto las 2-3 prioridades absolutas para que el tratamiento entre con un foco único y ejecutable.',
        'dafo':         f'El {c2_name} localiza dónde el negocio es más vulnerable y dónde tiene ventaja defendible para que actúes donde más retorno real hay.',
        'custom_calc':  f'La calculadora cuantifica el dato exacto que define el problema para que cada decisión en C4 tenga una consecuencia medida de antemano.',
        'analysis':     f'El {c2_name} clasifica el problema por frecuencia, coste e impacto para que el tratamiento entre donde más daño se concentra.',
    }
    return t.get(c2_type, f'"{c2_name}" convierte las opciones de C1 en una jerarquía clínica para que intervengas con criterio y datos.')

def expected_justi3(c3_type, c3_name, c2_name):
    t = {
        'flow_map':   f'El {c3_name} hace visible el flujo completo para que identifiques exactamente dónde se pierde tiempo y dónde se acumula carga sin valor.',
        'cause_eff':  f'El {c3_name} traza el camino desde el síntoma hasta la causa raíz de lo priorizado en C2 para que C4 actúe directamente en el origen.',
        'fin_anal':   f'El {c3_name} traduce la decisión de C2 en números concretos por línea, servicio o cliente para que cada acción en C4 esté respaldada por un dato.',
        'root_cause': f'Los {c3_name} desmontan la explicación superficial capa a capa para que identifiques el origen exacto antes de diseñar cualquier cambio.',
        'role_map':   f'El {c3_name} mapea quién hace qué, qué entra y qué sale para que redistribuyas sobre lo que realmente ocurre en el proceso.',
        'strat_map':  f'El {c3_name} traduce la dirección elegida en C2 en objetivos con relaciones causa-efecto para que C4 baje la visión a acciones concretas.',
        'prio_map':   f'El {c3_name} separa las prioridades que mueven resultados de las que consumen energía para que diseñes solo lo que genera impacto real.',
        'comm_audit': f'La {c3_name} revela qué canal genera oportunidades calificadas para que actives lo que funciona y liberes la energía que drena.',
        'channel_m':  f'El {c3_name} localiza en qué etapa del pipeline se estanca la venta para que intervengas en el punto exacto del bloqueo.',
        'cred_map':   f'El {c3_name} identifica qué genera confianza en el mercado para que construyas exactamente lo que aún falta.',
        'id_map':     f'El {c3_name} visualiza la esencia diferencial frente a cómo se percibe hoy para que C4 cierre ese gap con acciones concretas.',
        'pos_map':    f'El {c3_name} mapea el espacio competitivo y expone los huecos diferenciables para que ocupes ese territorio con ventaja.',
        'msg_map':    f'El {c3_name} detecta incoherencias de tono y mensaje entre canales para que unifiques la comunicación de la marca con criterio medible.',
        'tens_map':   f'El {c3_name} localiza en qué momentos y por qué el equipo entra en modo crisis para que C4 actúe directamente en los detonantes.',
        'energy_m':   f'El {c3_name} mapea dónde y cuándo el equipo pierde motivación para que intervengas en los puntos exactos donde se pierde energía.',
        'comp_map':   f'El {c3_name} muestra qué hace cada persona vs qué podría hacer con su nivel real para que redistribuyas el trabajo sobre capacidad probada.',
        'climate_m':  f'El {c3_name} localiza dónde se concentran las tensiones y qué las alimenta para que intervengas en las fricciones exactas que sostienen el conflicto.',
        'journey_m':  f'El {c3_name} recorre la experiencia del cliente momento a momento para que identifiques exactamente dónde pierde confianza o percepción de valor.',
        'emotion_m':  f'El {c3_name} identifica las señales que anuncian desconexión del cliente para que actúes en caliente sobre la señal concreta.',
    }
    return t.get(c3_type, f'"{c3_name}" convierte lo que "{c2_name}" priorizó en comprensión específica para que C4 actúe sobre datos concretos.')

def expected_justi4(c4_type, c4_name, c3_name):
    t = {
        'kaizen':    f'El {c4_name} convierte cada mejora que {c3_name} reveló en un responsable, una acción y un plazo para que el cambio empiece hoy y C5 tenga algo concreto que verificar.',
        'redesign':  f'Con los datos que entregó {c3_name}, el {c4_name} convierte cada cambio en una decisión cuantificada para que ejecutes con certeza y trazabilidad.',
        'action_pl': f'El {c4_name} convierte lo que {c3_name} reveló en acciones con responsable y fecha para que cada hallazgo tenga un dueño y un plazo de ejecución.',
        'auth_red':  f'La {c4_name} asigna niveles de decisión claros sobre los solapamientos que {c3_name} reveló para que los cuellos de botella desaparezcan del proceso.',
        'def_tool':  f'La {c4_name} convierte la dirección que {c3_name} mostró en compromisos concretos con métricas, fechas y responsables para que el equipo ejecute con claridad.',
        'comm_arch': f'La {c4_name} construye el motor de demanda que {c3_name} mostró que faltaba para que la entrada de clientes sea predecible y sistemática.',
        'heijunka':  f'La {c4_name} redistribuye la carga que {c3_name} localizó de forma sostenida para que el trabajo fluya a ritmo constante.',
    }
    return t.get(c4_type, f'El {c4_name} ejecuta el cambio que {c3_name} hizo necesario para que el diagnóstico se convierta en transformación con dueño y fecha.')

def expected_justi6(kpi_impact, symptom_name):
    if kpi_impact:
        return f'Revisamos el KPI del C0 con los datos reales recogidos en C5. {kpi_impact}'
    return f'Revisamos el indicador principal del síntoma "{symptom_name}" para medir si el tratamiento produjo el cambio real que se esperaba.'

def get_type(name):
    if not name: return ('unknown','Sin clasificar','Herramienta no definida')
    n = name.strip()
    if n in TOOL_TAX: return TOOL_TAX[n]
    for k,v in TOOL_TAX.items():
        if k.lower() == n.lower(): return v
    return ('unknown', f'"{n}"', 'Herramienta no clasificada en taxonomía MASFRAME')

def opts_count(v):
    if isinstance(v, list): return len(v)
    if isinstance(v, str): return len([x for x in v.split(';') if x.strip()])
    return 0

def justi_quality(text):
    if not text: return 'missing'
    t = text.strip()
    if len(t) < 50: return 'too_short'
    if t.lower().startswith('porque necesitas') and len(t) < 80: return 'generic'
    return 'ok'

def analyze(s):
    sid = s['symptom_id']
    c2n = s.get('capa_2_decision','')
    c3n = s.get('capa_3_comprension','')
    c4n = s.get('capa_4_cambio','')
    c2t,c2lbl,c2desc = get_type(c2n)
    c3t,c3lbl,c3desc = get_type(c3n)
    c4t,c4lbl,c4desc = get_type(c4n)
    issues = []

    c1c = opts_count(s.get('capa_1_options',''))
    c2c = opts_count(s.get('capa_2_options',''))
    if c1c != 6: issues.append(('error','C1',f'C1 tiene {c1c} opciones — debe ser exactamente 6',None,None))
    if c2c != 6: issues.append(('error','C2',f'C2 tiene {c2c} opciones — debe ser exactamente 6',None,None))

    c2_opts_str = ' '.join(s.get('capa_2_options','') if isinstance(s.get('capa_2_options'), list) else [s.get('capa_2_options','')]).lower()
    if c2t == 'matrix_2x2' and 'urgente' in c2n.lower():
        is_urgency = any(w in c2_opts_str for w in ['urgente','importante','prioridad','bloquear tiempo','delegar'])
        is_pattern = any(w in c2_opts_str for w in ['patrón','escalado','desbordamiento','microgestión'])
        if is_pattern and not is_urgency:
            issues.append(('error','C2-name',
                f'El nombre "{c2n}" no coincide con las opciones: las opciones describen PATRONES ORGANIZACIONALES, no urgencia vs importancia.',
                'Herramienta sugerida: "Diagnóstico de Patrones de Tensión" o "Análisis de Detonantes"',
                'Con Urgente vs Importante el cliente ordenaría tareas. Pero las opciones de C2 le piden que identifique PATRONES de comportamiento — eso requiere otra herramienta.'))

    if c2t != 'unknown' and c3t != 'unknown':
        compat = COMPAT_C2_C3.get(c2t, [])
        if compat and c3t not in compat:
            if c2t == 'decision_tree' and c3t == 'cause_eff':
                fix_tool = 'Análisis de Portafolio de Rentabilidad'
                fix_reason = f'Después de elegir una dirección estratégica con "{c2n}", el cliente necesita VER LAS CONSECUENCIAS de esa elección — no buscar causas de problemas pasados.'
            else:
                fix_tool = f'Herramienta de tipo {COMPAT_C2_C3.get(c2t,["comprensión"])[0]}'
                fix_reason = f'Después de usar {c2lbl} en C2, el cliente necesita una herramienta de comprensión que trabaje SOBRE el resultado de esa decisión.'
            issues.append(('error','C2→C3', f'"{c3n}" ({c3lbl}) no fluye clínicamente de "{c2n}" ({c2lbl})', fix_tool, fix_reason))

    if c3t != 'unknown' and c4t != 'unknown':
        compat = COMPAT_C3_C4.get(c3t, [])
        if compat and c4t not in compat:
            issues.append(('warn','C3→C4',
                f'"{c4n}" ({c4lbl}) no continúa directamente de "{c3n}" ({c3lbl})',
                None,
                f'Después de {c3desc.lower()}, el cambio en C4 debería actuar directamente sobre lo que el cliente entendió.'))

    j2_q = justi_quality(s.get('justi_capa2',''))
    j3_q = justi_quality(s.get('justi_capa3',''))
    j4_q = justi_quality(s.get('justi_capa4',''))

    kpi_impact = s.get('kpi_impact','').lower()
    j6_actual = s.get('justi_capa6','').lower()
    kpi_keywords = ['margen','liquidez','cobro','rotación','retención','tensión','calidad','cumplimiento','experiencia','identidad','diferenciación','dependencia']
    kpi_word = next((w for w in kpi_keywords if w in kpi_impact), None)
    if kpi_word and j6_actual and kpi_word not in j6_actual:
        wrong_words = [w for w in kpi_keywords if w in j6_actual and w != kpi_word]
        if wrong_words:
            issues.append(('error','justi_capa6',
                f'justi_capa6 menciona "{wrong_words[0]}" pero el KPI mide "{kpi_word}". Posible texto copiado de otro síntoma.',
                expected_justi6(s.get('kpi_impact',''), s.get('symptom_name','')),
                f'El KPI de "{s.get("symptom_name")}" mide {kpi_word}. El justi_capa6 debe referenciar ese mismo indicador.'))

    if sid == 'OPE-S2':
        issues.append(('warn','C3→C4','C3="SIPOC de roles" → C4="Redistribución de autoridad" es idéntico a PSI-S2. Dos síntomas con el mismo tratamiento.',None,
            'OPE-S2 trata dependencia del líder; PSI-S2 trata perfiles mal ubicados. C4 debería diferenciarse hacia documentación y transferencia de conocimiento.'))
    if sid == 'RES-S3':
        c1_opts = s.get('capa_1_options','')
        if 'depende' in c1_opts.lower() and 'persona' in c1_opts.lower():
            issues.append(('warn','C1/justi','C1 mezcla contenido de OPE-S2 (dependencia de persona) con el foco real de RES-S3 (conflictos internos).',
                'Opciones de C1 deben centrarse en conflictos, tensiones silenciosas y ambiente envenenado — no en dependencia operativa.',
                'RES-S3 es "Inflamación Interna". Si C1 habla de "dependencia de una persona", el cliente lo confunde con OPE-S2.'))

    for layer, q, actual, exp_fn in [
        ('justi_capa2', j2_q, s.get('justi_capa2',''), lambda: expected_justi2(c2t, c2n, '')),
        ('justi_capa3', j3_q, s.get('justi_capa3',''), lambda: expected_justi3(c3t, c3n, c2n)),
        ('justi_capa4', j4_q, s.get('justi_capa4',''), lambda: expected_justi4(c4t, c4n, c3n)),
    ]:
        if q in ('too_short','generic'):
            issues.append(('warn', layer,
                f'"{actual}" — texto genérico ({len(actual.strip())} chars). No describe qué hace la herramienta ni por qué encaja aquí.',
                exp_fn(),
                f'El justi de {layer} debe explicar al CC qué hará el cliente CON esa herramienta y por qué en este momento del tratamiento.'))

    n_err = sum(1 for i in issues if i[0]=='error')
    n_warn = sum(1 for i in issues if i[0]=='warn')
    score = max(0, 100 - n_err*25 - n_warn*8)

    return {
        'issues': issues, 'score': score,
        'c2': (c2t,c2lbl,c2desc,c2n), 'c3': (c3t,c3lbl,c3desc,c3n), 'c4': (c4t,c4lbl,c4desc,c4n),
        'j2': (j2_q, s.get('justi_capa2','')), 'j3': (j3_q, s.get('justi_capa3','')),
        'j4': (j4_q, s.get('justi_capa4','')), 'j6': (justi_quality(s.get('justi_capa6','')), s.get('justi_capa6','')),
        'exp_j2': expected_justi2(c2t,c2n,''),
        'exp_j3': expected_justi3(c3t,c3n,c2n),
        'exp_j4': expected_justi4(c4t,c4n,c3n),
        'exp_j6': expected_justi6(s.get('kpi_impact',''), s.get('symptom_name','')),
    }

ANALYSES = {s['symptom_id']: analyze(s) for s in SYMS}

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace("'","&#39;")

syms_json = json.dumps(SYMS, ensure_ascii=False)
analyses_json = json.dumps(ANALYSES, ensure_ascii=False)

HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>MASFRAME — Auditor Clínico v4</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,-apple-system,sans-serif;background:#141312;color:#f0ede8;min-height:100vh}}
.topbar{{background:#0d0d0d;border-bottom:1px solid #222;padding:8px 16px;display:flex;align-items:center;gap:10px;position:sticky;top:0;z-index:100}}
.topbar h1{{font-size:13px;font-weight:700;color:#f0ede8;white-space:nowrap}}
select{{background:#1a1918;color:#f0ede8;border:1px solid #333;padding:5px 8px;border-radius:5px;font-size:12px;flex:1;min-width:0}}
.nbtn{{background:#222;color:#aaa;border:1px solid #333;padding:5px 10px;border-radius:5px;cursor:pointer;font-size:12px;white-space:nowrap}}
.nbtn:hover{{background:#2a2928;color:#fff}}
.prog{{height:2px;background:#0d0d0d;position:sticky;top:37px;z-index:99}}
.progfill{{height:100%;background:#4fc3f7;transition:width .3s}}
.main{{max-width:820px;margin:0 auto;padding:14px}}
.dash{{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:14px;padding:10px;background:#111;border-radius:8px;border:1px solid #1e1d1c}}
.dot{{width:10px;height:10px;border-radius:50%;background:#222;cursor:pointer;border:1px solid #2a2a2a;transition:transform .1s}}
.dot:hover{{transform:scale(1.4)}}
.dot.ok{{background:#4caf50;border-color:#4caf50}}.dot.warn{{background:#ff9800;border-color:#ff9800}}.dot.err{{background:#e53935;border-color:#e53935}}
.symhead{{margin-bottom:12px}}
.symid{{font-size:11px;color:#555;font-family:monospace}}
.symname{{font-size:20px;font-weight:700;margin:3px 0}}
.symlogica{{font-size:13px;color:#888;font-style:italic;margin-bottom:4px}}
.scorebar{{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding:10px 14px;background:#111;border-radius:8px;border:1px solid #1e1d1c}}
.score-num{{font-size:28px;font-weight:700;min-width:52px}}
.score-label{{font-size:12px;font-weight:600}}
.score-detail{{font-size:11px;color:#666;margin-left:auto}}
.issues{{margin-bottom:14px}}
.issue{{border-radius:6px;margin-bottom:6px;overflow:hidden}}
.issue-head{{display:flex;align-items:flex-start;gap:8px;padding:9px 12px;cursor:pointer}}
.issue-head:hover{{filter:brightness(1.1)}}
.issue.err .issue-head{{background:#2a1010;border-left:3px solid #e53935}}
.issue.warn .issue-head{{background:#251e0a;border-left:3px solid #ff9800}}
.issue-icon{{font-size:13px;flex-shrink:0;margin-top:1px}}
.issue-layer{{font-size:10px;color:#666;font-family:monospace;white-space:nowrap;margin-top:1px}}
.issue-desc{{font-size:12px;line-height:1.4;flex:1}}
.issue-chev{{color:#444;font-size:12px;flex-shrink:0;transition:transform .2s}}
.issue-chev.open{{transform:rotate(180deg)}}
.issue-body{{display:none;border-top:1px solid #1a1a1a}}
.issue.err .issue-body{{background:#200c0c}}.issue.warn .issue-body{{background:#1e1700}}
.issue-body.open{{display:block}}
.pair{{padding:10px 12px}}
.pair-row{{display:flex;gap:8px;margin-bottom:6px}}
.pair-col{{flex:1;border-radius:5px;padding:8px 10px;font-size:12px;line-height:1.5}}
.col-json{{background:#161616;border:1px solid #2a2a2a;color:#aaa}}
.col-exp{{background:#0d1a0d;border:1px solid #1e3a1e;color:#c8e6c9}}
.col-lbl{{font-size:10px;color:#555;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}}
.pair-btns{{display:flex;gap:5px;margin-top:6px}}
.pbtn{{padding:4px 10px;border-radius:4px;border:1px solid #333;background:#1a1a1a;color:#888;cursor:pointer;font-size:11px}}
.pbtn:hover{{background:#222;color:#ccc}}
.pbtn.acc{{background:#0d1a0d;border-color:#4caf50;color:#a5d6a7}}
.pbtn.rej{{background:#2a1010;border-color:#e53935;color:#ef9a9a}}
.pair-note{{width:100%;background:#131312;border:1px solid #222;color:#ccc;font-size:11px;padding:5px 7px;border-radius:4px;resize:vertical;min-height:44px;margin-top:5px;display:none}}
.pair-note.show{{display:block}}
.pair-note:focus{{outline:none;border-color:#4fc3f7}}
.reasoning{{font-size:11px;color:#666;line-height:1.4;border-top:1px solid #1a1a1a;padding:8px 12px;font-style:italic}}
.sec{{background:#1a1918;border-radius:7px;margin-bottom:7px;border:1px solid #222;overflow:hidden}}
.sec-head{{display:flex;align-items:center;gap:8px;padding:9px 12px;cursor:pointer}}
.sec-head:hover{{background:#1e1d1c}}
.stag{{font-size:10px;font-weight:700;padding:2px 7px;border-radius:3px;letter-spacing:.05em}}
.t0{{background:#0d47a1;color:#90caf9}}.t1{{background:#4a148c;color:#e1bee7}}
.t2{{background:#1b5e20;color:#c8e6c9}}.t3{{background:#4e342e;color:#ffccbc}}
.t4{{background:#bf360c;color:#fff}}.t5{{background:#37474f;color:#cfd8dc}}
.t6{{background:#880e4f;color:#f8bbd0}}
.sec-title{{font-size:13px;font-weight:600;flex:1}}
.sec-sub{{font-size:11px;color:#555}}
.schev{{color:#444;font-size:12px;transition:transform .18s}}
.schev.open{{transform:rotate(180deg)}}
.sbody{{padding:12px;border-top:1px solid #1e1d1c;display:none}}
.sbody.open{{display:block}}
.kinp{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px}}
.ig{{flex:1;min-width:160px}}
.ig label{{font-size:11px;color:#666;display:block;margin-bottom:3px}}
.ig input{{width:100%;background:#111;border:1px solid #2a2a2a;color:#f0ede8;padding:6px 8px;border-radius:4px;font-size:13px}}
.ig input:focus{{outline:none;border-color:#4fc3f7}}
.kbox{{background:#111;border-radius:5px;padding:9px 11px;display:flex;align-items:center;gap:12px}}
.knum{{font-size:28px;font-weight:700;line-height:1}}
.knum.good{{color:#4caf50}}.knum.bad{{color:#e53935}}.knum.neutral{{color:#ffc107}}
.ksub{{font-size:11px;color:#555}}.kdet{{font-size:11px}}
.khi{{font-size:11px;color:#777;margin-top:7px;line-height:1.5}}
.c1opts{{display:flex;flex-direction:column;gap:4px}}
.c1opt{{display:flex;align-items:flex-start;gap:7px;padding:6px 9px;border-radius:5px;cursor:pointer;border:1px solid transparent}}
.c1opt:hover{{background:#1e1d1c}}.c1opt.sel{{background:#0d1a0d;border-color:#4caf50}}
.c1opt input{{margin-top:2px;accent-color:#4caf50;flex-shrink:0}}
.c1opt span{{font-size:12px;line-height:1.4}}
.toolcard{{background:#111;border-radius:5px;padding:9px 11px;margin-bottom:6px}}
.tool-name{{font-size:12px;font-weight:600;color:#a5d6a7;margin-bottom:2px}}
.tool-comp{{font-size:11px;color:#555;margin-bottom:3px}}
.tool-role{{font-size:12px;color:#888;line-height:1.4}}
.c2opts{{display:flex;flex-direction:column;gap:4px;margin-top:8px}}
.c2opt{{padding:7px 9px;border-radius:4px;background:#0a120a;border:1px solid #1a2a1a;font-size:12px;line-height:1.4}}
.pstep{{padding:8px 10px;border-radius:4px;margin-bottom:4px;font-size:12px}}
.pstep.c3{{background:#110816;border-left:3px solid #7b1fa2}}
.pstep.c4{{background:#130e02;border-left:3px solid #f57f17}}
.pstep.c5{{background:#080e10;border-left:3px solid #37474f}}
.psl{{font-size:9px;color:#555;text-transform:uppercase;letter-spacing:.06em;margin-bottom:2px}}
.psn{{font-weight:600;margin-bottom:2px}}.psd{{color:#666}}
.verdict{{background:#0d0d0d;border-radius:7px;padding:12px;margin-top:10px;border:1px solid #1e1d1c}}
.vttl{{font-size:10px;color:#444;text-transform:uppercase;letter-spacing:.08em;margin-bottom:7px}}
.vq{{font-size:12px;color:#888;margin-bottom:7px;line-height:1.4}}
.vbtns{{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:7px}}
.vbtn{{padding:6px 12px;border-radius:4px;border:1px solid #2a2a2a;background:#1a1a1a;color:#777;cursor:pointer;font-size:12px;font-weight:500}}
.vbtn:hover{{background:#222;color:#ccc}}
.vbtn.v-ok{{background:#0d1a0d;border-color:#4caf50;color:#a5d6a7}}
.vbtn.v-warn{{background:#1e1700;border-color:#ff9800;color:#ffcc80}}
.vbtn.v-bad{{background:#200c0c;border-color:#e53935;color:#ef9a9a}}
.vnote{{width:100%;background:#111;border:1px solid #1e1d1c;color:#aaa;font-size:11px;padding:6px;border-radius:4px;resize:vertical;min-height:52px}}
.vnote:focus{{outline:none;border-color:#4fc3f7}}
.empty{{color:#444;font-size:11px;padding:6px 0}}
</style>
</head>
<body>
<div class="topbar">
  <h1>🏥 MASFRAME Auditor v4</h1>
  <select id="sel" onchange="loadSym(this.value)"></select>
  <button class="nbtn" onclick="prev()">←</button>
  <button class="nbtn" onclick="next()">→</button>
  <button class="nbtn" onclick="exportJSON()" style="background:#0d1a0d;color:#a5d6a7;border-color:#4caf50">⬇ Export JSON</button>
</div>
<div class="prog"><div class="progfill" id="prog"></div></div>
<div class="main">
  <div class="dash" id="dash"></div>
  <div id="sim"></div>
</div>
<script>
function esc(s){{return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');}}
const S={syms_json};
const AN={analyses_json};
let verdicts=JSON.parse(localStorage.getItem('mf_v4')||'{{}}');
let notes=JSON.parse(localStorage.getItem('mf_n4')||'{{}}');
let corrections=JSON.parse(localStorage.getItem('mf_c4')||'{{}}');
let cur=0;
function opts(v){{if(Array.isArray(v))return v;if(typeof v==='string')return v.split(';').map(x=>x.trim()).filter(Boolean);return[];}}
function calcKpi(f,a,b){{if(!a||!b||isNaN(+a)||isNaN(+b)||+b===0)return null;try{{return eval(f.replace(/InputA/g,+a).replace(/InputB/g,+b));}}catch{{return null;}}}}
function parseObj(o){{const m=(o||'').match(/([<>]=?)(\\d+\\.?\\d*)/);return m?{{op:m[1],val:parseFloat(m[2])}}:null;}}
function kpiSt(v,o){{const p=parseObj(o);if(v===null||!p)return'neutral';if(p.op==='>')return v>p.val?'good':'bad';if(p.op==='<')return v<p.val?'good':'bad';return'neutral';}}
function fmt(n){{return n===null?'—':Math.abs(n)>=100?Math.round(n).toLocaleString('es'):n.toFixed(1).replace('.',',');}}
function updKpi(sid,f,obj){{
  const a=document.getElementById('ia-'+sid)?.value;
  const b=document.getElementById('ib-'+sid)?.value;
  const v=calcKpi(f,a,b);const cl=kpiSt(v,obj);
  const ne=document.getElementById('kn-'+sid);const de=document.getElementById('kd-'+sid);
  if(ne){{ne.textContent=v!==null?fmt(v):'—';ne.className='knum '+cl;}}
  if(de){{de.textContent=cl==='good'?'✓ Objetivo alcanzado':cl==='bad'?'✗ Por debajo':'';de.style.color=cl==='good'?'#4caf50':'#e53935';}}
}}
function tog(id){{const b=document.getElementById('sb-'+id);const c=document.getElementById('sc-'+id);if(b&&c){{const o=b.classList.toggle('open');c.classList.toggle('open',o);}}}}
function togIssue(id){{const b=document.getElementById('ib-'+id);const c=document.getElementById('ic-'+id);if(b&&c){{const o=b.classList.toggle('open');c.classList.toggle('open',o);}}}}
function acceptFix(uid,sid,field,val){{
  if(!corrections[sid])corrections[sid]={{}};
  corrections[sid][field]={{accepted:true,value:val}};
  localStorage.setItem('mf_c4',JSON.stringify(corrections));
  const btn=document.getElementById('pacc-'+uid);const rej=document.getElementById('prej-'+uid);
  if(btn)btn.className='pbtn acc';if(rej)rej.className='pbtn';
}}
function rejectFix(uid,sid,field){{
  if(!corrections[sid])corrections[sid]={{}};
  corrections[sid][field]={{accepted:false}};
  localStorage.setItem('mf_c4',JSON.stringify(corrections));
  const btn=document.getElementById('pacc-'+uid);const rej=document.getElementById('prej-'+uid);
  if(btn)btn.className='pbtn';if(rej)rej.className='pbtn rej';
  const n=document.getElementById('pn-'+uid);if(n)n.classList.add('show');
}}
function saveVerdict(sid,v){{
  verdicts[sid]=v;localStorage.setItem('mf_v4',JSON.stringify(verdicts));
  renderDash();
  ['ok','warn','bad'].forEach(x=>{{const b=document.getElementById('vb-'+x);if(b)b.className='vbtn'+(v===x?' v-'+x:'');
  }});
}}
function saveVerdNote(sid){{notes[sid]=document.getElementById('vn-'+sid)?.value||'';localStorage.setItem('mf_n4',JSON.stringify(notes));}}
function scoreColor(sc){{return sc>=85?'#4caf50':sc>=60?'#ff9800':'#e53935';}}
function renderSym(){{
  const s=S[cur];const sid=s.symptom_id;const an=AN[sid]||{{}};
  const issues=an.issues||[];const score=an.score??100;
  const verd=verdicts[sid]||'';const note=notes[sid]||'';
  const c1=opts(s.capa_1_options);const c2=opts(s.capa_2_options);
  const nErr=issues.filter(i=>i[0]==='error').length;const nWarn=issues.filter(i=>i[0]==='warn').length;
  const scolor=scoreColor(score);
  let h=`<div class="symhead">
    <div class="symid">${{sid}} · ${{s.specialty_id||''}}</div>
    <div class="symname">${{esc(s.symptom_name||'')}}</div>
    <div class="symlogica">"${{esc(s.logica||'')}}"</div>
  </div>
  <div class="scorebar">
    <div class="score-num" style="color:${{scolor}}">${{score}}</div>
    <div><div class="score-label" style="color:${{scolor}}">${{score>=85?'Sin problemas detectados':score>=60?'Revisar':'Corrección necesaria'}}</div>
    <div style="font-size:11px;color:#555;margin-top:2px">${{nErr}} error${{nErr!==1?'es':''}} · ${{nWarn}} aviso${{nWarn!==1?'s':''}}</div></div>
    <div class="score-detail">C2: ${{esc(an.c2?an.c2[1]:'—')}} → C3: ${{esc(an.c3?an.c3[1]:'—')}} → C4: ${{esc(an.c4?an.c4[1]:'—')}}</div>
  </div>`;
  if(issues.length>0){{
    h+='<div class="issues">';
    issues.forEach((iss,i)=>{{
      const uid=`${{sid}}-iss-${{i}}`;
      const lvl=iss[0],layer=iss[1],desc=iss[2],fix=iss[3],reason=iss[4];
      const hasFix=fix&&fix.length>0;
      h+=`<div class="issue ${{lvl==='error'?'err':'warn'}}">
        <div class="issue-head" onclick="togIssue('${{uid}}')">
          <span class="issue-icon">${{lvl==='error'?'🔴':'⚠️'}}</span>
          <span class="issue-layer">[${{esc(layer)}}]</span>
          <span class="issue-desc">${{esc(desc)}}</span>
          <span class="issue-chev" id="ic-${{uid}}">▾</span>
        </div>
        <div class="issue-body" id="ib-${{uid}}">`;
      if(hasFix){{
        const cs=corrections[sid]?corrections[sid][layer]:null;
        const isAcc=cs?.accepted===true;const isRej=cs?.accepted===false;
        h+=`<div class="pair"><div class="pair-row">
          <div class="pair-col col-json"><div class="col-lbl">📋 JSON actual</div>${{esc(desc)}}</div>
          <div class="pair-col col-exp"><div class="col-lbl">🎯 Motor sugiere</div>${{esc(fix)}}</div>
          </div>
          <div class="pair-btns">
            <button id="pacc-${{uid}}" class="pbtn${{isAcc?' acc':''}}" onclick="acceptFix('${{uid}}','${{sid}}','${{esc(layer)}}','${{esc(fix)}}')">✅ Aceptar</button>
            <button id="prej-${{uid}}" class="pbtn${{isRej?' rej':''}}" onclick="rejectFix('${{uid}}','${{sid}}','${{esc(layer)}}')">🔴 Anotar corrección</button>
          </div>
          <textarea class="pair-note${{isRej?' show':''}}" id="pn-${{uid}}" placeholder="¿Cuál sería la corrección?">${{cs?.note||''}}</textarea>
        </div>`;
      }}
      if(reason)h+=`<div class="reasoning">${{esc(reason)}}</div>`;
      h+='</div></div>';
    }});
    h+='</div>';
  }} else {{
    h+=`<div style="background:#0d1a0d;border:1px solid #1e3a1e;border-radius:6px;padding:9px 12px;font-size:12px;color:#a5d6a7;margin-bottom:12px">✅ Sin problemas detectados automáticamente</div>`;
  }}
  const kv=s.specialty_id==='UCI FINANCIERA'?['800','2100']:s.specialty_id==='UNIDAD DE PROCESOS'?['8','40']:
            s.specialty_id==='CARDIOLOGIA COMERCIAL'?['3','12']:s.specialty_id==='NEUROLOGIA ESTRATEGICA'?['6500','12000']:
            s.specialty_id==='GESTION CLINICA'?['4200','6000']:s.specialty_id==='CIRUGIA DE MARCA'?['3','8']:
            s.specialty_id==='PSIQUIATRIA ORGANIZACIONAL'?['6','22']:s.specialty_id==='RESCATE DE PERSONAS'?['2','14']:
            s.specialty_id==='TERAPIA DE EXPERIENCIA'?['4','65']:['1','12'];
  h+=`<div class="sec"><div class="sec-head" onclick="tog('c0-${{sid}}')">
    <span class="stag t0">C0</span><span class="sec-title">KPI — Diagnóstico</span>
    <span class="sec-sub">${{esc(s.kpi_formula||'')}}&nbsp;·&nbsp;Obj ${{esc(s.kpi_objective||'')}}</span>
    <span class="schev open" id="sc-c0-${{sid}}">▾</span></div>
  <div class="sbody open" id="sb-c0-${{sid}}">
    <p style="font-size:11px;color:#777;margin-bottom:7px">${{esc(s.kpi_question||'')}}</p>
    <div class="kinp">
      <div class="ig"><label>${{esc(s.input_a||'A')}}</label><input id="ia-${{sid}}" type="number" value="${{kv[0]}}" oninput="updKpi('${{sid}}','${{esc(s.kpi_formula)}}','${{esc(s.kpi_objective)}}')"></div>
      <div class="ig"><label>${{esc(s.input_b||'B')}}</label><input id="ib-${{sid}}" type="number" value="${{kv[1]}}" oninput="updKpi('${{sid}}','${{esc(s.kpi_formula)}}','${{esc(s.kpi_objective)}}')"></div>
    </div>
    <div class="kbox"><div><div class="knum neutral" id="kn-${{sid}}">—</div><div class="ksub">Objetivo: ${{esc(s.kpi_objective||'—')}}</div></div>
    <div id="kd-${{sid}}" class="kdet"></div></div>
    <div class="khi">${{esc(s.kpi_impact||'')}}</div>
    <div style="margin-top:8px;padding:6px 8px;background:#1a1a1a;border-radius:4px;font-size:11px;color:#666">
      <strong style="color:#888">Caso clínico JSON:</strong> ${{esc(s.example||s.description_symptom||'—')}}</div>
  </div></div>`;
  const c1html=c1.map((o,i)=>`<label class="c1opt"><input type="checkbox" onchange="this.closest('.c1opt').classList.toggle('sel',this.checked)"><span>${{esc(o)}}</span></label>`).join('')||'<p class="empty">Sin opciones</p>';
  h+=`<div class="sec"><div class="sec-head" onclick="tog('c1-${{sid}}')">
    <span class="stag t1">C1</span><span class="sec-title">Priorización</span>
    <span class="sec-sub">${{c1.length}}/6</span><span class="schev" id="sc-c1-${{sid}}">▾</span>
  </div><div class="sbody" id="sb-c1-${{sid}}"><div class="c1opts">${{c1html}}</div></div></div>`;
  const c2html=c2.map(o=>`<div class="c2opt">${{esc(o)}}</div>`).join('')||'<p class="empty">Sin opciones</p>';
  h+=`<div class="sec"><div class="sec-head" onclick="tog('c2-${{sid}}')">
    <span class="stag t2">C2</span><span class="sec-title">${{esc(s.capa_2_decision||'—')}}</span>
    <span class="sec-sub">${{c2.length}}/6</span><span class="schev" id="sc-c2-${{sid}}">▾</span>
  </div><div class="sbody" id="sb-c2-${{sid}}">
    <div class="toolcard"><div class="tool-name">${{esc(an.c2?an.c2[1]:'—')}}</div>
    <div class="tool-comp">Tipo: ${{esc(an.c2?an.c2[0]:'—')}}</div><div class="tool-role">${{esc(an.c2?an.c2[2]:'—')}}</div></div>
    <div style="font-size:11px;color:#666;margin-bottom:6px">
      <strong style="color:#777">justi_capa2 actual:</strong> ${{esc(s.justi_capa2||'—')}}<br>
      <strong style="color:#4caf50">Motor espera:</strong> ${{esc(an.exp_j2||'—')}}</div>
    <div class="c2opts">${{c2html}}</div>
  </div></div>`;
  h+=`<div class="sec"><div class="sec-head" onclick="tog('c35-${{sid}}')">
    <span class="stag t3">C3→C5</span><span class="sec-title">El Camino</span>
    <span class="schev" id="sc-c35-${{sid}}">▾</span>
  </div><div class="sbody" id="sb-c35-${{sid}}">
    <div class="toolcard" style="margin-bottom:8px">
      <div class="tool-name">C3: ${{esc(s.capa_3_comprension||'—')}}</div>
      <div class="tool-comp">Tipo: ${{esc(an.c3?an.c3[0]:'—')}} · ${{esc(an.c3?an.c3[1]:'—')}}</div>
      <div class="tool-role">${{esc(an.c3?an.c3[2]:'—')}}</div></div>
    <div style="font-size:11px;color:#666;margin-bottom:8px">
      <strong style="color:#777">justi_capa3 actual:</strong> ${{esc(s.justi_capa3||'—')}}<br>
      <strong style="color:#4caf50">Motor espera:</strong> ${{esc(an.exp_j3||'—')}}</div>
    <div class="pstep c3"><div class="psl">C3 — Comprensión</div><div class="psn">${{esc(s.capa_3_comprension||'—')}}</div><div class="psd">${{esc(s.justi_capa3||'')}}</div></div>
    <div style="font-size:11px;color:#666;margin:8px 0">
      <strong style="color:#777">justi_capa4 actual:</strong> ${{esc(s.justi_capa4||'—')}}<br>
      <strong style="color:#4caf50">Motor espera:</strong> ${{esc(an.exp_j4||'—')}}</div>
    <div class="pstep c4"><div class="psl">C4 — Cambio</div><div class="psn">${{esc(s.capa_4_cambio||'—')}}</div><div class="psd">${{esc(s.justi_capa4||'')}}</div></div>
    <div class="pstep c5"><div class="psl">C5 — Ejecución</div><div class="psn">${{esc(s.capa_5_ejecucion||'—')}}</div><div class="psd">${{esc(s.justi_capa5||'')}}</div></div>
    <div style="font-size:11px;color:#666;margin-top:8px">
      <strong style="color:#777">justi_capa6 actual:</strong> ${{esc(s.justi_capa6||'—')}}<br>
      <strong style="color:#4caf50">Motor espera:</strong> ${{esc(an.exp_j6||'—')}}</div>
  </div></div>`;
  h+=`<div class="verdict"><div class="vttl">Veredicto de consultoría</div>
    <div class="vq">¿Este síntoma es comercialmente viable (399–1.500€) y clínicamente coherente?</div>
    <div class="vbtns">
      <button id="vb-ok" class="vbtn${{verd==='ok'?' v-ok':''}}" onclick="saveVerdict('${{sid}}','ok')">✅ Aprobado</button>
      <button id="vb-warn" class="vbtn${{verd==='warn'?' v-warn':''}}" onclick="saveVerdict('${{sid}}','warn')">⚠️ Ajuste menor</button>
      <button id="vb-bad" class="vbtn${{verd==='bad'?' v-bad':''}}" onclick="saveVerdict('${{sid}}','bad')">🔴 Corrección necesaria</button>
    </div>
    <textarea class="vnote" id="vn-${{sid}}" placeholder="Notas..." oninput="saveVerdNote('${{sid}}')">${{esc(note)}}</textarea>
  </div>`;
  document.getElementById('sim').innerHTML=h;
  setTimeout(()=>updKpi(sid,s.kpi_formula,s.kpi_objective),40);
}}
function renderDash(){{
  document.getElementById('dash').innerHTML=S.map((s,i)=>{{
    const an=AN[s.symptom_id]||{{}};const sc=an.score??100;const v=verdicts[s.symptom_id]||'';
    const cls=v?('ok warn err'.split(' ')[['ok','warn','bad'].indexOf(v)]||''):sc>=85?'ok':sc>=60?'warn':'err';
    return `<div class="dot ${{cls}}" title="${{esc(s.symptom_id)}}: ${{esc(s.symptom_name)}} (${{sc}})" onclick="cur=${{i}};renderSym();updSel();updProg()"></div>`;
  }}).join('');
}}
function loadSym(id){{cur=S.findIndex(s=>s.symptom_id===id);if(cur<0)cur=0;renderSym();updProg();window.scrollTo(0,0);}}
function updSel(){{document.getElementById('sel').value=S[cur].symptom_id;}}
function updProg(){{document.getElementById('prog').style.width=(((cur+1)/S.length)*100)+'%';}}
function prev(){{if(cur>0){{cur--;renderSym();updSel();updProg();window.scrollTo(0,0);}}}}
function next(){{if(cur<S.length-1){{cur++;renderSym();updSel();updProg();window.scrollTo(0,0);}}}}
function exportJSON(){{
  const out=JSON.parse(JSON.stringify(S));let count=0;
  out.forEach(s=>{{const c=corrections[s.symptom_id];if(!c)return;
    Object.entries(c).forEach(([field,data])=>{{
      if(data.accepted&&data.value){{
        if(field==='C2→C3')s.capa_3_comprension=data.value;
        else if(field==='justi_capa2')s.justi_capa2=data.value;
        else if(field==='justi_capa3')s.justi_capa3=data.value;
        else if(field==='justi_capa4')s.justi_capa4=data.value;
        else if(field==='justi_capa6')s.justi_capa6=data.value;
        count++;
      }}
    }});
  }});
  const blob=new Blob([JSON.stringify(out,null,2)],{{type:'application/json'}});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='symptoms_corrected.json';a.click();
  alert(`Exportado con ${{count}} corrección${{count!==1?'es':''}} aplicada${{count!==1?'s':''}}.`);
}}
function init(){{
  const sel=document.getElementById('sel');
  S.forEach(s=>{{const o=document.createElement('option');o.value=s.symptom_id;o.textContent=s.symptom_id+' — '+s.symptom_name;sel.appendChild(o);}});
  renderDash();loadSym(S[0].symptom_id);
}}
init();
</script>
</body></html>"""

OUT = r'C:\Users\Masesora\Documents\Claude\Projects\Masesora\simulador_masframe.html'
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f"OK — {len(HTML.encode('utf-8'))//1024} KB → {OUT}")
