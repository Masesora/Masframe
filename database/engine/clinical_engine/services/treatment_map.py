# masesora_backend/database/engine/clinical_engine/services/treatment_map.py

TREATMENT_MAP = {
    # ---------------------------------------------------------
    # UCI FINANCIERA — S1
    # ---------------------------------------------------------
    "UCI-S1": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato. "
                "No solo estabiliza la caja: opera como un quirófano financiero, reduciendo gastos innecesarios, "
                "optimizando procesos ocultos y potenciando los productos estrella que sostienen la rentabilidad. "
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir "
                "crisis y crecer con confianza. RESUELVE: - Gasto fijo desproporcionado que ahoga la caja "
                "- Productos que consumen recursos sin retorno - Márgenes invisibles por falta de análisis "
                "- Caja débil y sin colchón - Dependencia excesiva de pocos clientes - Falta de foco en lo que realmente funciona"
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 1,
            "department": "FINANZAS",
            "plan": "PIE",
            "code": "UCI-S1",
            "logic": (
                "Resistencia de Caja: Saber con precisión cuántos días puede el negocio mantener la actividad "
                "si mañana dejan de entrar ingresos, sin decisiones de urgencia."
            ),
        },
        "treatment": {
            "decision": "Priorización de Pagos",
            "decision_explanation": (
                "Determinar qué pagos sostienen la supervivencia y cuáles pueden esperar sin comprometer el negocio."
            ),
            "action": "Ordenar pagos y activar cobro inmediato",
            "action_explanation": "Evita decisiones emocionales y frena la salida de caja innecesaria.",
            "tool": "Matriz de Tesorería",
            "tool_explanation": (
                "Visualiza entradas y salidas para decidir con datos y no con urgencia."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno Absoluto de Caja",
            "decision_explanation": (
                "La caja deja de ser consecuencia y pasa a ser objeto de control consciente."
            ),
            "action": "Diseñar un mapa de caja anticipativo",
            "action_explanation": "Permite decidir antes de que el problema exista.",
            "tool": "Radar de Liquidez 90D",
            "tool_explanation": "Anticipa escenarios y elimina decisiones reactivas.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S2
    # ---------------------------------------------------------
    "UCI-S2": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato. "
                "No solo estabiliza la caja: opera como un quirófano financiero, reduciendo gastos innecesarios, "
                "optimizando procesos ocultos y potenciando los productos estrella que sostienen la rentabilidad."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 2,
            "department": "FINANZAS",
            "plan": "PIE",
            "code": "UCI-S2",
            "logic": (
                "Salud del Margen: Comprobar si, tras cubrir el coste real de lo que vendes, "
                "queda margen suficiente para sostener la estructura y generar beneficio."
            ),
        },
        "treatment": {
            "decision": "Saneamiento de Cartera",
            "decision_explanation": (
                "Identificar clientes y productos que erosionan la rentabilidad global."
            ),
            "action": "Recalcular costes y ajustar precios o mix",
            "action_explanation": "Recupera margen sin aumentar volumen ni estructura.",
            "tool": "Análisis Pareto 80/20",
            "tool_explanation": "Enfoca el esfuerzo donde realmente se genera el beneficio.",
        },
        "master_treatment": {
            "decision": "Arquitectura de Margen",
            "decision_explanation": "El margen se diseña, no se sufre.",
            "action": "Reconstruir precios desde valor capturado",
            "action_explanation": "Desvincula precio de coste y lo vincula a valor.",
            "tool": "Escandallo Estratégico",
            "tool_explanation": "Define el margen objetivo por diseño.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S3
    # ---------------------------------------------------------
    "UCI-S3": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 3,
            "department": "FINANZAS",
            "plan": "PIE",
            "code": "UCI-S3",
            "logic": (
                "Dinero Invisible: Identificar cuánto dinero ya ganado sigue fuera de la cuenta "
                "por no cerrar correctamente el ciclo de facturación y cobro."
            ),
        },
        "treatment": {
            "decision": "Aceleración de Ciclo",
            "decision_explanation": (
                "Reducir el tiempo entre venta, facturación y cobro."
            ),
            "action": "Facturar por hitos y adelantar cobros",
            "action_explanation": "Convierte ventas en liquidez real.",
            "tool": "Ciclo de Caja",
            "tool_explanation": (
                "Mide el tiempo que el dinero tarda en llegar a caja."
            ),
        },
        "master_treatment": {
            "decision": "Dominio del Ciclo de Ingresos",
            "decision_explanation": "La facturación se convierte en palanca financiera.",
            "action": "Convertir la facturación en financiación",
            "action_explanation": "El cliente financia parte del crecimiento.",
            "tool": "Ingeniería Order-to-Cash",
            "tool_explanation": "Rediseña el flujo completo venta-cobro.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S4
    # ---------------------------------------------------------
    "UCI-S4": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 4,
            "department": "FINANZAS",
            "plan": "PRE",
            "code": "UCI-S4",
            "logic": (
                "Velocidad de Cobro: Medir el tiempo real que tarda el dinero en llegar a caja "
                "desde que se realiza la venta y su impacto en la liquidez diaria."
            ),
        },
        "treatment": {
            "decision": "Filtro de Calidad de Clientes",
            "decision_explanation": (
                "Proteger la caja priorizando clientes sanos y recurrentes."
            ),
            "action": "Clasificar clientes por riesgo y valor",
            "action_explanation": "Reduce impagos y dependencia de malos clientes.",
            "tool": "Regla 5/25",
            "tool_explanation": (
                "Permite decidir a quién servir, cómo y en qué condiciones."
            ),
        },
        "master_treatment": {
            "decision": "Selección de Clientes",
            "decision_explanation": "No todos los clientes merecen caja.",
            "action": "Blindar la caja eliminando dependencia",
            "action_explanation": "Reduce riesgo sistémico del negocio.",
            "tool": "Ranking de Clientes por Poder de Caja",
            "tool_explanation": "Prioriza clientes que fortalecen la empresa.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S5
    # ---------------------------------------------------------
    "UCI-S5": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 5,
            "department": "FINANZAS",
            "plan": "PRE",
            "code": "UCI-S5",
            "logic": (
                "Almacén Dinámico: Detectar si el stock está trabajando para el negocio "
                "o si hay dinero inmovilizado en productos que no rotan."
            ),
        },
        "treatment": {
            "decision": "Liquidación de Activos",
            "decision_explanation": (
                "Liberar dinero atrapado en inventario improductivo."
            ),
            "action": "Identificar y liquidar stock sin rotación",
            "action_explanation": "Recupera liquidez sin endeudarse.",
            "tool": "Matriz ABC de Stock",
            "tool_explanation": "Diferencia lo crítico de lo prescindible.",
        },
        "master_treatment": {
            "decision": "Activación de Capital",
            "decision_explanation": "El stock debe trabajar o salir.",
            "action": "Transformar stock dormido en liquidez",
            "action_explanation": "Convierte pasivo oculto en activo estratégico.",
            "tool": "Tablero de Rotación Viva",
            "tool_explanation": "Mide vida y utilidad real del inventario.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S6
    # ---------------------------------------------------------
    "UCI-S6": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 6,
            "department": "FINANZAS",
            "plan": "PRE",
            "code": "UCI-S6",
            "logic": (
                "Oxígeno Financiero: Evaluar hasta qué punto los proveedores están financiando la operativa diaria "
                "reduciendo la presión de caja."
            ),
        },
        "treatment": {
            "decision": "Apalancamiento Operativo",
            "decision_explanation": (
                "Usar a los proveedores como fuente de financiación operativa."
            ),
            "action": "Renegociar plazos y centralizar compras",
            "action_explanation": "Reduce presión de caja diaria.",
            "tool": "Cuadro de Negociación DPO",
            "tool_explanation": "Permite ganar días de pago de forma estructurada.",
        },
        "master_treatment": {
            "decision": "Control de la Cadena",
            "decision_explanation": (
                "La cadena de suministro es un juego de poder."
            ),
            "action": "Convertir proveedores en financiadores",
            "action_explanation": "Traslada tensión financiera fuera.",
            "tool": "Mapa de Poder de Proveedores",
            "tool_explanation": (
                "Visualiza dependencia y capacidad de negociación."
            ),
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S7
    # ---------------------------------------------------------
    "UCI-S7": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 7,
            "department": "FINANZAS",
            "plan": "PRE",
            "code": "UCI-S7",
            "logic": (
                "Libertad de Deuda: Analizar si el beneficio generado es suficiente para absorber la deuda financiera "
                "sin comprometer la estabilidad del negocio."
            ),
        },
        "treatment": {
            "decision": "Reestructuración de Pasivo",
            "decision_explanation": (
                "Evitar que la deuda asfixie la operativa."
            ),
            "action": "Reordenar vencimientos y reducir coste financiero",
            "action_explanation": "Devuelve oxígeno al flujo de caja.",
            "tool": "Dossier Bancario",
            "tool_explanation": "Presenta el negocio de forma financiable.",
        },
        "master_treatment": {
            "decision": "Soberanía Financiera",
            "decision_explanation": (
                "La deuda debe servir al negocio, no dominarlo."
            ),
            "action": "Rediseñar la deuda como palanca",
            "action_explanation": "Recupera control estratégico.",
            "tool": "Arquitectura de Pasivo",
            "tool_explanation": "Ordena deuda según propósito y retorno.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S8
    # ---------------------------------------------------------
    "UCI-S8": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 8,
            "department": "FINANZAS",
            "plan": "PRE",
            "code": "UCI-S8",
            "logic": (
                "Rentabilidad del Esfuerzo: Distinguir qué productos o servicios multiplican el valor del negocio "
                "y cuáles consumen recursos sin retorno proporcional."
            ),
        },
        "treatment": {
            "decision": "Purga de Portafolio",
            "decision_explanation": (
                "Eliminar productos que consumen recursos sin retorno."
            ),
            "action": "Suprimir líneas con margen insuficiente",
            "action_explanation": "Simplifica y mejora la rentabilidad global.",
            "tool": "Matriz Margen / Esfuerzo",
            "tool_explanation": (
                "Mide valor generado frente a esfuerzo requerido."
            ),
        },
        "master_treatment": {
            "decision": "Diseño de Portafolio",
            "decision_explanation": "El negocio se concentra donde domina.",
            "action": "Focalizar en líneas multiplicadoras",
            "action_explanation": "Aumenta valor sin complejidad.",
            "tool": "Mapa de Dominancia de Oferta",
            "tool_explanation": "Identifica dónde se gana de verdad.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S9
    # ---------------------------------------------------------
    "UCI-S9": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 9,
            "department": "FINANZAS",
            "plan": "PRE",
            "code": "UCI-S9",
            "logic": (
                "Cierre de Fugas: Localizar desviaciones recurrentes entre lo planificado y lo ejecutado "
                "que erosionan el resultado sin aportar valor."
            ),
        },
        "treatment": {
            "decision": "Ablación de Estructura",
            "decision_explanation": (
                "Reducir peso estructural que no aporta valor."
            ),
            "action": "Eliminar gastos sin ROI directo",
            "action_explanation": "Mejora margen sin crecer ventas.",
            "tool": "Presupuesto Cero",
            "tool_explanation": "Justifica cada gasto desde cero.",
        },
        "master_treatment": {
            "decision": "Ingeniería de Estructura",
            "decision_explanation": (
                "La estructura debe escalar sin peso muerto."
            ),
            "action": "Rediseñar estructura hacia lo variable",
            "action_explanation": "Permite crecer sin perder rentabilidad.",
            "tool": "Estructura Variable Objetivo",
            "tool_explanation": "Ajusta costes al ritmo del negocio.",
        },
    },

    # ---------------------------------------------------------
    # UCI FINANCIERA — S10
    # ---------------------------------------------------------
    "UCI-S10": {
        "meta": {
            "specialty": "UCI FINANCIERA",
            "description": (
                "Es la unidad que entra en acción cuando la empresa necesita un rescate financiero inmediato."
            ),
            "strategic_objective": (
                "Transformar la estructura financiera en un sistema ligero, rentable y antifrágil, capaz de resistir crisis y crecer con confianza."
            ),
            "order": 10,
            "department": "FINANZAS",
            "plan": "PRE",
            "code": "UCI-S10",
            "logic": (
                "Colchón de Seguridad: Calcular la capacidad real del negocio para absorber imprevistos "
                "y tomar decisiones desde la calma y no desde la urgencia."
            ),
        },
        "treatment": {
            "decision": "Blindaje del Beneficio",
            "decision_explanation": (
                "Asegurar un nivel mínimo de beneficio sostenible."
            ),
            "action": "Garantizar ≥15% de beneficio neto por venta",
            "action_explanation": "Permite decidir desde la calma.",
            "tool": "Escandallo de Oro S10",
            "tool_explanation": "Define el beneficio real mínimo aceptable.",
        },
        "master_treatment": {
            "decision": "Supervisión Estratégica",
            "decision_explanation": (
                "Monitorear resultados de forma integral para evitar sorpresas."
            ),
            "action": "Revisar semanalmente desviaciones de caja y margen",
            "action_explanation": "Detecta riesgos antes de que afecten a la operativa.",
            "tool": "Tablero de Indicadores Clave",
            "tool_explanation": (
                "Consolida datos clave de caja y margen para decisiones rápidas."
            ),
        },
    },
    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S1
    # ---------------------------------------------------------
    "UNI-S1": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía. "
                "Establece estándares simples, elimina desperdicios y crea flujo real de valor. "
                "No se toleran 'costumbres' sin ROI: cada paso debe justificar su existencia."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 11,
            "department": "PROCESOS",
            "plan": "PIE",
            "code": "UNI-S1",
            "logic": (
                "Proceso Comercial Fluido: Saber si una oportunidad se convierte en pedido "
                "sin fricción ni pérdida innecesaria."
            ),
        },
        "treatment": {
            "decision": "Mapeo de Tiempos Muertos",
            "decision_explanation": (
                "Identificar dónde se pierde tiempo entre pasos sin aportar valor."
            ),
            "action": "Cronometrar tiempos reales entre puestos",
            "action_explanation": (
                "Hace visibles las esperas ocultas que encarecen el proceso."
            ),
            "tool": "Diagrama de Flujo de Valor",
            "tool_explanation": (
                "Representa gráficamente el tiempo útil vs. el desperdicio."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno del Flujo",
            "decision_explanation": (
                "El flujo se gobierna, no se observa pasivamente."
            ),
            "action": "Diseñar un sistema sin esperas estructurales",
            "action_explanation": (
                "Convierte tiempo en capacidad productiva."
            ),
            "tool": "Radar de Flujo Operativo",
            "tool_explanation": (
                "Visualiza bloqueos y fricciones del sistema."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S2
    # ---------------------------------------------------------
    "UNI-S2": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía. "
                "Establece estándares simples, elimina desperdicios y crea flujo real de valor."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 12,
            "department": "PROCESOS",
            "plan": "PIE",
            "code": "UNI-S2",
            "logic": (
                "Arranque del Pedido: Medir si el pedido entra bien definido "
                "o genera aclaraciones y retrasos posteriores."
            ),
        },
        "treatment": {
            "decision": "Priorización de Valor",
            "decision_explanation": (
                "Enfocar la capacidad limitada en tareas que generan resultado."
            ),
            "action": "Eliminar tareas 'ruido' y proteger tiempo crítico",
            "action_explanation": (
                "Reduce saturación directiva y desbloquea el flujo."
            ),
            "tool": "Regla 5/25 de Tareas + Planificador",
            "tool_explanation": (
                "Clasifica tareas por impacto y urgencia real."
            ),
        },
        "master_treatment": {
            "decision": "Dominio de la Capacidad",
            "decision_explanation": (
                "La agenda refleja el poder real del negocio."
            ),
            "action": "Rediseñar prioridades según impacto sistémico",
            "action_explanation": (
                "Libera capacidad estratégica."
            ),
            "tool": "Mapa de Capacidad Crítica",
            "tool_explanation": (
                "Identifica cuellos que limitan todo el sistema."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S3
    # ---------------------------------------------------------
    "UNI-S3": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 13,
            "department": "PROCESOS",
            "plan": "PIE",
            "code": "UNI-S3",
            "logic": (
                "Cumplimiento del Proceso: Saber si la empresa cumple lo que promete "
                "de forma sistemática."
            ),
        },
        "treatment": {
            "decision": "Estandarización Crítica",
            "decision_explanation": (
                "Evitar errores repetidos por falta de criterios claros."
            ),
            "action": "Documentar fallos recurrentes y crear checklist de entrega",
            "action_explanation": (
                "Reduce reprocesos y errores evitables."
            ),
            "tool": "Checklist de Calidad / Handoff",
            "tool_explanation": (
                "Asegura continuidad y calidad entre áreas."
            ),
        },
        "master_treatment": {
            "decision": "Diseño de la Ejecución",
            "decision_explanation": (
                "La calidad se diseña, no se inspecciona."
            ),
            "action": "Crear estándares de salida innegociables",
            "action_explanation": (
                "Elimina errores antes de producirse."
            ),
            "tool": "Arquitectura de Checkpoints",
            "tool_explanation": (
                "Integra calidad en el proceso."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S4
    # ---------------------------------------------------------
    "UNI-S4": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 14,
            "department": "PROCESOS",
            "plan": "PRE",
            "code": "UNI-S4",
            "logic": (
                "Calidad Integrada: Medir si el proceso produce bien a la primera "
                "o necesita correcciones."
            ),
        },
        "treatment": {
            "decision": "Eliminación de Desperdicio",
            "decision_explanation": (
                "Suprimir pasos que no generan valor para el cliente."
            ),
            "action": "Eliminar actividades sin impacto directo",
            "action_explanation": (
                "Reduce costes invisibles y acelera entregas."
            ),
            "tool": "Auditoría de Desperdicios (LEAN)",
            "tool_explanation": (
                "Identifica desperdicio en tiempo, movimiento y espera."
            ),
        },
        "master_treatment": {
            "decision": "Optimización del Flujo de Valor",
            "decision_explanation": (
                "Cada paso debe justificar su existencia."
            ),
            "action": "Eliminar pasos sin retorno económico",
            "action_explanation": (
                "Maximiza valor por unidad de tiempo."
            ),
            "tool": "Mapa de Valor Vivo",
            "tool_explanation": (
                "Relaciona tiempo, coste y valor."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S5
    # ---------------------------------------------------------
    "UNI-S5": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 15,
            "department": "PROCESOS",
            "plan": "PRE",
            "code": "UNI-S5",
            "logic": (
                "Gestión de Incidencias: Evaluar si los errores se cierran rápido "
                "o se enquistan."
            ),
        },
        "treatment": {
            "decision": "Actualización de Técnica",
            "decision_explanation": (
                "Evitar que el 'siempre se hizo así' frene la mejora."
            ),
            "action": "Implementar una mejora semanal propuesta por el equipo",
            "action_explanation": (
                "Activa mejora continua sin grandes proyectos."
            ),
            "tool": "Círculo de Mejora Continua",
            "tool_explanation": (
                "Sistematiza pequeñas mejoras sostenidas."
            ),
        },
        "master_treatment": {
            "decision": "Evolución Operativa",
            "decision_explanation": (
                "El sistema aprende o se queda obsoleto."
            ),
            "action": "Institucionalizar mejora continua",
            "action_explanation": (
                "Hace antifrágil la operación."
            ),
            "tool": "Sistema Kaizen Dirigido",
            "tool_explanation": (
                "Canaliza mejoras alineadas al objetivo."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S6
    # ---------------------------------------------------------
    "UNI-S6": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 16,
            "department": "PROCESOS",
            "plan": "PRE",
            "code": "UNI-S6",
            "logic": (
                "Proceso Documentado: Saber si el negocio depende de personas "
                "o de procesos replicables."
            ),
        },
        "treatment": {
            "decision": "Eliminación de Grasa",
            "decision_explanation": (
                "Reducir movimientos, esperas y exceso de inventario."
            ),
            "action": "Localizar desperdicios y ajustar reposición",
            "action_explanation": (
                "Disminuye capital inmovilizado y fricción."
            ),
            "tool": "Registro de Mudas + Kanban",
            "tool_explanation": (
                "Controla flujo y reposición según consumo real."
            ),
        },
        "master_treatment": {
            "decision": "Activación de Recursos",
            "decision_explanation": (
                "Los recursos deben trabajar o desaparecer."
            ),
            "action": "Convertir desperdicio en capacidad",
            "action_explanation": (
                "Reduce coste estructural."
            ),
            "tool": "Tablero de Activación Lean",
            "tool_explanation": (
                "Mide uso real de recursos."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S7
    # ---------------------------------------------------------
    "UNI-S7": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 17,
            "department": "PROCESOS",
            "plan": "PRE",
            "code": "UNI-S7",
            "logic": (
                "Soporte del Sistema: Medir cuánto del trabajo se apoya en herramientas "
                "y cuánto en esfuerzo manual."
            ),
        },
        "treatment": {
            "decision": "Protocolización de Roles",
            "decision_explanation": (
                "Reducir riesgo operativo ligado a individuos."
            ),
            "action": "Crear fichas de puesto con KPIs claros",
            "action_explanation": (
                "Permite sustitución y escalabilidad."
            ),
            "tool": "Matriz de Polivalencia",
            "tool_explanation": (
                "Mide capacidad de cubrir funciones críticas."
            ),
        },
        "master_treatment": {
            "decision": "Soberanía del Rol",
            "decision_explanation": (
                "El rol importa más que la persona."
            ),
            "action": "Diseñar puestos autónomos y replicables",
            "action_explanation": (
                "El negocio no depende de héroes."
            ),
            "tool": "Arquitectura de Roles",
            "tool_explanation": (
                "Separa función, responsabilidad y persona."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S8
    # ---------------------------------------------------------
    "UNI-S8": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 18,
            "department": "PROCESOS",
            "plan": "PRE",
            "code": "UNI-S8",
            "logic": (
                "Proceso de Decisión: Saber si las decisiones se toman con datos consistentes "
                "o con intuición."
            ),
        },
        "treatment": {
            "decision": "Ritmos de Gestión",
            "decision_explanation": (
                "Ordenar la toma de decisiones y la transmisión de órdenes."
            ),
            "action": "Implantar reuniones cortas y canales oficiales",
            "action_explanation": (
                "Reduce errores por malentendidos."
            ),
            "tool": "Agenda de Gobierno Interno + Manual",
            "tool_explanation": (
                "Estandariza cuándo, cómo y quién comunica."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno de la Decisión",
            "decision_explanation": (
                "Decidir es un proceso, no un acto."
            ),
            "action": "Centralizar datos, ritmos y canales",
            "action_explanation": (
                "Reduce errores estratégicos."
            ),
            "tool": "Sistema de Gobierno Interno",
            "tool_explanation": (
                "Ordena información y autoridad."
            ),
        },
    },

    # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S9
    # ---------------------------------------------------------
    "UNI-S9": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 19,
            "department": "PROCESOS",
            "plan": "PRE",
            "code": "UNI-S9",
            "logic": (
                "Autonomía del Negocio: Medir si la empresa puede operar sin la presencia constante del dueño."
            ),
        },
        "treatment": {
            "decision": "Plan Preventivo Operativo",
            "decision_explanation": (
                "Evitar paradas por descuido o improvisación."
            ),
            "action": "Establecer revisiones periódicas de activos clave",
            "action_explanation": (
                "Reduce incidencias y dependencia personal."
            ),
            "tool": "Plan de Prevención",
            "tool_explanation": (
                "Anticipa fallos antes de que ocurran."
            ),
        },
        "master_treatment": {
            "decision": "Autonomía Sistémica",
            "decision_explanation": (
                "El negocio debe operar sin presencia constante."
            ),
            "action": "Crear mecanismos de autocontrol",
            "action_explanation": (
                "Libera tiempo del dueño."
            ),
            "tool": "Sistema de Autogestión",
            "tool_explanation": (
                "Mantiene estabilidad sin supervisión directa."
            ),
        },
    },

       # ---------------------------------------------------------
    # UNIDAD DE PROCESOS — S10
    # ---------------------------------------------------------
    "UNI-S10": {
        "meta": {
            "specialty": "UNIDAD DE PROCESOS",
            "description": (
                "Unidad crítica que detecta dónde se pierde tiempo, dinero y energía. "
                "Establece estándares simples, elimina desperdicios y crea flujo real de valor. "
                "No se toleran 'costumbres' sin ROI: cada paso debe justificar su existencia."
            ),
            "strategic_objective": (
                "Bajar el estrés operativo y los costes invisibles, subir la productividad por rol "
                "y garantizar entregas a tiempo con una operativa ligera, clara y escalable."
            ),
            "order": 20,
            "department": "PROCESOS",
            "plan": "PRE",
            "code": "UNI-S10",
            "logic": (
                "Escalabilidad del Sistema: Evaluar si el negocio puede crecer sin multiplicar problemas."
            ),
        },
        "treatment": {
            "decision": "Ingeniería de Costes",
            "decision_explanation": (
                "Detectar límites estructurales al crecimiento."
            ),
            "action": "Rediseñar procesos para reducir coste unitario",
            "action_explanation": (
                "Permite crecer sin colapsar."
            ),
            "tool": "Mapa de Valorización S10 + RACI",
            "tool_explanation": (
                "Relaciona coste, valor y responsabilidad."
            ),
        },
        "master_treatment": {
            "decision": "Arquitectura Escalable",
            "decision_explanation": (
                "El crecimiento se diseña antes de ejecutarse."
            ),
            "action": "Rediseñar procesos para crecer sin fricción",
            "action_explanation": (
                "Permite escalar sin multiplicar problemas."
            ),
            "tool": "Arquitectura Operativa S10",
            "tool_explanation": (
                "Define límites y palancas de escalado."
            ),
        },
    },
    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S1
    # ---------------------------------------------------------
    "CARDIO-S1": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa. Detecta fugas de clientes activos, "
                "impulsa la conversión y fortalece la cartera con productos estrella y estrategias de fidelización. "
                "Aquí se mide el pulso real del negocio: ventas, clientes y recurrencia."
            ),
            "strategic_objective": "",
            "order": 21,
            "department": "COMERCIAL",
            "plan": "PIE",
            "code": "CARDIO-S1",
            "logic": (
                "Eficiencia Comercial: Saber si el esfuerzo comercial se transforma en clientes "
                "o se diluye en contactos sin conversión."
            ),
        },
        "treatment": {
            "decision": "Radiografía de Cartera",
            "decision_explanation": (
                "Detectar qué clientes generan ingresos reales y quiénes consumen recursos sin retorno."
            ),
            "action": "Clasificar clientes en Activos, Dormidos y Perdidos",
            "action_explanation": (
                "Permite enfocar esfuerzos en clientes valiosos y reactivar los perdidos."
            ),
            "tool": "Clasificación de Clientes",
            "tool_explanation": (
                "Visualiza el estado de cada cliente para priorizar acciones."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno de la Cartera",
            "decision_explanation": (
                "Controlar flujo de clientes activos, inactivos y perdidos."
            ),
            "action": "Rediseñar segmentación y priorización de clientes",
            "action_explanation": (
                "Convierte cartera en activo estratégico y reduce fugas."
            ),
            "tool": "Radar de Clientes Estratégicos",
            "tool_explanation": (
                "Muestra estado y potencial de todos los clientes."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S2
    # ---------------------------------------------------------
    "CARDIO-S2": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 22,
            "department": "COMERCIAL",
            "plan": "PIE",
            "code": "CARDIO-S2",
            "logic": (
                "Riesgo de Concentración: Medir cuánto depende el negocio de un solo cliente "
                "y el peligro real si desaparece."
            ),
        },
        "treatment": {
            "decision": "Protocolo de Rescate",
            "decision_explanation": (
                "Evitar dependencia de un único cliente y minimizar riesgo de pérdida."
            ),
            "action": "Contactar clientes inactivos >90 días",
            "action_explanation": (
                "Reduce riesgo de abandono y estabiliza ingresos."
            ),
            "tool": "Plan de Rescate Comercial",
            "tool_explanation": (
                "Define pasos claros de intervención para clientes en riesgo."
            ),
        },
        "master_treatment": {
            "decision": "Dominio del Riesgo",
            "decision_explanation": (
                "Asegurar continuidad comercial sin depender de clientes individuales."
            ),
            "action": "Ejecutar plan de rescate inmediato y personalizado",
            "action_explanation": (
                "Minimiza riesgo de pérdida y asegura ingresos."
            ),
            "tool": "Protocolo de Recuperación de Clientes",
            "tool_explanation": (
                "Define acciones de retención y seguimiento crítico."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S3
    # ---------------------------------------------------------
    "CARDIO-S3": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 23,
            "department": "COMERCIAL",
            "plan": "PIE",
            "code": "CARDIO-S3",
            "logic": (
                "Regularidad Comercial: Detectar si las ventas responden a un sistema estable "
                "o a picos de suerte."
            ),
        },
        "treatment": {
            "decision": "Inyección de Producto Estrella",
            "decision_explanation": (
                "Aumentar claridad y relevancia de la oferta."
            ),
            "action": "Re-empaquetar producto de mayor margen como oferta principal",
            "action_explanation": (
                "Mejora conversión y comprensión de valor."
            ),
            "tool": "Reposicionamiento de Producto",
            "tool_explanation": (
                "Destaca la propuesta más rentable para el cliente."
            ),
        },
        "master_treatment": {
            "decision": "Arquitectura de Producto",
            "decision_explanation": (
                "Crear claridad absoluta sobre propuesta de valor."
            ),
            "action": "Reestructurar producto estrella y comunicación al cliente",
            "action_explanation": (
                "Maximiza conversión y foco en margen."
            ),
            "tool": "Mapa de Valor Comercial",
            "tool_explanation": (
                "Visualiza productos estratégicos y oportunidades."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S4
    # ---------------------------------------------------------
    "CARDIO-S4": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 24,
            "department": "COMERCIAL",
            "plan": "PRE",
            "code": "CARDIO-S4",
            "logic": (
                "Coste de Crecer: Saber si captar clientes genera valor "
                "o erosiona el margen desde el inicio."
            ),
        },
        "treatment": {
            "decision": "Limpieza de Prospección",
            "decision_explanation": (
                "Priorizar leads de alto potencial frente a contactos irrelevantes."
            ),
            "action": "Eliminar leads 'basura' y concentrarse en oportunidades reales",
            "action_explanation": (
                "Reduce costes de adquisición y aumenta eficiencia."
            ),
            "tool": "Auditoría de Leads",
            "tool_explanation": (
                "Clasifica prospectos según probabilidad de conversión."
            ),
        },
        "master_treatment": {
            "decision": "Optimización de Prospección",
            "decision_explanation": (
                "Convertir el pipeline en motor de ingresos confiable."
            ),
            "action": "Repriorizar leads según potencial y ROI",
            "action_explanation": (
                "Evita esfuerzos desperdiciados y acelera ventas."
            ),
            "tool": "Sistema de Leads Prioritarios",
            "tool_explanation": (
                "Permite gestión dinámica de oportunidades valiosas."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S5
    # ---------------------------------------------------------
    "CARDIO-S5": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 25,
            "department": "COMERCIAL",
            "plan": "PRE",
            "code": "CARDIO-S5",
            "logic": (
                "Vida de la Cartera: Medir si los clientes vuelven "
                "o si el negocio vive siempre de empezar de cero."
            ),
        },
        "treatment": {
            "decision": "Plan de Fidelización",
            "decision_explanation": (
                "Aumentar repetición de compra y hábito de consumo."
            ),
            "action": "Implementar ciclos de recompra automática o recordatorios",
            "action_explanation": (
                "Incrementa ingresos recurrentes y relación con clientes."
            ),
            "tool": "Sistema de Fidelización",
            "tool_explanation": (
                "Mantiene contacto constante y estructurado con clientes."
            ),
        },
        "master_treatment": {
            "decision": "Diseño de Fidelización",
            "decision_explanation": (
                "Convertir clientes en fuentes sostenibles de ingresos."
            ),
            "action": "Implementar ciclo automático de recompra y engagement",
            "action_explanation": (
                "Genera hábito de compra y recurrencia."
            ),
            "tool": "Programa de Retención Estratégica",
            "tool_explanation": (
                "Estandariza la relación con clientes a largo plazo."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S6
    # ---------------------------------------------------------
    "CARDIO-S6": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 26,
            "department": "COMERCIAL",
            "plan": "PRE",
            "code": "CARDIO-S6",
            "logic": (
                "Posicionamiento de Precio: Evaluar si el precio genera valor percibido "
                "o deja dinero encima de la mesa."
            ),
        },
        "treatment": {
            "decision": "Estrategia de Upsell/Cross-sell",
            "decision_explanation": (
                "Incrementar valor de cada cliente sin aumentar coste de adquisición."
            ),
            "action": "Diseñar ofertas complementarias para clientes actuales",
            "action_explanation": (
                "Mejora margen por cliente y rentabilidad."
            ),
            "tool": "Paquetes y Bundles",
            "tool_explanation": (
                "Permite combinar productos para aumentar ticket medio."
            ),
        },
        "master_treatment": {
            "decision": "Maximización de Valor",
            "decision_explanation": (
                "Aumentar rentabilidad por cliente sin esfuerzo adicional."
            ),
            "action": "Diseñar estrategias de upsell y cross-sell integradas",
            "action_explanation": (
                "Incrementa margen global y ticket promedio."
            ),
            "tool": "Arquitectura de Ofertas Integradas",
            "tool_explanation": (
                "Identifica combinaciones óptimas de venta."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S7
    # ---------------------------------------------------------
    "CARDIO-S7": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 27,
            "department": "COMERCIAL",
            "plan": "PRE",
            "code": "CARDIO-S7",
            "logic": (
                "Valor de Cada Venta: Medir si el esfuerzo comercial se dedica "
                "a operaciones que merecen la pena."
            ),
        },
        "treatment": {
            "decision": "Automatización de Hitos",
            "decision_explanation": (
                "Asegurar que cada venta recibe seguimiento sistemático."
            ),
            "action": "Configurar secuencias automáticas postventa",
            "action_explanation": (
                "Evita pérdida de oportunidades y mejora experiencia del cliente."
            ),
            "tool": "CRM / Secuencias Automáticas",
            "tool_explanation": (
                "Garantiza seguimiento consistente y documentado."
            ),
        },
        "master_treatment": {
            "decision": "Control de Relación",
            "decision_explanation": (
                "Garantizar que ninguna oportunidad se pierde."
            ),
            "action": "Automatizar y monitorizar hitos críticos de seguimiento",
            "action_explanation": (
                "Asegura consistencia y cierre de oportunidades."
            ),
            "tool": "Plataforma CRM Estratégica",
            "tool_explanation": (
                "Visualiza pipeline completo y acciones necesarias."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S8
    # ---------------------------------------------------------
    "CARDIO-S8": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 28,
            "department": "COMERCIAL",
            "plan": "PRE",
            "code": "CARDIO-S8",
            "logic": (
                "Velocidad de Conversión: Saber cuántos días tarda una oportunidad "
                "en convertirse en dinero real."
            ),
        },
        "treatment": {
            "decision": "Diversificación Comercial",
            "decision_explanation": (
                "Reducir riesgo asociado a un único canal de ventas."
            ),
            "action": "Testar nuevos canales de captación (LinkedIn, alianzas, etc.)",
            "action_explanation": (
                "Aumenta resiliencia y oportunidades de ingreso."
            ),
            "tool": "Plan Multicanal",
            "tool_explanation": (
                "Permite monitorizar desempeño y explorar nuevas fuentes."
            ),
        },
        "master_treatment": {
            "decision": "Soberanía Comercial",
            "decision_explanation": (
                "Reducir riesgo estructural de canal único."
            ),
            "action": "Testar y consolidar múltiples canales de captación",
            "action_explanation": (
                "Diversifica ingresos y fortalece resiliencia."
            ),
            "tool": "Plan Multicanal Estratégico",
            "tool_explanation": (
                "Mide efectividad de cada canal y prioriza inversión."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S9
    # ---------------------------------------------------------
    "CARDIO-S9": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 29,
            "department": "COMERCIAL",
            "plan": "PRE",
            "code": "CARDIO-S9",
            "logic": (
                "Aprendizaje Comercial: Medir si cada 'no' mejora el sistema "
                "o se pierde como ruido."
            ),
        },
        "treatment": {
            "decision": "Optimización de Conversión",
            "decision_explanation": (
                "Aprender de cada 'no' y mejorar comunicación."
            ),
            "action": "Cambiar enfoque de 'lo que hago' a 'lo que resuelvo'",
            "action_explanation": (
                "Incrementa efectividad comercial y conversión."
            ),
            "tool": "Revisión de Pitch Comercial",
            "tool_explanation": (
                "Analiza resultados y ajusta mensajes estratégicamente."
            ),
        },
        "master_treatment": {
            "decision": "Evolución del Pitch",
            "decision_explanation": (
                "Transformar cada interacción en aprendizaje y conversión."
            ),
            "action": "Redefinir enfoque de comunicación hacia resolución de problemas",
            "action_explanation": (
                "Mejora efectividad de cada contacto comercial."
            ),
            "tool": "Sistema de Optimización de Mensaje",
            "tool_explanation": (
                "Permite ajustes continuos basados en resultados reales."
            ),
        },
    },

    # ---------------------------------------------------------
    # CARDIOLOGÍA COMERCIAL — S10
    # ---------------------------------------------------------
    "CARDIO-S10": {
        "meta": {
            "specialty": "CARDIOLOGIA COMERCIAL",
            "description": (
                "Es la unidad que revitaliza el corazón comercial de la empresa."
            ),
            "strategic_objective": "",
            "order": 30,
            "department": "COMERCIAL",
            "plan": "PRE",
            "code": "CARDIO-S10",
            "logic": (
                "Marca que Vende Sola: Evaluar la fuerza comercial que existe "
                "incluso cuando no estás presente."
            ),
        },
        "treatment": {
            "decision": "Optimización del LTV",
            "decision_explanation": (
                "Incrementar fuerza comercial independiente del vendedor."
            ),
            "action": "Implementar sistema de lealtad y aumento de ticket medio",
            "action_explanation": (
                "Aumenta ingresos recurrentes y retención de clientes."
            ),
            "tool": "Programa de Referidos y Loyalty",
            "tool_explanation": (
                "Fomenta ventas adicionales y recomendación espontánea."
            ),
        },
        "master_treatment": {
            "decision": "Marca Autónoma",
            "decision_explanation": (
                "Hacer que la marca venda incluso sin presencia directa."
            ),
            "action": "Implementar lealtad, referidos y estrategias de aumento de ticket",
            "action_explanation": (
                "Incrementa ingresos sostenibles y recurrentes."
            ),
            "tool": "Programa de Lealtad & Referral",
            "tool_explanation": (
                "Sistema que amplifica ventas y fidelización sin intervención."
            ),
        },
    },
    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S1
    # ---------------------------------------------------------
    "NEURO-S1": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa. Detecta dispersión, falta de foco y decisiones improvisadas. "
                "Reestructura la visión, ordena prioridades y activa un sistema de dirección claro y medible."
            ),
            "strategic_objective": (
                "Dar claridad de rumbo, ordenar prioridades y garantizar que cada decisión esté conectada con la visión y los resultados."
            ),
            "order": 31,
            "department": "ESTRATÉGIA",
            "plan": "PIE",
            "code": "NEURO-S1",
            "logic": (
                "Alineación del Equipo: Medir si la fuerza operativa rema hacia el mismo objetivo que la dirección."
            ),
        },
        "treatment": {
            "decision": "Fijación de Rumbo",
            "decision_explanation": (
                "Detectar si el equipo conoce y entiende los objetivos estratégicos."
            ),
            "action": "Entrevista de alineación con el Comité",
            "action_explanation": (
                "Alinea esfuerzos y elimina dispersión."
            ),
            "tool": "Manifiesto de Visión 1-Page",
            "tool_explanation": (
                "Resume y comunica objetivos de manera clara y rápida."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno de la Visión",
            "decision_explanation": (
                "Alinear mentalmente a todo el equipo con la dirección estratégica."
            ),
            "action": "Sistematizar revisión y comunicación de objetivos",
            "action_explanation": (
                "Asegura que todos reman hacia mismo Norte."
            ),
            "tool": "Manifiesto Estratégico",
            "tool_explanation": (
                "Documento vivo de referencia para toda la organización."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S2
    # ---------------------------------------------------------
    "NEURO-S2": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Dar claridad de rumbo, ordenar prioridades y garantizar decisiones conectadas con la visión."
            ),
            "order": 32,
            "department": "ESTRATÉGIA",
            "plan": "PIE",
            "code": "NEURO-S2",
            "logic": (
                "Foco Estratégico: Saber si el dueño está 'pensando' el futuro o 'apagando fuegos' del presente."
            ),
        },
        "treatment": {
            "decision": "Corte de Ramas",
            "decision_explanation": (
                "Identificar proyectos que consumen tiempo sin impacto estratégico."
            ),
            "action": "Listar proyectos activos y filtrar por impacto",
            "action_explanation": (
                "Permite al dueño centrarse en prioridades críticas."
            ),
            "tool": "Matriz de Priorización (Impacto/Esfuerzo)",
            "tool_explanation": (
                "Clasifica iniciativas según valor y esfuerzo."
            ),
        },
        "master_treatment": {
            "decision": "Dominio de Prioridades",
            "decision_explanation": (
                "Reducir dispersión de tiempo y recursos en iniciativas de bajo impacto."
            ),
            "action": "Rediseñar portafolio de proyectos eliminando lastre",
            "action_explanation": (
                "Optimiza concentración de esfuerzos y velocidad de ejecución."
            ),
            "tool": "Matriz de Impacto Estratégico",
            "tool_explanation": (
                "Visualiza qué proyectos aportan verdadero valor."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S3
    # ---------------------------------------------------------
    "NEURO-S3": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Dar claridad de rumbo y garantizar foco estratégico."
            ),
            "order": 33,
            "department": "ESTRATÉGIA",
            "plan": "PIE",
            "code": "NEURO-S3",
            "logic": (
                "Limpieza de Portafolio: Identificar productos o servicios que consumen recursos pero no dan beneficio."
            ),
        },
        "treatment": {
            "decision": "Sincronización de Agenda",
            "decision_explanation": (
                "Detectar productos/servicios que consumen recursos sin retorno."
            ),
            "action": "Definir 3 hitos innegociables del trimestre",
            "action_explanation": (
                "Garantiza enfoque operativo y estratégico."
            ),
            "tool": "Roadmap Estratégico",
            "tool_explanation": (
                "Visualiza metas clave y plazos de ejecución."
            ),
        },
        "master_treatment": {
            "decision": "Arquitectura de Portafolio",
            "decision_explanation": (
                "Evitar consumo de recursos en iniciativas sin retorno."
            ),
            "action": "Establecer hitos estratégicos trimestrales",
            "action_explanation": (
                "Garantiza foco en resultados relevantes."
            ),
            "tool": "Roadmap Maestro",
            "tool_explanation": (
                "Conecta estrategia con ejecución operativa."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S4
    # ---------------------------------------------------------
    "NEURO-S4": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Dar claridad de rumbo y decisiones basadas en datos."
            ),
            "order": 34,
            "department": "ESTRATÉGIA",
            "plan": "PRE",
            "code": "NEURO-S4",
            "logic": (
                "Diversificación de Riesgo: Medir la dependencia de un solo mercado o sector."
            ),
        },
        "treatment": {
            "decision": "Objetivación del Éxito",
            "decision_explanation": (
                "Evitar decisiones basadas en corazonadas."
            ),
            "action": "Identificar 5 KPIs maestros a monitorear",
            "action_explanation": (
                "Permite medir y actuar con datos."
            ),
            "tool": "Dashboard de Mando Neuro",
            "tool_explanation": (
                "Visualiza indicadores clave y resultados estratégicos."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno por Indicadores",
            "decision_explanation": (
                "Convertir intuición en decisiones basadas en datos."
            ),
            "action": "Seleccionar y monitorizar KPIs críticos",
            "action_explanation": (
                "Permite decisiones rápidas y precisas."
            ),
            "tool": "Dashboard Estratégico",
            "tool_explanation": (
                "Centraliza indicadores y muestra el estado del negocio."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S5
    # ---------------------------------------------------------
    "NEURO-S5": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Aumentar velocidad y calidad de decisiones."
            ),
            "order": 35,
            "department": "ESTRATÉGIA",
            "plan": "PRE",
            "code": "NEURO-S5",
            "logic": (
                "Índice de Innovación: Saber si la empresa se está quedando obsoleta o se renueva."
            ),
        },
        "treatment": {
            "decision": "Protocolo de Decisión",
            "decision_explanation": (
                "Reducir el agotamiento y aumentar velocidad de decisión."
            ),
            "action": "Implementar sistema de criterios para el 'SÍ'",
            "action_explanation": (
                "Acelera decisiones y reduce indecisión."
            ),
            "tool": "Árbol de Decisión MASESORA",
            "tool_explanation": (
                "Estandariza criterios y pasos de decisión."
            ),
        },
        "master_treatment": {
            "decision": "Sistema de Decisión Ágil",
            "decision_explanation": (
                "Estandarizar criterios y reducir indecisión."
            ),
            "action": "Definir protocolo de decisiones rápidas",
            "action_explanation": (
                "Mejora velocidad y consistencia de decisiones."
            ),
            "tool": "Árbol de Decisión Avanzado",
            "tool_explanation": (
                "Facilita aplicar criterios de juicio estratégicos."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S6
    # ---------------------------------------------------------
    "NEURO-S6": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Mejorar eficiencia interdepartamental."
            ),
            "order": 36,
            "department": "ESTRATÉGIA",
            "plan": "PRE",
            "code": "NEURO-S6",
            "logic": (
                "Escalabilidad de Ventas: Medir cuánto cuesta conseguir un cliente respecto a lo que gasta."
            ),
        },
        "treatment": {
            "decision": "Interconexión Departamental",
            "decision_explanation": (
                "Detectar falta de comunicación entre áreas."
            ),
            "action": "Reunión de alineación cruzada (Cross-dept)",
            "action_explanation": (
                "Conecta información y evita duplicidades."
            ),
            "tool": "Mapa de Dependencias",
            "tool_explanation": (
                "Muestra relaciones y dependencias entre áreas."
            ),
        },
        "master_treatment": {
            "decision": "Sinapsis Organizacional",
            "decision_explanation": (
                "Integrar información entre departamentos y eliminar aislamiento."
            ),
            "action": "Implementar reuniones cross-dept y flujos de información",
            "action_explanation": (
                "Mejora colaboración y eficiencia interdepartamental."
            ),
            "tool": "Mapa de Dependencias Estratégico",
            "tool_explanation": (
                "Visualiza relaciones críticas y flujos de valor."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S7
    # ---------------------------------------------------------
    "NEURO-S7": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Aumentar autonomía operativa y estratégica."
            ),
            "order": 37,
            "department": "ESTRATÉGIA",
            "plan": "PRE",
            "code": "NEURO-S7",
            "logic": (
                "Grado de Autonomía: Medir si el negocio vende por su 'sistema' o por la 'marca personal' del dueño."
            ),
        },
        "treatment": {
            "decision": "Neuro-plasticidad",
            "decision_explanation": (
                "Medir si la empresa depende del dueño o de sistemas replicables."
            ),
            "action": "Taller de gestión del cambio y nuevas metas",
            "action_explanation": (
                "Facilita adopción de procesos y autonomía."
            ),
            "tool": "Plan de Adopción de Estrategia",
            "tool_explanation": (
                "Acompaña transición hacia sistemas operativos autónomos."
            ),
        },
        "master_treatment": {
            "decision": "Neuro-adaptabilidad",
            "decision_explanation": (
                "La empresa debe adaptarse sin depender de líderes individuales."
            ),
            "action": "Talleres de cambio y adopción de nuevas metas",
            "action_explanation": (
                "Facilita resiliencia organizacional."
            ),
            "tool": "Plan de Adopción Estratégico",
            "tool_explanation": (
                "Sistematiza cambio cultural y operativo."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S8
    # ---------------------------------------------------------
    "NEURO-S8": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Alinear ejecución con estrategia."
            ),
            "order": 38,
            "department": "ESTRATÉGIA",
            "plan": "PRE",
            "code": "NEURO-S8",
            "logic": (
                "Agilidad Estratégica: Tiempo que pasa desde que se decide un cambio hasta que se ejecuta."
            ),
        },
        "treatment": {
            "decision": "Alineación Vertical",
            "decision_explanation": (
                "Medir si los objetivos se traducen en acciones consistentes."
            ),
            "action": "Revisar que tareas del equipo sumen a los KPIs",
            "action_explanation": (
                "Garantiza que cada acción aporta al objetivo."
            ),
            "tool": "Cascada de Objetivos (OKR)",
            "tool_explanation": (
                "Conecta visión estratégica con ejecución diaria."
            ),
        },
        "master_treatment": {
            "decision": "Alineación de Ejecución",
            "decision_explanation": (
                "Garantizar que estrategia se traduzca en acción consistente."
            ),
            "action": "Revisar tareas y KPIs alineados a objetivos estratégicos",
            "action_explanation": (
                "Minimiza errores tácticos y dispersión."
            ),
            "tool": "Cascada OKR Avanzada",
            "tool_explanation": (
                "Conecta objetivos estratégicos con resultados operativos."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S9
    # ---------------------------------------------------------
    "NEURO-S9": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Fortalecer ventaja competitiva."
            ),
            "order": 39,
            "department": "ESTRATÉGIA",
            "plan": "PRE",
            "code": "NEURO-S9",
            "logic": (
                "Foso Defensivo: Medir la ventaja competitiva (qué tan difícil es copiarte)."
            ),
        },
        "treatment": {
            "decision": "Visión Prospectiva",
            "decision_explanation": (
                "Detectar vulnerabilidades frente a competencia."
            ),
            "action": "Sesión de análisis de amenazas y oportunidades",
            "action_explanation": (
                "Fortalece diferenciación y blindaje del negocio."
            ),
            "tool": "Matriz DAFO Dinámica",
            "tool_explanation": (
                "Identifica ventajas competitivas y riesgos emergentes."
            ),
        },
        "master_treatment": {
            "decision": "Visión Prospectiva Estratégica",
            "decision_explanation": (
                "Mantener ventaja competitiva y barreras de entrada."
            ),
            "action": "Sesión de análisis prospectivo y escenarios futuros",
            "action_explanation": (
                "Protege márgenes y fortalece posición."
            ),
            "tool": "Matriz DAFO Dinámica Avanzada",
            "tool_explanation": (
                "Analiza amenazas, oportunidades y ventajas sostenibles."
            ),
        },
    },

    # ---------------------------------------------------------
    # NEUROLOGÍA ESTRATÉGICA — S10
    # ---------------------------------------------------------
    "NEURO-S10": {
        "meta": {
            "specialty": "NEUROLOGIA ESTRATÉGICA",
            "description": (
                "Es la unidad que alinea el cerebro de la empresa."
            ),
            "strategic_objective": (
                "Convertir la estrategia en un activo financiero autónomo."
            ),
            "order": 40,
            "department": "ESTRATÉGIA",
            "plan": "PRE",
            "code": "NEURO-S10",
            "logic": (
                "Valor de la Estrategia: Relación entre el valor de la empresa y la inversión del dueño."
            ),
        },
        "treatment": {
            "decision": "Sello de Alta Neurológica",
            "decision_explanation": (
                "Medir el valor de la estrategia respecto a la inversión del dueño."
            ),
            "action": "Evaluación de alineación del 100% del equipo",
            "action_explanation": (
                "Permite que el negocio sea un activo financiero independiente."
            ),
            "tool": "Certificado de Foco Estratégico",
            "tool_explanation": (
                "Certifica alineación, claridad y madurez estratégica."
            ),
        },
               "master_treatment": {
            "decision": "Sello de Maestría Estratégica",
            "decision_explanation": (
                "Transformar la empresa en un activo autónomo y escalable."
            ),
            "action": "Certificar alineación y claridad total de objetivos y equipo",
            "action_explanation": (
                "Convierte estrategia en patrimonio empresarial."
            ),
            "tool": "Certificado de Gobierno Estratégico",
            "tool_explanation": (
                "Garante que visión, ejecución y resultados están totalmente conectados."
            ),
        },
    },
    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S1
    # ---------------------------------------------------------
    "CLI-S1": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa. Transforma procesos manuales, repetitivos "
                "y desgastantes en flujos automáticos, inteligentes y optimizados. El resultado: más tiempo, menos errores "
                "y una operativa que escala sin añadir más personas."
            ),
            "strategic_objective": (
                "Multiplicar la eficiencia, reducir costes ocultos y liberar al empresario y su equipo para que se centren "
                "en lo que realmente genera valor."
            ),
            "order": 41,
            "department": "GESTION",
            "plan": "PIE",
            "code": "CLI-S1",
            "logic": (
                "Velocidad de Cierre: Medir la capacidad de obtener la foto de beneficio real rápido."
            ),
        },
        "treatment": {
            "decision": "Drenaje de Incendios",
            "decision_explanation": (
                "Detectar retrasos en cierre y decisiones basadas en intuición."
            ),
            "action": "Clasificar tareas diarias en Operar vs. Gestionar",
            "action_explanation": (
                "Evita apagar fuegos y prioriza acciones críticas."
            ),
            "tool": "Matriz Operar/Gestionar",
            "tool_explanation": (
                "Permite identificar actividades de alto impacto vs. rutina."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno de Emergencias",
            "decision_explanation": (
                "El negocio debe reaccionar rápido sin caos."
            ),
            "action": "Implementar flujo de decisiones críticas automáticas",
            "action_explanation": (
                "Reduce latencia y errores en cierre financiero."
            ),
            "tool": "Flujo de Drenaje Estratégico",
            "tool_explanation": (
                "Coordina acciones de urgencia sin intervención manual."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S2
    # ---------------------------------------------------------
    "CLI-S2": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Multiplicar eficiencia y convertir datos en acción."
            ),
            "order": 42,
            "department": "GESTION",
            "plan": "PIE",
            "code": "CLI-S2",
            "logic": (
                "Utilidad del Dato: Saber si mides por medir o si los datos sirven para actuar."
            ),
        },
        "treatment": {
            "decision": "Fluidez de Información",
            "decision_explanation": (
                "Medir si los datos realmente permiten actuar."
            ),
            "action": "Organizar el 'Cerebro Digital' (nube unificada)",
            "action_explanation": (
                "Centraliza información y reduce burocracia."
            ),
            "tool": "Repositorio Digital Unificado",
            "tool_explanation": (
                "Facilita búsqueda, acceso y control de información."
            ),
        },
        "master_treatment": {
            "decision": "Control de Información",
            "decision_explanation": (
                "Transformar datos dispersos en conocimiento accionable."
            ),
            "action": "Centralizar y etiquetar información clave",
            "action_explanation": (
                "Facilita decisiones rápidas y precisas."
            ),
            "tool": "Cerebro Digital Integrado",
            "tool_explanation": (
                "Muestra la información relevante organizada y accesible."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S3
    # ---------------------------------------------------------
    "CLI-S3": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Eliminar tareas improductivas y aumentar autonomía operativa."
            ),
            "order": 43,
            "department": "GESTION",
            "plan": "PIE",
            "code": "CLI-S3",
            "logic": (
                "Índice de Seguridad: Medir el cumplimiento de obligaciones para evitar sanciones."
            ),
        },
        "treatment": {
            "decision": "Recuperación de Autonomía",
            "decision_explanation": (
                "Identificar tareas que consumen tiempo innecesario."
            ),
            "action": "Detectar el 20% de tareas que roban el 80% del tiempo",
            "action_explanation": (
                "Libera tiempo para tareas estratégicas."
            ),
            "tool": "Hoja de Registro de Tiempo",
            "tool_explanation": (
                "Visualiza dónde se pierde tiempo y permite optimización."
            ),
        },
        "master_treatment": {
            "decision": "Optimización de Actividades",
            "decision_explanation": (
                "Cada minuto debe generar valor real."
            ),
            "action": "Automatizar y eliminar tareas de bajo impacto",
            "action_explanation": (
                "Incrementa productividad y eficiencia del equipo."
            ),
            "tool": "Analizador de Tiempos Críticos",
            "tool_explanation": (
                "Detecta cuellos de botella y optimiza flujos."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S4
    # ---------------------------------------------------------
    "CLI-S4": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Convertir conocimiento tácito en patrimonio operativo."
            ),
            "order": 44,
            "department": "GESTION",
            "plan": "PRE",
            "code": "CLI-S4",
            "logic": (
                "Fuga Silenciosa: Detectar el gasto sin clasificar que drena el beneficio."
            ),
        },
        "treatment": {
            "decision": "Fijación de Conocimiento",
            "decision_explanation": (
                "Evitar dependencia de la memoria humana."
            ),
            "action": "Protocolizar las 5 acciones que más errores generan",
            "action_explanation": (
                "Reduce errores y asegura continuidad operativa."
            ),
            "tool": "Procedimientos Estandarizados",
            "tool_explanation": (
                "Documenta conocimiento crítico y reduce riesgo humano."
            ),
        },
        "master_treatment": {
            "decision": "Gobernanza del Conocimiento",
            "decision_explanation": (
                "Transformar conocimiento tácito en patrimonio operativo."
            ),
            "action": "Protocolizar y documentar procesos críticos",
            "action_explanation": (
                "Evita pérdida de información y dependencia de personas."
            ),
            "tool": "Sistema de Procedimientos Inteligente",
            "tool_explanation": (
                "Actualiza y comunica procesos automáticamente."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S5
    # ---------------------------------------------------------
    "CLI-S5": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Eliminar procesos manuales y liberar capacidad del equipo."
            ),
            "order": 45,
            "department": "GESTION",
            "plan": "PRE",
            "code": "CLI-S5",
            "logic": (
                "Ratio de Operatividad: Medir si las reuniones producen avances o solo consumen tiempo."
            ),
        },
        "treatment": {
            "decision": "Sustitución Mecánica",
            "decision_explanation": (
                "Detectar procesos manuales que consumen recursos."
            ),
            "action": "Sustituir 1 proceso manual por flujo automático",
            "action_explanation": (
                "Incrementa eficiencia y libera al equipo."
            ),
            "tool": "Automatización de Procesos",
            "tool_explanation": (
                "Convierte tareas repetitivas en procesos automáticos."
            ),
        },
        "master_treatment": {
            "decision": "Flujo Automático",
            "decision_explanation": (
                "Convertir tareas repetitivas en procesos que se autoejecutan."
            ),
            "action": "Implementar automatizaciones clave",
            "action_explanation": (
                "Libera recursos y acelera ejecución."
            ),
            "tool": "Plataforma de Automatización",
            "tool_explanation": (
                "Garantiza ejecución consistente sin intervención manual."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S6
    # ---------------------------------------------------------
    "CLI-S6": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Mejorar velocidad y precisión de decisiones."
            ),
            "order": 46,
            "department": "GESTION",
            "plan": "PRE",
            "code": "CLI-S6",
            "logic": (
                "Nivel de Delegación: Medir cuánto tiempo del dueño sigue atrapado en el 'papeleo'."
            ),
        },
        "treatment": {
            "decision": "Simplificación de Mando",
            "decision_explanation": (
                "Evitar que exceso de información bloquee decisiones."
            ),
            "action": "Reducir datos a 3 KPIs críticos",
            "action_explanation": (
                "Permite enfoque en indicadores que realmente importan."
            ),
            "tool": "Panel de Control Ejecutivo",
            "tool_explanation": (
                "Facilita decisiones rápidas con información clave."
            ),
        },
        "master_treatment": {
            "decision": "Decisión Ágil",
            "decision_explanation": (
                "Reducir complejidad informativa para tomar decisiones estratégicas."
            ),
            "action": "Filtrar información a KPIs críticos",
            "action_explanation": (
                "Mejora velocidad y precisión de decisiones."
            ),
            "tool": "Dashboard Estratégico",
            "tool_explanation": (
                "Presenta indicadores estratégicos en tiempo real."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S7
    # ---------------------------------------------------------
    "CLI-S7": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Crear autonomía operativa real."
            ),
            "order": 47,
            "department": "GESTION",
            "plan": "PRE",
            "code": "CLI-S7",
            "logic": (
                "Orden de Batalla: Saber si el equipo tiene claro qué debe hacer cada día."
            ),
        },
        "treatment": {
            "decision": "Descentralización",
            "decision_explanation": (
                "Evitar que el dueño controle cada acción."
            ),
            "action": "Crear sistema de reporte autónomo del dueño",
            "action_explanation": (
                "Da claridad de responsabilidades y autonomía."
            ),
            "tool": "Sistema de Reporte Automático",
            "tool_explanation": (
                "Permite control sin intervención directa."
            ),
        },
        "master_treatment": {
            "decision": "Autonomía Sistémica",
            "decision_explanation": (
                "Hacer que el sistema funcione sin dueño."
            ),
            "action": "Crear reportes y alertas automáticas",
            "action_explanation": (
                "Permite operación sin supervisión constante."
            ),
            "tool": "Sistema de Reporte Autónomo",
            "tool_explanation": (
                "Facilita control y seguimiento independiente."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S8
    # ---------------------------------------------------------
    "CLI-S8": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Eliminar fricción digital y duplicidades."
            ),
            "order": 48,
            "department": "GESTION",
            "plan": "PRE",
            "code": "CLI-S8",
            "logic": (
                "Salud Digital: Medir si el software trabaja para ti o tú para el software."
            ),
        },
        "treatment": {
            "decision": "Integración de Flujos",
            "decision_explanation": (
                "Detectar duplicación y esfuerzos manuales."
            ),
            "action": "Conectar herramientas y procesos",
            "action_explanation": (
                "Reduce trabajo manual y errores de transferencia."
            ),
            "tool": "Integración de Sistemas",
            "tool_explanation": (
                "Garantiza datos únicos y procesos coordinados."
            ),
        },
        "master_treatment": {
            "decision": "Sincronización de Sistemas",
            "decision_explanation": (
                "Eliminar fricción entre herramientas y procesos."
            ),
            "action": "Integrar plataformas y datos",
            "action_explanation": (
                "Aumenta eficiencia y reduce errores."
            ),
            "tool": "Hub de Integración Operativa",
            "tool_explanation": (
                "Garantiza coordinación total de procesos digitales."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S9
    # ---------------------------------------------------------
    "CLI-S9": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Preparar la empresa para crecer sin fricciones."
            ),
            "order": 49,
            "department": "GESTION",
            "plan": "PRE",
            "code": "CLI-S9",
            "logic": (
                "Horizonte de Previsión: Capacidad de la empresa para ver venir baches de caja."
            ),
        },
        "treatment": {
            "decision": "Elasticidad Operativa",
            "decision_explanation": (
                "Medir capacidad de previsión y reacción."
            ),
            "action": "Crear plan de 'crecimiento sin estrés'",
            "action_explanation": (
                "Permite escalar operaciones sin colapsar."
            ),
            "tool": "Plan de Escalabilidad Operativa",
            "tool_explanation": (
                "Alinea recursos y procesos con crecimiento proyectado."
            ),
        },
        "master_treatment": {
            "decision": "Escalabilidad Controlada",
            "decision_explanation": (
                "Preparar la empresa para crecer sin fricciones."
            ),
            "action": "Diseñar plan de escalabilidad operativa",
            "action_explanation": (
                "Permite crecimiento sostenible y seguro."
            ),
            "tool": "Plan Maestro de Escalabilidad",
            "tool_explanation": (
                "Coordina recursos, procesos y equipos con proyección."
            ),
        },
    },

    # ---------------------------------------------------------
    # GESTIÓN CLÍNICA — S10
    # ---------------------------------------------------------
    "CLI-S10": {
        "meta": {
            "specialty": "GESTION CLINICA",
            "description": (
                "Es la unidad que regenera el tejido operativo de la empresa."
            ),
            "strategic_objective": (
                "Certificar autonomía operativa real."
            ),
            "order": 50,
            "department": "GESTIÓN",
            "plan": "PRE",
            "code": "CLI-S10",
            "logic": (
                "Sello de Gestión: Capacidad de los departamentos para reportar sin ser empujados."
            ),
        },
        "treatment": {
            "decision": "Simulacro de Autonomía",
            "decision_explanation": (
                "Evaluar si los departamentos pueden operar sin supervisión constante."
            ),
            "action": "Superar 7 días de operativa sin intervención del dueño",
            "action_explanation": (
                "Verifica madurez operativa y confianza."
            ),
            "tool": "Prueba de Autonomía Operativa",
            "tool_explanation": (
                "Comprueba capacidad de operación independiente."
            ),
        },
        "master_treatment": {
            "decision": "Sello de Autonomía Operativa",
            "decision_explanation": (
                "Certificar que la empresa puede operar sin intervención."
            ),
            "action": "Ejecutar simulaciones de operación autónoma",
            "action_explanation": (
                "Evalúa madurez operativa y capacidad de auto-sostenimiento."
            ),
            "tool": "Certificado de Operatividad Independiente",
            "tool_explanation": (
                "Verifica autonomía completa del sistema."
            ),
        },
    },
    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S1
    # ---------------------------------------------------------
    "CIR-S1": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa. Mejora la estética comercial, "
                "la presentación de productos/servicios y la comunicación visual para generar impacto inmediato "
                "en clientes y entorno."
            ),
            "strategic_objective": (
                "Provocar un efecto WOW rápido en clientes y mercado, reforzar la percepción de valor "
                "y aumentar la atracción comercial."
            ),
            "order": 51,
            "department": "MARCA",
            "plan": "PIE",
            "code": "CIR-S1",
            "logic": (
                "Atracción Total: Medir la capacidad de la marca para captar atención en ambos mundos."
            ),
        },
        "treatment": {
            "decision": "Radiografía Estética",
            "decision_explanation": (
                "Detectar deficiencias visuales y físicas de la marca."
            ),
            "action": "Auditoría visual 360º de identidad y local",
            "action_explanation": (
                "Identifica puntos críticos y áreas de mejora."
            ),
            "tool": "Informe Puntos Críticos",
            "tool_explanation": (
                "Documenta estado actual de la marca y entorno físico."
            ),
        },
        "master_treatment": {
            "decision": "Gobierno Estético",
            "decision_explanation": (
                "Transformar percepción visual de manera inmediata."
            ),
            "action": "Auditoría completa de identidad y local",
            "action_explanation": (
                "Identifica todas las oportunidades de impacto."
            ),
            "tool": "Informe de Estado de Marca",
            "tool_explanation": (
                "Diagnóstico visual estratégico."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S2
    # ---------------------------------------------------------
    "CIR-S2": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Provocar un efecto WOW rápido y coherente en todos los puntos de contacto."
            ),
            "order": 52,
            "department": "MARCA",
            "plan": "PIE",
            "code": "CIR-S2",
            "logic": (
                "Coherencia de Mensaje: Saber si lo que el cliente ve en redes es lo que encuentra al entrar al local."
            ),
        },
        "treatment": {
            "decision": "Ajuste de Entorno",
            "decision_explanation": (
                "Evitar que la experiencia local contradiga la marca digital."
            ),
            "action": "Cambiar iluminación, orden y señalética",
            "action_explanation": (
                "Alinea experiencia presencial con percepción de marca."
            ),
            "tool": "Checklist de Puesta a Punto",
            "tool_explanation": (
                "Lista de mejoras visuales rápidas y medibles."
            ),
        },
        "master_treatment": {
            "decision": "Coherencia Experiencial",
            "decision_explanation": (
                "Integrar todos los puntos de contacto."
            ),
            "action": "Rediseño de iluminación, orden y señalética",
            "action_explanation": (
                "Garantiza uniformidad de la marca."
            ),
            "tool": "Checklist de Coherencia",
            "tool_explanation": (
                "Lista de verificación para consistencia visual."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S3
    # ---------------------------------------------------------
    "CIR-S3": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Reforzar percepción premium y capacidad de sostener precios altos."
            ),
            "order": 53,
            "department": "MARCA",
            "plan": "PIE",
            "code": "CIR-S3",
            "logic": (
                "Poder de Marca (Premium): Capacidad de sostener precios altos por 'nombre' y no por 'oferta'."
            ),
        },
        "treatment": {
            "decision": "Detalle de Recepción",
            "decision_explanation": (
                "El primer contacto genera percepción inmediata de la marca."
            ),
            "action": "Implementar café, aroma o saludo especial",
            "action_explanation": (
                "Mejora primera impresión y sensación de cuidado."
            ),
            "tool": "Manual de Primera Impresión",
            "tool_explanation": (
                "Establece protocolos de bienvenida consistentes."
            ),
        },
        "master_treatment": {
            "decision": "Experiencia WOW",
            "decision_explanation": (
                "Convertir la recepción en un impacto memorable."
            ),
            "action": "Protocolos de bienvenida multisensorial",
            "action_explanation": (
                "Genera primera impresión positiva e inolvidable."
            ),
            "tool": "Manual de Primera Impresión Avanzado",
            "tool_explanation": (
                "Estándar de interacción inicial con clientes."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S4
    # ---------------------------------------------------------
    "CIR-S4": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Mejorar experiencia y percepción de valor."
            ),
            "order": 54,
            "department": "MARCA",
            "plan": "PIE",
            "code": "CIR-S4",
            "logic": (
                "Experiencia de Cliente: Medir si el cliente 'disfruta' de la marca o solo consume."
            ),
        },
        "treatment": {
            "decision": "Ergonomía de Servicio",
            "decision_explanation": (
                "Identificar fricciones en la experiencia del cliente."
            ),
            "action": "Eliminación de fricciones en atención y venta",
            "action_explanation": (
                "Facilita el proceso y aumenta tiempo de exposición a la oferta."
            ),
            "tool": "Checklist Fricción Cero",
            "tool_explanation": (
                "Lista de pasos críticos de atención optimizados."
            ),
        },
        "master_treatment": {
            "decision": "Servicio Sin Fricción",
            "decision_explanation": (
                "Eliminar fricciones que reducen conversión y satisfacción."
            ),
            "action": "Rediseño completo del flujo de atención",
            "action_explanation": (
                "Mejora percepción y experiencia de compra."
            ),
            "tool": "Checklist de Experiencia Perfecta",
            "tool_explanation": (
                "Estándares para atención fluida y agradable."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S5
    # ---------------------------------------------------------
    "CIR-S5": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Aumentar fidelización emocional y engagement."
            ),
            "order": 55,
            "department": "MARCA",
            "plan": "PRE",
            "code": "CIR-S5",
            "logic": (
                "Fidelidad Híbrida: Clientes que te compran en el local y te siguen/interactúan online."
            ),
        },
        "treatment": {
            "decision": "Micro-experiencias",
            "decision_explanation": (
                "Detectar falta de conexión emocional con el cliente."
            ),
            "action": "Añadir nota escrita o detalle tras compra",
            "action_explanation": (
                "Genera vínculo y fidelización."
            ),
            "tool": "Lista de Acciones WOW",
            "tool_explanation": (
                "Registro de micro-impactos para clientes."
            ),
        },
        "master_treatment": {
            "decision": "Micro-Conexión",
            "decision_explanation": (
                "Crear vínculo emocional con cada cliente."
            ),
            "action": "Implementar micro-experiencias personalizadas",
            "action_explanation": (
                "Aumenta fidelización y engagement."
            ),
            "tool": "Plan de Acciones WOW",
            "tool_explanation": (
                "Registro y seguimiento de experiencias de alto impacto."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S6
    # ---------------------------------------------------------
    "CIR-S6": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Humanizar la marca y aumentar confianza."
            ),
            "order": 56,
            "department": "MARCA",
            "plan": "PRE",
            "code": "CIR-S6",
            "logic": (
                "Reputación 360º: Calidad de la huella que dejas tras el servicio."
            ),
        },
        "treatment": {
            "decision": "Humanización Exprés",
            "decision_explanation": (
                "Evitar marca fría y genérica."
            ),
            "action": "Hacer fotos reales del equipo y productos estrella",
            "action_explanation": (
                "Comunica autenticidad y cercanía."
            ),
            "tool": "Protocolo de Presentación / Banco de Imágenes",
            "tool_explanation": (
                "Establece estándar de presentación visual coherente."
            ),
        },
        "master_treatment": {
            "decision": "Humanización de Marca",
            "decision_explanation": (
                "Convertir la marca en algo cercano y confiable."
            ),
            "action": "Fotos reales y storytelling visual del equipo",
            "action_explanation": (
                "Mejora confianza y cercanía."
            ),
            "tool": "Banco de Imágenes Estratégico",
            "tool_explanation": (
                "Estandariza la comunicación visual auténtica."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S7
    # ---------------------------------------------------------
    "CIR-S7": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Aumentar retención y valor del cliente."
            ),
            "order": 57,
            "department": "MARCA",
            "plan": "PRE",
            "code": "CIR-S7",
            "logic": (
                "Autoridad y Destino: ¿Vienen a buscarte a ti o pasan por delante?"
            ),
        },
        "treatment": {
            "decision": "Sistema de Fidelización",
            "decision_explanation": (
                "Evitar pérdida de clientes tras la compra."
            ),
            "action": "Crear programa de retención y contacto",
            "action_explanation": (
                "Mantiene relación y asegura recompra."
            ),
            "tool": "Plan de Retención",
            "tool_explanation": (
                "Sistema estructurado de seguimiento post-venta."
            ),
        },
        "master_treatment": {
            "decision": "Retención Inteligente",
            "decision_explanation": (
                "Garantizar que la relación continúe tras la venta."
            ),
            "action": "Sistema de seguimiento y recompra automática",
            "action_explanation": (
                "Evita pérdida de clientes y maximiza LTV."
            ),
            "tool": "Plan Maestro de Retención",
            "tool_explanation": (
                "Sistema integral de fidelización multicanal."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S8
    # ---------------------------------------------------------
    "CIR-S8": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Convertir la marca en un activo único y defensible."
            ),
            "order": 58,
            "department": "MARCA",
            "plan": "PRE",
            "code": "CIR-S8",
            "logic": (
                "Eficiencia Omnicanal: Medir si el esfuerzo digital realmente se traduce en ventas físicas."
            ),
        },
        "treatment": {
            "decision": "Diferenciación Única",
            "decision_explanation": (
                "Evitar que la marca sea copiable o irrelevante."
            ),
            "action": "Definir propuesta de valor única",
            "action_explanation": (
                "Protege margen y marca frente a competencia."
            ),
            "tool": "Matriz de Atributos Críticos",
            "tool_explanation": (
                "Identifica los elementos diferenciadores clave."
            ),
        },
        "master_treatment": {
            "decision": "Diferenciación Estratégica",
            "decision_explanation": (
                "Convertir la marca en un activo único."
            ),
            "action": "Definir atributos distintivos y defensibles",
            "action_explanation": (
                "Protege margen y reconocimiento."
            ),
            "tool": "Matriz de Diferenciación Premium",
            "tool_explanation": (
                "Identifica elementos de alto valor percibido."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S9
    # ---------------------------------------------------------
    "CIR-S9": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Atraer público cualificado y aumentar impacto comercial."
            ),
            "order": 59,
            "department": "MARCA",
            "plan": "PRE",
            "code": "CIR-S9",
            "logic": (
                "Calidad del Público: Atraer al cliente que valora el servicio, no al que busca el descuento."
            ),
        },
        "treatment": {
            "decision": "Impulso de Atracción",
            "decision_explanation": (
                "Detectar clientes no comprometidos que podrían generar valor."
            ),
            "action": "Lanzar promoción visualmente potente",
            "action_explanation": (
                "Aumenta visibilidad y tráfico cualificado."
            ),
            "tool": "Campaña Flash de Atracción",
            "tool_explanation": (
                "Acciones rápidas y medibles de impacto comercial."
            ),
        },
        "master_treatment": {
            "decision": "Atracción Proactiva",
            "decision_explanation": (
                "Detectar y activar clientes potenciales de alto valor."
            ),
            "action": "Campaña de visibilidad intensa y segmentada",
            "action_explanation": (
                "Genera tráfico cualificado y rápido impacto."
            ),
            "tool": "Flash Campaign Planner",
            "tool_explanation": (
                "Herramienta de ejecución de campañas de efecto inmediato."
            ),
        },
    },

    # ---------------------------------------------------------
    # CIRUGÍA DE MARCA — S10
    # ---------------------------------------------------------
    "CIR-S10": {
        "meta": {
            "specialty": "CIRUJIA DE MARCA",
            "description": (
                "Es la unidad que aplica un 'lifting exprés' a la empresa."
            ),
            "strategic_objective": (
                "Fortalecer reputación, percepción y crecimiento orgánico."
            ),
            "order": 60,
            "department": "MARCA",
            "plan": "PRE",
            "code": "CIR-S10",
            "logic": (
                "Efecto Altavoz: Capacidad de la marca para que el cliente sea tu comercial."
            ),
        },
        "treatment": {
            "decision": "Sello de Alta Evolutiva",
            "decision_explanation": (
                "Evaluar fuerza de la marca y reputación."
            ),
            "action": "Medición de NPS y monitorizar reseñas",
            "action_explanation": (
                "Permite crecimiento orgánico sostenible."
            ),
            "tool": "Informe de Valor de Marca S10",
            "tool_explanation": (
                "Certifica excelencia externa y reputación positiva."
            ),
        },
        "master_treatment": {
            "decision": "Sello de Excelencia",
            "decision_explanation": (
                "Evaluar y certificar reputación y percepción."
            ),
            "action": "Medición de NPS, reseñas y reputación online",
            "action_explanation": (
                "Permite crecimiento orgánico sostenible y reforzar marca."
            ),
            "tool": "Informe de Reputación Estratégica",
            "tool_explanation": (
                "Certifica percepción positiva y consistencia de marca."
            ),
        },
    },
    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S1
    # ---------------------------------------------------------
    "PSI-S1": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa como si fuera un organismo vivo. "
                "No se limita a medir clima laboral: reprograma la forma en que las personas piensan, sienten y actúan, "
                "alineando liderazgo, motivación y valores."
            ),
            "strategic_objective": (
                "Construir equipos comprometidos, motivados y alineados, donde cada persona se sienta comprendida "
                "y potenciada según su perfil DISC, y donde las emociones se gestionen de forma consciente y productiva."
            ),
            "order": 61,
            "department": "ORGANIZACIONAL",
            "plan": "PIE",
            "code": "PSI-S1",
            "logic": (
                "Índice de 'Estado de Flow': Medir cuánto tiempo trabaja el equipo sin interrupciones absurdas."
            ),
        },
        "treatment": {
            "decision": "Desbloqueo Mental",
            "decision_explanation": (
                "Identificar frenos mentales que bloquean productividad."
            ),
            "action": "Detectar los 3 frenos más comunes en el equipo",
            "action_explanation": (
                "Elimina hábitos improductivos y acelera flujo de trabajo."
            ),
            "tool": "Cuestionario de Creencias Limitantes",
            "tool_explanation": (
                "Evalúa patrones de pensamiento que generan bloqueo."
            ),
        },
        "master_treatment": {
            "decision": "Reprogramación Cognitiva",
            "decision_explanation": (
                "Rediseñar hábitos mentales que frenan productividad."
            ),
            "action": "Diagnóstico de bloqueos y reentrenamiento",
            "action_explanation": (
                "Elimina patrones improductivos a nivel profundo."
            ),
            "tool": "Cuestionario Avanzado de Creencias",
            "tool_explanation": (
                "Herramienta de diagnóstico psicológico y conductual."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S2
    # ---------------------------------------------------------
    "PSI-S2": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Construir equipos alineados según fortalezas naturales."
            ),
            "order": 62,
            "department": "ORGANIZACIONAL",
            "plan": "PIE",
            "code": "PSI-S2",
            "logic": (
                "Carga de Micro-decisiones: Medir el agotamiento por tener que decidir hasta el último detalle."
            ),
        },
        "treatment": {
            "decision": "Sincronización DISC",
            "decision_explanation": (
                "Asignar roles según fortalezas individuales."
            ),
            "action": "Test de perfil conductual en puestos clave",
            "action_explanation": (
                "Potencia talento natural y reduce conflictos."
            ),
            "tool": "Matriz de Perfiles DISC",
            "tool_explanation": (
                "Muestra la alineación entre persona y puesto."
            ),
        },
        "master_treatment": {
            "decision": "Optimización de Roles",
            "decision_explanation": (
                "Maximizar rendimiento asignando roles según talento."
            ),
            "action": "Reasignación estratégica basada en perfiles DISC",
            "action_explanation": (
                "Aumenta eficacia y reduce fricción."
            ),
            "tool": "Matriz Estratégica DISC",
            "tool_explanation": (
                "Visualiza la compatibilidad rol-persona."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S3
    # ---------------------------------------------------------
    "PSI-S3": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Activar motivación intrínseca y comunicación sana."
            ),
            "order": 63,
            "department": "ORGANIZACIONAL",
            "plan": "PIE",
            "code": "PSI-S3",
            "logic": (
                "Calidad de la Comunicación: Medir si la información fluye o se estanca en 'corrillos'."
            ),
        },
        "treatment": {
            "decision": "Activación del Dopamina",
            "decision_explanation": (
                "Recuperar motivación intrínseca del equipo."
            ),
            "action": "Crear sistema de 'Quick Wins'",
            "action_explanation": (
                "Refuerza logros y engagement."
            ),
            "tool": "Plan de Reconocimiento Inmediato",
            "tool_explanation": (
                "Protocoliza recompensas rápidas y visibles."
            ),
        },
        "master_treatment": {
            "decision": "Motivación Sostenible",
            "decision_explanation": (
                "Activar motivación intrínseca permanente."
            ),
            "action": "Sistema de recompensas y logros visibles",
            "action_explanation": (
                "Incrementa compromiso y retención."
            ),
            "tool": "Plan Maestro de Reconocimiento",
            "tool_explanation": (
                "Estandariza reconocimiento continuo."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S4
    # ---------------------------------------------------------
    "PSI-S4": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Alinear liderazgo y eliminar contradicciones."
            ),
            "order": 64,
            "department": "ORGANIZACIONAL",
            "plan": "PRE",
            "code": "PSI-S4",
            "logic": (
                "Entropía en Reuniones: Medir la energía que se pierde en reuniones sin orden del día."
            ),
        },
        "treatment": {
            "decision": "Coherencia de Mando",
            "decision_explanation": (
                "Alinear mensajes y acciones de liderazgo."
            ),
            "action": "Auditoría de contradicciones en cadena de mando",
            "action_explanation": (
                "Evita mensajes contradictorios y mejora claridad."
            ),
            "tool": "Test de Coherencia de Liderazgo",
            "tool_explanation": (
                "Diagnóstico de consistencia en liderazgo."
            ),
        },
        "master_treatment": {
            "decision": "Gobernanza del Mando",
            "decision_explanation": (
                "Asegurar coherencia y predictibilidad del liderazgo."
            ),
            "action": "Protocolizar comunicación y decisiones",
            "action_explanation": (
                "Reduce incertidumbre y mejora alineación."
            ),
            "tool": "Dashboard de Liderazgo",
            "tool_explanation": (
                "Monitoriza consistencia y decisiones de líderes."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S5
    # ---------------------------------------------------------
    "PSI-S5": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Restaurar energía emocional y resiliencia."
            ),
            "order": 65,
            "department": "ORGANIZACIONAL",
            "plan": "PRE",
            "code": "PSI-S5",
            "logic": (
                "Índice de Reconocimiento: Saber si el equipo se mueve por miedo o por logro."
            ),
        },
        "treatment": {
            "decision": "Resiliencia Organizativa",
            "decision_explanation": (
                "Restaurar energía tras situaciones críticas."
            ),
            "action": "Sesiones de ventilación y enfoque a futuro",
            "action_explanation": (
                "Reduce estrés y evita rotación voluntaria."
            ),
            "tool": "Protocolo de Gestión de Crisis Emocional",
            "tool_explanation": (
                "Guía para recuperación rápida del equipo."
            ),
        },
        "master_treatment": {
            "decision": "Recuperación Activa",
            "decision_explanation": (
                "Restaurar resiliencia del equipo."
            ),
            "action": "Implementación de sesiones estructuradas post-crisis",
            "action_explanation": (
                "Minimiza impacto emocional y operativo."
            ),
            "tool": "Protocolo Integral de Crisis",
            "tool_explanation": (
                "Plan de acción para recuperación emocional."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S6
    # ---------------------------------------------------------
    "PSI-S6": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Convertir valores en conductas observables."
            ),
            "order": 66,
            "department": "ORGANIZACIONAL",
            "plan": "PRE",
            "code": "PSI-S6",
            "logic": (
                "Seguridad Psicológica: Medir si el equipo se atreve a proponer o tiene miedo al error."
            ),
        },
        "treatment": {
            "decision": "Encarnación de Cultura",
            "decision_explanation": (
                "Hacer tangibles los valores de la empresa."
            ),
            "action": "Traducir valores en 3 conductas prohibidas y 3 premiadas",
            "action_explanation": (
                "Refuerza cultura deseada y conducta correcta."
            ),
            "tool": "Código de Conducta Consciente",
            "tool_explanation": (
                "Manual de valores aplicado al día a día."
            ),
        },
        "master_treatment": {
            "decision": "Cultura Tangible",
            "decision_explanation": (
                "Convertir valores en acciones observables."
            ),
            "action": "Integración de valores en KPI y conducta",
            "action_explanation": (
                "Facilita adopción y seguimiento."
            ),
            "tool": "Código de Conducta Estratégico",
            "tool_explanation": (
                "Transformación de valores en práctica diaria."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S7
    # ---------------------------------------------------------
    "PSI-S7": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Mejorar comunicación interna y reducir reprocesos."
            ),
            "order": 67,
            "department": "ORGANIZACIONAL",
            "plan": "PRE",
            "code": "PSI-S7",
            "logic": (
                "Drenaje por Re-procesos: Medir la frustración de tener que hacer lo mismo dos veces."
            ),
        },
        "treatment": {
            "decision": "Asertividad Radical",
            "decision_explanation": (
                "Hablar claro sin generar conflictos."
            ),
            "action": "Formación en comunicación no violenta y feedback directo",
            "action_explanation": (
                "Mejora interacción y reduce frustración."
            ),
            "tool": "Guía de Feedback MASESORA",
            "tool_explanation": (
                "Herramienta para conversaciones difíciles."
            ),
        },
        "master_treatment": {
            "decision": "Claridad Radical",
            "decision_explanation": (
                "Mejorar comunicación interna efectiva."
            ),
            "action": "Talleres y simulaciones de feedback",
            "action_explanation": (
                "Eleva nivel de interacción y reduce malentendidos."
            ),
            "tool": "Kit de Comunicación Efectiva",
            "tool_explanation": (
                "Herramienta de entrenamiento y seguimiento."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S8
    # ---------------------------------------------------------
    "PSI-S8": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Alinear propósito personal y empresarial."
            ),
            "order": 68,
            "department": "ORGANIZACIONAL",
            "plan": "PRE",
            "code": "PSI-S8",
            "logic": (
                "Autonomía de Emergencia: ¿Sabe el equipo qué hacer si el dueño no está localizable?"
            ),
        },
        "treatment": {
            "decision": "Propósito Conectado",
            "decision_explanation": (
                "Vincular objetivos personales con empresariales."
            ),
            "action": "Taller de alineación de propósito",
            "action_explanation": (
                "Incrementa sentido de pertenencia y motivación."
            ),
            "tool": "Manifiesto del Propósito",
            "tool_explanation": (
                "Documento de referencia de propósito alineado."
            ),
        },
        "master_treatment": {
            "decision": "Propósito Compartido",
            "decision_explanation": (
                "Alinear propósito personal con el empresarial."
            ),
            "action": "Taller de alineación estratégica",
            "action_explanation": (
                "Incrementa engagement y motivación."
            ),
            "tool": "Manifiesto de Propósito Estratégico",
            "tool_explanation": (
                "Documento maestro de alineación cultural."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S9
    # ---------------------------------------------------------
    "PSI-S9": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Promover colaboración real entre áreas."
            ),
            "order": 69,
            "department": "ORGANIZACIONAL",
            "plan": "PRE",
            "code": "PSI-S9",
            "logic": (
                "Clima de Cooperación: Medir si los departamentos colaboran o compiten entre sí."
            ),
        },
        "treatment": {
            "decision": "Humildad Organizativa",
            "decision_explanation": (
                "Fomentar colaboración real."
            ),
            "action": "Implementar proyectos transversales",
            "action_explanation": (
                "Elimina competencia interna y promueve cooperación."
            ),
            "tool": "Matriz de Colaboración Cruzada",
            "tool_explanation": (
                "Herramienta para visualizar y medir sinergias."
            ),
        },
        "master_treatment": {
            "decision": "Sinergia Organizacional",
            "decision_explanation": (
                "Promover colaboración y eliminar reinos de taifas."
            ),
            "action": "Proyectos interdepartamentales con objetivos claros",
            "action_explanation": (
                "Fortalece colaboración y eficiencia."
            ),
            "tool": "Matriz de Colaboración Estratégica",
            "tool_explanation": (
                "Visualiza impacto y resultados de sinergias."
            ),
        },
    },

    # ---------------------------------------------------------
    # PSIQUIATRÍA ORGANIZACIONAL — S10
    # ---------------------------------------------------------
    "PSI-S10": {
        "meta": {
            "specialty": "PSIQUIATRÍA ORGANIZACIONAL",
            "description": (
                "Es la unidad que trabaja la mente y la cultura de la empresa."
            ),
            "strategic_objective": (
                "Mantener niveles óptimos de energía y compromiso."
            ),
            "order": 70,
            "department": "ORGANIZACIONAL",
            "plan": "PRE",
            "code": "PSI-S10",
            "logic": (
                "Sello de Vitalidad: Medir el nivel de energía al final de la semana."
            ),
        },
        "treatment": {
            "decision": "Alineación de Talento",
            "decision_explanation": (
                "Que cada rol tenga energía y claridad."
            ),
            "action": "Vincular perfil psicológico con responsabilidad",
            "action_explanation": (
                "Optimiza asignación y reduce desgaste."
            ),
            "tool": "Manifiesto del Propósito S10",
            "tool_explanation": (
                "Estándar de alineación de energía, propósito y rol."
            ),
        },
        "master_treatment": {
            "decision": "Vitalidad Estratégica",
            "decision_explanation": (
                "Mantener niveles óptimos de energía y compromiso."
            ),
            "action": "Vinculación de energía, propósito y rol",
            "action_explanation": (
                "Garantiza sostenibilidad y desempeño alto."
            ),
            "tool": "Dashboard de Talento y Propósito",
            "tool_explanation": (
                "Herramienta para seguimiento integral de energía y motivación."
            ),
        },
    },
    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S1
    # ---------------------------------------------------------
    "RES-S1": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño, este protocolo asegura que la empresa crezca "
                "con estructuras sólidas, evitando 'crecimientos enfermos' que generan caos o fragilidad. Es el tratamiento "
                "que convierte la expansión en un proceso sano, sostenible y estructurado."
            ),
            "strategic_objective": (
                "Garantizar que la empresa no solo aumente ventas o tamaño, sino que lo haga de forma sana, sostenible "
                "y coherente, preservando cultura, eficiencia y propósito mientras escala."
            ),
            "order": 71,
            "department": "PERSONAS",
            "plan": "PIE",
            "code": "RES-S1",
            "logic": (
                "Densidad de Talento: ¿Tienes estrellas o solo ocupas sillas?"
            ),
        },
        "treatment": {
            "decision": "Blindaje de Clave",
            "decision_explanation": (
                "Retener a empleados que realmente suman."
            ),
            "action": "Entrevistas de fidelización con perfiles A",
            "action_explanation": (
                "Asegura continuidad de conocimiento crítico y alto desempeño."
            ),
            "tool": "Mapa de Talento (Matriz 9-Box)",
            "tool_explanation": (
                "Visualiza talento vs. potencial para priorizar retención."
            ),
        },
        "master_treatment": {
            "decision": "Retención Estratégica",
            "decision_explanation": (
                "Mantener los A-Players críticos."
            ),
            "action": "Estrategia de fidelización personalizada",
            "action_explanation": (
                "Garantiza continuidad y crecimiento sostenido."
            ),
            "tool": "Mapa Estratégico de Talento 9-Box",
            "tool_explanation": (
                "Prioriza recursos y esfuerzos de retención."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S2
    # ---------------------------------------------------------
    "RES-S2": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Escalar con claridad de rol y contribución."
            ),
            "order": 72,
            "department": "PERSONAS",
            "plan": "PIE",
            "code": "RES-S2",
            "logic": (
                "Onboarding: Tiempo para que un nuevo sea rentable."
            ),
        },
        "treatment": {
            "decision": "Alineación de Objetivos",
            "decision_explanation": (
                "Que cada puesto tenga metas claras y medibles."
            ),
            "action": "Definir 3 objetivos clave por puesto",
            "action_explanation": (
                "Reduce tiempo perdido y acelera curva de adaptación."
            ),
            "tool": "Cuadro de Mandos Operativo",
            "tool_explanation": (
                "Herramienta de seguimiento de objetivos individuales."
            ),
        },
        "master_treatment": {
            "decision": "Optimización de Rol",
            "decision_explanation": (
                "Cada persona contribuye al máximo."
            ),
            "action": "KPI claros + objetivos alineados",
            "action_explanation": (
                "Aumenta impacto de cada rol y reduce sobrecarga."
            ),
            "tool": "Dashboard de Desempeño Individual",
            "tool_explanation": (
                "Visualiza contribución y progreso."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S3
    # ---------------------------------------------------------
    "RES-S3": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Preservar cultura sana y evitar toxicidad."
            ),
            "order": 73,
            "department": "PERSONAS",
            "plan": "PIE",
            "code": "RES-S3",
            "logic": (
                "Polivalencia: Riesgo de 'persona-dependencia'."
            ),
        },
        "treatment": {
            "decision": "Saneamiento Cultural",
            "decision_explanation": (
                "Cortar comportamientos negativos antes de que se propaguen."
            ),
            "action": "Encuesta de clima rápida y anónima",
            "action_explanation": (
                "Detecta focos de conflicto y permite acción inmediata."
            ),
            "tool": "eNPS (Employee NPS)",
            "tool_explanation": (
                "Mide compromiso y satisfacción del equipo."
            ),
        },
        "master_treatment": {
            "decision": "Cultura Regenerativa",
            "decision_explanation": (
                "Mejorar engagement y cohesión."
            ),
            "action": "Acciones inmediatas de ajuste cultural",
            "action_explanation": (
                "Reduce rotación y conflictos."
            ),
            "tool": "eNPS Avanzado + Feedback Continuo",
            "tool_explanation": (
                "Mide evolución y compromiso en tiempo real."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S4
    # ---------------------------------------------------------
    "RES-S4": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Reducir interrupciones al dueño y fortalecer mandos."
            ),
            "order": 74,
            "department": "PERSONAS",
            "plan": "PRE",
            "code": "RES-S4",
            "logic": (
                "Carga de Soporte: Interrupciones al dueño."
            ),
        },
        "treatment": {
            "decision": "Escuela de Mandos",
            "decision_explanation": (
                "Enseñar a delegar sin perder control."
            ),
            "action": "Formación en comunicación y reporte",
            "action_explanation": (
                "Reduce interrupciones al dueño y empodera mandos intermedios."
            ),
            "tool": "Protocolo de Delegación",
            "tool_explanation": (
                "Guía para delegar tareas manteniendo accountability."
            ),
        },
        "master_treatment": {
            "decision": "Delegación Inteligente",
            "decision_explanation": (
                "Empoderar mandos sin perder control."
            ),
            "action": "Formación en reporting y comunicación estratégica",
            "action_explanation": (
                "Optimiza tiempo del dueño y fortalece mandos intermedios."
            ),
            "tool": "Protocolo Dinámico de Delegación",
            "tool_explanation": (
                "Permite seguimiento y control remoto de tareas."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S5
    # ---------------------------------------------------------
    "RES-S5": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Contratar con criterio y fortalecer cultura."
            ),
            "order": 75,
            "department": "PERSONAS",
            "plan": "PRE",
            "code": "RES-S5",
            "logic": (
                "Accountability: ¿El equipo se siente dueño?"
            ),
        },
        "treatment": {
            "decision": "Protocolo de Fichaje",
            "decision_explanation": (
                "Contratar con criterio y no por urgencia."
            ),
            "action": "Definir 'Avatar de Empleado Ideal'",
            "action_explanation": (
                "Evita reincidencia de malos fichajes y fortalece cultura."
            ),
            "tool": "Scorecard de Reclutamiento",
            "tool_explanation": (
                "Evaluación estructurada de candidatos según perfil y potencial."
            ),
        },
        "master_treatment": {
            "decision": "Reclutamiento de Alto Impacto",
            "decision_explanation": (
                "Contratar para escalar."
            ),
            "action": "Definir perfil ideal + pruebas prácticas",
            "action_explanation": (
                "Reduce riesgo de malos fichajes y fortalece cultura."
            ),
            "tool": "Scorecard Predictivo",
            "tool_explanation": (
                "Priorización de candidatos según impacto esperado."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S6
    # ---------------------------------------------------------
    "RES-S6": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Alinear incentivos con desempeño real."
            ),
            "order": 76,
            "department": "PERSONAS",
            "plan": "PRE",
            "code": "RES-S6",
            "logic": (
                "Flexibilidad: Eficiencia del modelo de trabajo."
            ),
        },
        "treatment": {
            "decision": "Equidad Salarial",
            "decision_explanation": (
                "Ajustar incentivos a resultados y roles."
            ),
            "action": "Diseño de bonus vinculados a resultados",
            "action_explanation": (
                "Alinea motivación con desempeño y reduce frustración."
            ),
            "tool": "Plan de Incentivos",
            "tool_explanation": (
                "Estructura de compensación vinculada a KPIs y objetivos."
            ),
        },
        "master_treatment": {
            "decision": "Incentivos Estratégicos",
            "decision_explanation": (
                "Vincular rendimiento y compensación."
            ),
            "action": "Bonus ligados a resultados + objetivos estratégicos",
            "action_explanation": (
                "Alinea motivación con KPIs y estrategia de empresa."
            ),
            "tool": "Plan Maestro de Incentivos",
            "tool_explanation": (
                "Seguimiento y ajuste en tiempo real según desempeño."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S7
    # ---------------------------------------------------------
    "RES-S7": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Mantener habilidades actualizadas y evitar obsolescencia."
            ),
            "order": 77,
            "department": "PERSONAS",
            "plan": "PRE",
            "code": "RES-S7",
            "logic": (
                "Iniciativa: ¿El equipo empuja el coche?"
            ),
        },
        "treatment": {
            "decision": "Plan de Formación",
            "decision_explanation": (
                "Evitar obsolescencia del equipo."
            ),
            "action": "Detección de necesidades técnicas y formación continua",
            "action_explanation": (
                "Mejora habilidades y permite adaptación constante."
            ),
            "tool": "Matriz de Capacitación",
            "tool_explanation": (
                "Herramienta de seguimiento y planificación de desarrollo."
            ),
        },
        "master_treatment": {
            "decision": "Formación Continua",
            "decision_explanation": (
                "Mantener habilidades actualizadas."
            ),
            "action": "Capacitación planificada y seguimiento",
            "action_explanation": (
                "Garantiza adaptación y crecimiento constante."
            ),
            "tool": "Matriz Avanzada de Capacitación",
            "tool_explanation": (
                "Prioriza formación según impacto estratégico."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S8
    # ---------------------------------------------------------
    "RES-S8": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Blindar continuidad operativa ante ausencias."
            ),
            "order": 78,
            "department": "PERSONAS",
            "plan": "PRE",
            "code": "RES-S8",
            "logic": (
                "Fricción: Tiempo perdido por sistemas lentos."
            ),
        },
        "treatment": {
            "decision": "Plan de Sucesión",
            "decision_explanation": (
                "Garantizar continuidad ante ausencias."
            ),
            "action": "Identificar sustitutos críticos",
            "action_explanation": (
                "Evita dependencia de personas clave."
            ),
            "tool": "Mapa de Relevo Crítico",
            "tool_explanation": (
                "Visualiza roles críticos y planes de contingencia."
            ),
        },
        "master_treatment": {
            "decision": "Sucesión Proactiva",
            "decision_explanation": (
                "Blindar la empresa frente a ausencias."
            ),
            "action": "Identificar y preparar sustitutos",
            "action_explanation": (
                "Permite escalabilidad sin riesgo."
            ),
            "tool": "Mapa Estratégico de Relevo",
            "tool_explanation": (
                "Visualiza plan de sucesión y niveles de criticidad."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S9
    # ---------------------------------------------------------
    "RES-S9": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Ajustar estructura a crecimiento real."
            ),
            "order": 79,
            "department": "PERSONAS",
            "plan": "PRE",
            "code": "RES-S9",
            "logic": (
                "Coherencia DISC: Perfil adecuado en puesto adecuado."
            ),
        },
        "treatment": {
            "decision": "Estructura Flexible",
            "decision_explanation": (
                "Ajustar perfiles al rol natural."
            ),
            "action": "Simplificar organigrama y alinear roles",
            "action_explanation": (
                "Aumenta eficiencia y agilidad operativa."
            ),
            "tool": "Organigrama Circular",
            "tool_explanation": (
                "Representación dinámica de la estructura y flujos."
            ),
        },
        "master_treatment": {
            "decision": "Adaptabilidad Organizativa",
            "decision_explanation": (
                "Ajustar estructura a crecimiento."
            ),
            "action": "Reorganización por roles y procesos críticos",
            "action_explanation": (
                "Facilita expansión ágil y reducción de cuellos de botella."
            ),
            "tool": "Organigrama Dinámico Circular",
            "tool_explanation": (
                "Herramienta de modelado flexible para crecimiento."
            ),
        },
    },

    # ---------------------------------------------------------
    # RESCATE DE PERSONAS — S10
    # ---------------------------------------------------------
    "RES-S10": {
        "meta": {
            "specialty": "RESCATE DEPERSONAS",
            "description": (
                "Igual que la pediatría acompaña el desarrollo de un niño."
            ),
            "strategic_objective": (
                "Escalar sin perder eficiencia ni cultura."
            ),
            "order": 80,
            "department": "PERSONAS",
            "plan": "PRE",
            "code": "RES-S10",
            "logic": (
                "Escalabilidad: ¿Crecer drena o suma valor?"
            ),
        },
        "treatment": {
            "decision": "Integración Acelerada",
            "decision_explanation": (
                "Que nuevos rindan rápido sin depender del dueño."
            ),
            "action": "Manual de onboarding + auditoría de procesos",
            "action_explanation": (
                "Reduce curva de aprendizaje y errores iniciales."
            ),
            "tool": "Protocolo de Onboarding",
            "tool_explanation": (
                "Estandariza incorporación y entrega de conocimiento."
            ),
        },
        "master_treatment": {
            "decision": "Integración Sostenible",
            "decision_explanation": (
                "Nuevos operan al 100% rápidamente."
            ),
            "action": "Onboarding + auditoría + mentoring",
            "action_explanation": (
                "Acelera contribución y reduce dependencia del dueño."
            ),
            "tool": "Protocolo Integral de Onboarding",
            "tool_explanation": (
                "Estandariza incorporación con resultados medibles."
            ),
        },
    },
    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S1
    # ---------------------------------------------------------
    "TER-S1": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad, este protocolo transforma la marca "
                "empresarial para elevar la experiencia del cliente, fidelizar y consolidar la reputación. Es el tratamiento "
                "que asegura que la empresa proyecte hacia fuera la misma salud que ya ha alcanzado internamente, evaluando "
                "además si la digitalización aporta valor o complica el negocio."
            ),
            "strategic_objective": (
                "Optimizar la percepción externa de la empresa, fortalecer la fidelización y posicionarla como referente "
                "en su sector y comunidad, integrando digitalización solo cuando sea conveniente y sostenible."
            ),
            "order": 81,
            "department": "EXPERIENCIA",
            "plan": "PIE",
            "code": "TER-S1",
            "logic": (
                "Calidez Híbrida: ¿La bienvenida es igual de humana en la puerta que en el chat?"
            ),
        },
        "treatment": {
            "decision": "Estructuración de Base",
            "decision_explanation": (
                "Evitar que el crecimiento rompa la experiencia."
            ),
            "action": "Auditoría de procesos vs. carga nueva",
            "action_explanation": (
                "Detecta puntos críticos que colapsan con más ventas."
            ),
            "tool": "Test de Estrés de Crecimiento",
            "tool_explanation": (
                "Simula la capacidad operativa y visualiza cuellos de botella."
            ),
        },
        "master_treatment": {
            "decision": "Escalabilidad Experta",
            "decision_explanation": (
                "Crecer sin romper experiencia."
            ),
            "action": "Auditoría operativa + simulación de crecimiento",
            "action_explanation": (
                "Garantiza que la experiencia se mantenga con mayores volúmenes."
            ),
            "tool": "Simulación de Estrés Operativo",
            "tool_explanation": (
                "Modela impacto de incremento de clientes y procesos."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S2
    # ---------------------------------------------------------
    "TER-S2": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Mantener ADN y valores intactos en cada interacción."
            ),
            "order": 82,
            "department": "EXPERIENCIA",
            "plan": "PIE",
            "code": "TER-S2",
            "logic": (
                "Onboarding Omnicanal: ¿Sabe qué hacer tras pagar (ticket físico o email de confirmación)?"
            ),
        },
        "treatment": {
            "decision": "Protección de Esencia",
            "decision_explanation": (
                "Mantener ADN y valores intactos."
            ),
            "action": "Manual de bienvenida y valores",
            "action_explanation": (
                "Asegura coherencia de experiencia y cultura."
            ),
            "tool": "Onboarding de Cultura",
            "tool_explanation": (
                "Documento de integración de nuevos clientes/empleados según valores."
            ),
        },
        "master_treatment": {
            "decision": "Cultura Cohesiva",
            "decision_explanation": (
                "Integrar valores en cada interacción."
            ),
            "action": "Onboarding omnicanal de clientes y equipo",
            "action_explanation": (
                "Refuerza coherencia de marca y experiencia."
            ),
            "tool": "Playbook de Cultura",
            "tool_explanation": (
                "Manual de aplicación práctica de valores en todos los canales."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S3
    # ---------------------------------------------------------
    "TER-S3": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Preparar operación para crecer sin colapsar."
            ),
            "order": 83,
            "department": "EXPERIENCIA",
            "plan": "PIE",
            "code": "TER-S3",
            "logic": (
                "Ratio de Impacto: Capacidad de generar un agradecimiento espontáneo (reseña o verbal)."
            ),
        },
        "treatment": {
            "decision": "Refuerzo de Cimientos",
            "decision_explanation": (
                "Preparar la operación antes de crecer."
            ),
            "action": "Identificar puestos críticos ante aumento de ventas",
            "action_explanation": (
                "Garantiza continuidad sin sobrecarga de personal."
            ),
            "tool": "Mapa de Nodos Críticos",
            "tool_explanation": (
                "Visualiza roles y procesos clave que podrían colapsar."
            ),
        },
        "master_treatment": {
            "decision": "Resiliencia de Procesos",
            "decision_explanation": (
                "Preparar estructura para picos de demanda."
            ),
            "action": "Identificación y refuerzo de nodos críticos",
            "action_explanation": (
                "Reduce riesgo de quiebres operativos."
            ),
            "tool": "Mapa Estratégico de Nodos",
            "tool_explanation": (
                "Visualización de procesos y roles clave con impacto estratégico."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S4
    # ---------------------------------------------------------
    "TER-S4": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Maximizar margen sin comprometer experiencia."
            ),
            "order": 84,
            "department": "EXPERIENCIA",
            "plan": "PRE",
            "code": "TER-S4",
            "logic": (
                "Tasa de Dolor: Fricción en el proceso (ej. cola en local o fallo en web)."
            ),
        },
        "treatment": {
            "decision": "Rentabilidad en Escala",
            "decision_explanation": (
                "No vender más, vender mejor."
            ),
            "action": "Análisis costes variables en expansión",
            "action_explanation": (
                "Maximiza margen sin comprometer experiencia."
            ),
            "tool": "Matriz de Escala Rentable",
            "tool_explanation": (
                "Evalúa impacto económico de cada unidad de crecimiento."
            ),
        },
        "master_treatment": {
            "decision": "Rentabilidad Inteligente",
            "decision_explanation": (
                "Optimizar ganancias sin sacrificar experiencia."
            ),
            "action": "Optimización de costes vs. experiencia",
            "action_explanation": (
                "Mantiene margen y satisfacción del cliente."
            ),
            "tool": "Matriz de Escala Rentable Avanzada",
            "tool_explanation": (
                "Permite decisiones de expansión basadas en ROI real."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S5
    # ---------------------------------------------------------
    "TER-S5": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Supervisar experiencia sin presencia física."
            ),
            "order": 85,
            "department": "EXPERIENCIA",
            "plan": "PRE",
            "code": "TER-S5",
            "logic": (
                "Cuidado Proactivo: Seguimiento post-venta por el canal preferido del cliente."
            ),
        },
        "treatment": {
            "decision": "Gobierno Remoto",
            "decision_explanation": (
                "Gestionar sin presencia física."
            ),
            "action": "Cuadros de mando por sede/equipo",
            "action_explanation": (
                "Permite supervisión de experiencia desde cualquier lugar."
            ),
            "tool": "Dashboard de Expansión",
            "tool_explanation": (
                "Seguimiento centralizado de KPIs de experiencia y ventas."
            ),
        },
        "master_treatment": {
            "decision": "Gestión Autónoma",
            "decision_explanation": (
                "Supervisar sin depender de presencia."
            ),
            "action": "Dashboards integrales y alertas",
            "action_explanation": (
                "Mantiene control de experiencia y KPIs críticos."
            ),
            "tool": "Cuadro de Mando Omnicanal",
            "tool_explanation": (
                "Integración total de canales y sedes con métricas unificadas."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S6
    # ---------------------------------------------------------
    "TER-S6": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Mantener ventaja competitiva sostenible."
            ),
            "order": 86,
            "department": "EXPERIENCIA",
            "plan": "PRE",
            "code": "TER-S6",
            "logic": (
                "Efecto Sorpresa: Detalles físicos para clientes online o cupones digitales para locales."
            ),
        },
        "treatment": {
            "decision": "Vigilancia de Mercado",
            "decision_explanation": (
                "Mantener ventaja competitiva."
            ),
            "action": "Análisis tendencias y competidores",
            "action_explanation": (
                "Detecta oportunidades de innovación antes que otros."
            ),
            "tool": "Radar de Innovación",
            "tool_explanation": (
                "Herramienta de monitoreo de mercado y tendencias."
            ),
        },
        "master_treatment": {
            "decision": "Innovación Constante",
            "decision_explanation": (
                "Mantener ventaja competitiva sostenible."
            ),
            "action": "Análisis de tendencias y benchmarks",
            "action_explanation": (
                "Permite anticipar cambios del mercado."
            ),
            "tool": "Radar Estratégico de Innovación",
            "tool_explanation": (
                "Identifica oportunidades de mejora y diferenciación."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S7
    # ---------------------------------------------------------
    "TER-S7": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Eliminar fricciones y burocracia innecesaria."
            ),
            "order": 87,
            "department": "EXPERIENCIA",
            "plan": "PRE",
            "code": "TER-S7",
            "logic": (
                "Rescate Omnicanal: Velocidad para solucionar un problema sin importar dónde nació."
            ),
        },
        "treatment": {
            "decision": "Simplificación Radical",
            "decision_explanation": (
                "Reducir burocracia creada por crecimiento."
            ),
            "action": "Eliminar pasos innecesarios",
            "action_explanation": (
                "Flujo más rápido y simple para el cliente."
            ),
            "tool": "Protocolo de Simplificación",
            "tool_explanation": (
                "Guía para eliminar fricciones en procesos."
            ),
        },
        "master_treatment": {
            "decision": "Flujo Simplificado",
            "decision_explanation": (
                "Reducir pasos que no aportan valor."
            ),
            "action": "Reingeniería de procesos críticos",
            "action_explanation": (
                "Experiencia más rápida y fluida para clientes."
            ),
            "tool": "Protocolo de Simplificación Avanzado",
            "tool_explanation": (
                "Guía de eliminación de fricciones y redundancias."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S8
    # ---------------------------------------------------------
    "TER-S8": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Preparar la empresa para el relevo."
            ),
            "order": 88,
            "department": "EXPERIENCIA",
            "plan": "PRE",
            "code": "TER-S8",
            "logic": (
                "Escucha Activa: ¿Las sugerencias (buzón o comentarios rrss) llegan a implementarse?"
            ),
        },
        "treatment": {
            "decision": "Continuidad del Legado",
            "decision_explanation": (
                "Preparar la empresa para el relevo."
            ),
            "action": "Formar 'herederos de gestión'",
            "action_explanation": (
                "Asegura operación sin dependencia de fundadores."
            ),
            "tool": "Plan de Sucesión Sostenible",
            "tool_explanation": (
                "Define roles y capacitación de sucesores."
            ),
        },
        "master_treatment": {
            "decision": "Relevo Estratégico",
            "decision_explanation": (
                "Preparar la próxima generación de líderes."
            ),
            "action": "Programa de desarrollo de sucesores",
            "action_explanation": (
                "Garantiza continuidad operativa sin pérdida de calidad."
            ),
            "tool": "Plan Integral de Sucesión",
            "tool_explanation": (
                "Define roles, capacitación y seguimiento de sucesores."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S9
    # ---------------------------------------------------------
    "TER-S9": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Escalar sin perder know-how."
            ),
            "order": 89,
            "department": "EXPERIENCIA",
            "plan": "PRE",
            "code": "TER-S9",
            "logic": (
                "Ratio de Fidelidad: El cliente que compra en tienda y también pide por la web."
            ),
        },
        "treatment": {
            "decision": "Gestión del Activo Intelectual",
            "decision_explanation": (
                "Retener conocimiento crítico."
            ),
            "action": "Documentar procesos y saber hacer",
            "action_explanation": (
                "Permite replicar procesos y escalar sin pérdida de know-how."
            ),
            "tool": "Wiki / Manual de Activos",
            "tool_explanation": (
                "Centraliza información clave y protocolos."
            ),
        },
        "master_treatment": {
            "decision": "Protección del Know-how",
            "decision_explanation": (
                "Documentar todo conocimiento crítico."
            ),
            "action": "Sistema centralizado de gestión de activos",
            "action_explanation": (
                "Escalabilidad sin pérdida de información."
            ),
            "tool": "Wiki Estratégico / Manual Maestro",
            "tool_explanation": (
                "Repositorio vivo y actualizado de procesos y buenas prácticas."
            ),
        },
    },

    # ---------------------------------------------------------
    # TERAPIA DE EXPERIENCIA — S10
    # ---------------------------------------------------------
    "TER-S10": {
        "meta": {
            "specialty": "TERAPIA DE EXPERIENCIA",
            "description": (
                "Igual que la cirugía estética mejora la apariencia y funcionalidad."
            ),
            "strategic_objective": (
                "Consolidar comunidad, coherencia y reputación."
            ),
            "order": 90,
            "department": "EXPERIENCIA",
            "plan": "PRE",
            "code": "TER-S10",
            "logic": (
                "Sello Experiencia: Ventas que vienen por el boca a boca (físico) o etiqueta (digital)."
            ),
        },
        "treatment": {
            "decision": "Alineación de Coherencia",
            "decision_explanation": (
                "Consolidar la comunidad y fidelización."
            ),
            "action": "Revisión trimestral de valores e hitos",
            "action_explanation": (
                "Mantiene experiencia consistente y medible."
            ),
            "tool": "Brújula de Coherencia S10",
            "tool_explanation": (
                "Seguimiento de la coherencia entre estrategia y experiencia."
            ),
        },
        "master_treatment": {
            "decision": "Experiencia Sello",
            "decision_explanation": (
                "Transformar clientes en promotores activos."
            ),
            "action": "Revisión de valores y consolidación de comunidad",
            "action_explanation": (
                "Mantiene coherencia y reputación de marca."
            ),
            "tool": "Brújula de Coherencia Estratégica",
            "tool_explanation": (
                "Herramienta de seguimiento y ajuste de experiencia a largo plazo."
            ),
        },
    },
    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S1
    # ---------------------------------------------------------
    "OPE-S1": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos, "
                "eliminando errores, desperdicios y fricciones, y liberando al equipo y al dueño para centrarse en "
                "generar valor real."
            ),
            "strategic_objective": (
                "Maximizar la eficiencia operativa, asegurar la continuidad del negocio, reducir costes ocultos y "
                "lograr que la empresa funcione perfectamente incluso sin la presencia del dueño."
            ),
            "order": 91,
            "department": "EXCELENCIA",
            "plan": "PIE",
            "code": "OPE-S1",
            "logic": (
                "Antifragilidad Operativa: Medir si el sistema aprende solo de los errores."
            ),
        },
        "treatment": {
            "decision": "Mejorar sistema de aprendizaje",
            "decision_explanation": (
                "Convertir los errores en oportunidades de mejora continua."
            ),
            "action": "Implementar revisión post-incidencia",
            "action_explanation": (
                "Registrar, analizar y aplicar cambios tras cada fallo."
            ),
            "tool": "Registro de Incidencias",
            "tool_explanation": (
                "Documenta cada fallo y las mejoras aplicadas para aprendizaje sistemático."
            ),
        },
        "master_treatment": {
            "decision": "Activar aprendizaje automático",
            "decision_explanation": (
                "El sistema debe usar los errores para mejorar."
            ),
            "action": "Implementar seguimiento de incidencias",
            "action_explanation": (
                "Registrar y analizar fallos para ajustar procesos."
            ),
            "tool": "Sistema de Registro de Incidencias",
            "tool_explanation": (
                "Permite rastrear y aprender de cada error."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S2
    # ---------------------------------------------------------
    "OPE-S2": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Permitir que la empresa funcione sin supervisión constante."
            ),
            "order": 92,
            "department": "EXCELENCIA",
            "plan": "PIE",
            "code": "OPE-S2",
            "logic": (
                "Rendimiento Invisible: Eficiencia pura sin supervisión del líder."
            ),
        },
        "treatment": {
            "decision": "Fomentar autonomía del sistema",
            "decision_explanation": (
                "Permitir que la empresa funcione sin supervisión constante."
            ),
            "action": "Delegar y automatizar procesos críticos",
            "action_explanation": (
                "Identificar y transferir tareas repetitivas a procesos autónomos."
            ),
            "tool": "Dashboard de Autonomía",
            "tool_explanation": (
                "Permite medir cuánto del negocio funciona sin intervención del dueño."
            ),
        },
        "master_treatment": {
            "decision": "Autonomizar procesos",
            "decision_explanation": (
                "Reducir supervisión directa del líder."
            ),
            "action": "Delegar tareas críticas",
            "action_explanation": (
                "Que el equipo opere sin intervención constante."
            ),
            "tool": "Dashboard de Autonomía",
            "tool_explanation": (
                "Monitorea la ejecución de tareas sin depender del dueño."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S3
    # ---------------------------------------------------------
    "OPE-S3": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Garantizar experiencia uniforme entre online y offline."
            ),
            "order": 93,
            "department": "EXCELENCIA",
            "plan": "PIE",
            "code": "OPE-S3",
            "logic": (
                "Sincronía Híbrida: Medir la fricción entre el mundo físico (80%) y virtual (20%)."
            ),
        },
        "treatment": {
            "decision": "Sincronizar procesos físicos y digitales",
            "decision_explanation": (
                "Garantizar experiencia uniforme entre online y offline."
            ),
            "action": "Establecer protocolos de traspaso",
            "action_explanation": (
                "Crear flujos estandarizados entre web y local."
            ),
            "tool": "Checklist de Sincronía",
            "tool_explanation": (
                "Herramienta para validar la correcta transición entre canales."
            ),
        },
        "master_treatment": {
            "decision": "Sincronizar híbrido",
            "decision_explanation": (
                "Evitar errores al pasar de digital a físico."
            ),
            "action": "Revisar flujos híbridos",
            "action_explanation": (
                "Asegurar que las tareas se transfieran correctamente."
            ),
            "tool": "Mapa de Flujo Omnicanal",
            "tool_explanation": (
                "Visualiza y corrige los puntos de fricción entre canales."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S4
    # ---------------------------------------------------------
    "OPE-S4": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Eliminar reprocesos y asegurar entregas correctas a la primera."
            ),
            "order": 94,
            "department": "EXCELENCIA",
            "plan": "PRE",
            "code": "OPE-S4",
            "logic": (
                "Cero Desperdicio (Lean): Eliminar el re-trabajo por falta de claridad."
            ),
        },
        "treatment": {
            "decision": "Reducir desperdicio",
            "decision_explanation": (
                "Evitar errores por falta de claridad o instrucción."
            ),
            "action": "Implementar entregas First-Time",
            "action_explanation": (
                "Estandarizar procesos y controles para entregar correctamente a la primera."
            ),
            "tool": "Lean Workflow",
            "tool_explanation": (
                "Visualiza flujos y elimina pasos innecesarios para optimizar eficiencia."
            ),
        },
        "master_treatment": {
            "decision": "Cero desperdicio",
            "decision_explanation": (
                "Eliminar reprocesos innecesarios."
            ),
            "action": "Aplicar entregas First-Time",
            "action_explanation": (
                "Garantizar que el trabajo salga correcto a la primera."
            ),
            "tool": "Checklists Lean",
            "tool_explanation": (
                "Establece pasos claros para entregas perfectas."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S5
    # ---------------------------------------------------------
    "OPE-S5": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Absorber picos de demanda sin colapsar."
            ),
            "order": 95,
            "department": "EXCELENCIA",
            "plan": "PRE",
            "code": "OPE-S5",
            "logic": (
                "Velocidad de Escala: Tiempo en absorber un pico de demanda sin colapsar."
            ),
        },
        "treatment": {
            "decision": "Incrementar elasticidad operativa",
            "decision_explanation": (
                "Manejar aumentos de demanda sin colapsar."
            ),
            "action": "Ajustar recursos en picos",
            "action_explanation": (
                "Redistribuir personal y procesos para responder a demandas altas."
            ),
            "tool": "Plan de Escalabilidad",
            "tool_explanation": (
                "Simula escenarios de aumento de demanda y evalúa capacidad de respuesta."
            ),
        },
        "master_treatment": {
            "decision": "Elasticidad operativa",
            "decision_explanation": (
                "Absorber aumentos sin colapsar."
            ),
            "action": "Ajustar recursos y procesos",
            "action_explanation": (
                "Preparar sistemas para escalabilidad."
            ),
            "tool": "Indicadores de Elasticidad",
            "tool_explanation": (
                "Mide capacidad de respuesta frente a picos."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S6
    # ---------------------------------------------------------
    "OPE-S6": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Garantizar precisión y fiabilidad del suministro."
            ),
            "order": 96,
            "department": "EXCELENCIA",
            "plan": "PRE",
            "code": "OPE-S6",
            "logic": (
                "Precisión de Suministro: Garantizar que el 100% de la 'materia prima' es excelente."
            ),
        },
        "treatment": {
            "decision": "Mejorar precisión de suministro",
            "decision_explanation": (
                "Garantizar que los materiales lleguen completos y a tiempo."
            ),
            "action": "Validar proveedores y seguimiento",
            "action_explanation": (
                "Control estricto de entregas y cumplimiento de proveedores."
            ),
            "tool": "Control de Suministro",
            "tool_explanation": (
                "Registra y verifica la calidad y puntualidad de los proveedores."
            ),
        },
        "master_treatment": {
            "decision": "Control de calidad",
            "decision_explanation": (
                "Evitar que proveedores frenen la operación."
            ),
            "action": "Monitorizar entregas",
            "action_explanation": (
                "Detectar desviaciones y corregir rápidamente."
            ),
            "tool": "Panel de Suministro",
            "tool_explanation": (
                "Visualiza cumplimiento de proveedores en tiempo y forma."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S7
    # ---------------------------------------------------------
    "OPE-S7": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Fomentar innovación interna continua."
            ),
            "order": 97,
            "department": "EXCELENCIA",
            "plan": "PRE",
            "code": "OPE-S7",
            "logic": (
                "Cultura de Innovación: El equipo ya no solo opera, ahora crea."
            ),
        },
        "treatment": {
            "decision": "Fomentar cultura de innovación",
            "decision_explanation": (
                "Incentivar propuestas de mejora del equipo."
            ),
            "action": "Crear programa de ideas rentables",
            "action_explanation": (
                "Premiar y ejecutar ideas que aporten valor."
            ),
            "tool": "Mapa de Innovación",
            "tool_explanation": (
                "Herramienta para registrar ideas, evaluar impacto y seguimiento."
            ),
        },
        "master_treatment": {
            "decision": "Innovación interna",
            "decision_explanation": (
                "El equipo debe generar mejoras."
            ),
            "action": "Incentivar propuestas rentables",
            "action_explanation": (
                "Capturar ideas que aumenten beneficio."
            ),
            "tool": "Registro de Propuestas",
            "tool_explanation": (
                "Permite registrar, evaluar y medir ideas de la plantilla."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S8
    # ---------------------------------------------------------
    "OPE-S8": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Mantener know-how ante cambios de personal."
            ),
            "order": 98,
            "department": "EXCELENCIA",
            "plan": "PRE",
            "code": "OPE-S8",
            "logic": (
                "Blindaje de Calidad: Medir la robustez de los procesos ante cambios de personal."
            ),
        },
        "treatment": {
            "decision": "Blindar procesos críticos",
            "decision_explanation": (
                "Evitar pérdida de know-how por cambios de personal."
            ),
            "action": "Establecer backups de procesos",
            "action_explanation": (
                "Capacitar a varias personas en procesos clave."
            ),
            "tool": "Manual de Procesos",
            "tool_explanation": (
                "Documenta cada proceso vital para asegurar continuidad ante bajas."
            ),
        },
        "master_treatment": {
            "decision": "Blindaje de procesos",
            "decision_explanation": (
                "Mantener know-how ante cambios."
            ),
            "action": "Documentar procesos con backups",
            "action_explanation": (
                "Asegurar que varias personas dominan cada tarea."
            ),
            "tool": "Manual de Procesos Críticos",
            "tool_explanation": (
                "Respalda conocimiento clave de la empresa."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S9
    # ---------------------------------------------------------
    "OPE-S9": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Digitalizar tareas repetitivas para liberar tiempo estratégico."
            ),
            "order": 99,
            "department": "EXCELENCIA",
            "plan": "PRE",
            "code": "OPE-S9",
            "logic": (
                "Automatización Inteligente: Liberar al humano de lo que puede hacer un código."
            ),
        },
        "treatment": {
            "decision": "Digitalizar tareas",
            "decision_explanation": (
                "Liberar al humano para tareas estratégicas."
            ),
            "action": "Implementar automatización inteligente",
            "action_explanation": (
                "Software o scripts para tareas repetitivas."
            ),
            "tool": "Sistema de Automatización",
            "tool_explanation": (
                "Plataforma que permite programar, monitorizar y ejecutar tareas automáticas."
            ),
        },
        "master_treatment": {
            "decision": "Automatización inteligente",
            "decision_explanation": (
                "Liberar al humano de tareas sin valor."
            ),
            "action": "Implementar software/IA",
            "action_explanation": (
                "Digitalizar procesos repetitivos."
            ),
            "tool": "Plataforma de Automatización",
            "tool_explanation": (
                "Ejecuta tareas automáticamente, reduciendo errores y tiempo."
            ),
        },
    },

    # ---------------------------------------------------------
    # EXCELENCIA OPERATIVA — S10
    # ---------------------------------------------------------
    "OPE-S10": {
        "meta": {
            "specialty": "EXCELENCIA OPERATIVA",
            "description": (
                "Unidad que transforma los procesos de la empresa en sistemas inteligentes, robustos y autónomos."
            ),
            "strategic_objective": (
                "Validar que la empresa funciona mejor sin el dueño."
            ),
            "order": 100,
            "department": "EXCELENCIA",
            "plan": "PRE",
            "code": "OPE-S10",
            "logic": (
                "Sello S10 Excelencia: La empresa funciona mejor cuando el dueño no está."
            ),
        },
        "treatment": {
            "decision": "Validar que el negocio mantiene productividad",
            "decision_explanation": (
                "Que la empresa funcione perfectamente sin supervisión."
            ),
            "action": "Medir resultados en ausencia del dueño",
            "action_explanation": (
                "Comparar desempeño con y sin la presencia del dueño."
            ),
            "tool": "Panel de Performance Post-Dueño",
            "tool_explanation": (
                "Mide la autonomía operativa y la capacidad del negocio de generar valor sin intervención."
            ),
        },
        "master_treatment": {
            "decision": "Auditoría de Robustez Operativa",
            "decision_explanation": (
                "Comprobar la resistencia de procesos críticos frente a variaciones de operación."
            ),
            "action": "Testar sistemas y procesos ante escenarios límite",
            "action_explanation": (
                "Identifica puntos débiles y asegura continuidad operativa."
            ),
            "tool": "Checklist de Stress Test Operativo",
            "tool_explanation": (
                "Verifica que procesos críticos mantienen eficiencia y fiabilidad."
            ),
        },
    },
 }