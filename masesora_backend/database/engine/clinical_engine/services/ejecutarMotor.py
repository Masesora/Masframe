from motores.calculadora_de_flujo import calculadora_de_flujo
from motores.matriz_universal import matriz_universal
from motores.dashboard_universal import dashboard_universal
from motores.scoring import sistema_scoring
from motores.checklist import checklist_dinamico
from motores.roadmap import roadmap_timeline
from motores.generador_docs import generador_docs

from herramientas.matriz_tesoreria import matriz_tesoreria
from herramientas.regla_5_25 import regla_5_25
from herramientas.escandallo_oro import escandallo_oro
from herramientas.presupuesto_cero import presupuesto_cero
from herramientas.dossier_bancario import dossier_bancario
from herramientas.integracion_crm import integracion_crm
from herramientas.automatizacion import automatizacion


def ejecutar_motor(tool_base, payload):
    """
    ejecuta el motor adecuado según tool_base.
    payload es un dict que puede contener:
      - inputs
      - formula / kpi_formula
      - thresholds
      - items / metricas / subkpis / pasos / acciones / contexto
      - motor_config (si lo usas)
    """

    # -------------------------
    # MOTORES
    # -------------------------

    if tool_base in ["CalculadoraKPIs", "CalculadoraDeFlujo"]:
        inputs = payload.get("inputs", {})
        formula = payload.get("kpi_formula") or payload.get("formula") or "(InputA / InputB)"
        thresholds = payload.get("thresholds", {})
        return calculadora_de_flujo(inputs, formula, thresholds)

    if tool_base == "MatrizUniversal":
        items = payload.get("items", [])
        config = payload.get("motor_config", {})
        return matriz_universal(items, config)

    if tool_base == "DashboardUniversal":
        metricas = payload.get("metricas", {})
        thresholds = payload.get("thresholds", {})
        return dashboard_universal(metricas, thresholds)

    if tool_base == "SistemaScoring":
        subkpis = payload.get("subkpis", {})
        pesos = payload.get("pesos", {})
        return sistema_scoring(subkpis, pesos)

    if tool_base == "ChecklistDinamico":
        pasos = payload.get("pasos", [])
        return checklist_dinamico(pasos)

    if tool_base == "RoadmapTimeline":
        acciones = payload.get("acciones", [])
        return roadmap_timeline(acciones)

    if tool_base == "GeneradorDocs":
        contexto = payload.get("contexto", {})
        template = payload.get("template", {})
        return generador_docs(contexto, template)

    # -------------------------
    # HERRAMIENTAS
    # -------------------------

    if tool_base == "MatrizTesoreria":
        return matriz_tesoreria(payload)

    if tool_base == "Regla5_25":
        return regla_5_25(payload.get("tareas", []))

    if tool_base == "EscandalloOro":
        return escandallo_oro(payload)

    if tool_base == "PresupuestoCero":
        return presupuesto_cero(payload.get("gastos", []))

    if tool_base == "DossierBancario":
        return dossier_bancario(payload)

    if tool_base == "IntegracionCRM":
        return integracion_crm(payload.get("clientes", []))

    if tool_base == "Automatizacion":
        return automatizacion(payload.get("procesos", []))

    # -------------------------
    # ERROR SI NO EXISTE MOTOR
    # -------------------------

    return {
        "error": "Motor no encontrado",
        "tool_base": tool_base
    }
    }