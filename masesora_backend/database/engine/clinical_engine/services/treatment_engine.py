import json
import os


class TreatmentEngine:
    """
    TreatmentEngine (versión unificada)
    ----------------------------------
    Ahora lee directamente desde symptoms.json.
    Devuelve el bloque clínico EXACTO asociado al código:

        - meta
        - treatment
        - master_treatment

    No interpreta.
    No modifica.
    No calcula.
    """

    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        symptoms_path = os.path.join(
            base_path,
            "..",
            "..",
            "..",
            "..",
            "data",
            "symptoms.json"
        )

        with open(symptoms_path, "r", encoding="utf-8") as f:
            self.catalog = json.load(f)

        # Indexar por symptom_id en lugar de id
        self.index = {item["symptom_id"]: item for item in self.catalog}

    def get_treatment(self, code: str) -> dict:
        if code not in self.index:
            return {
                "error": True,
                "message": f"Código clínico no encontrado: {code}",
                "available_codes": list(self.index.keys())
            }

        data = self.index[code]

        return {
            "error": False,
            "code": code,
            "meta": {
                "specialty": data.get("specialty"),
                "description": data.get("description_symptom"),
                "strategic_objective": data.get("kpi_impact"),
                "department": data.get("department"),
                "plan": data.get("plan"),
                "order": data.get("orden"),
                "logic": data.get("logica"),
            },
            "treatment": {
                "decision": data.get("optimizer_decision"),
                "decision_explanation": data.get("optimizer_decision_explanation"),
                "action": data.get("optimizer_action"),
                "action_explanation": data.get("impact_treatment"),
                "tool_explanation": data.get("optimizer_tool_explanation"),
            },
            "master_treatment": {
                "decision": data.get("capa_2_decision"),
                "decision_explanation": data.get("justi_capa2"),
                "action": data.get("capa_4_cambio"),
                "action_explanation": data.get("justi_capa4"),
                "tool": data.get("capa_3_comprension"),
                "tool_explanation": data.get("justi_capa3"),
            }
        }