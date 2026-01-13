from .treatment_map import TREATMENT_MAP

class TreatmentEngine:
    """
    TreatmentEngine
    ----------------
    Este engine recibe un código clínico (ej: 'UCI-S1', 'UNI-S4', 'CARDIO-S3')
    y devuelve el bloque completo del catálogo:

        - meta
        - treatment
        - master_treatment

    No interpreta.
    No modifica.
    No calcula.
    Solo entrega el bloque EXACTO del catálogo validado.
    """

    @staticmethod
    def get_treatment(code: str) -> dict:
        """
        Devuelve el tratamiento completo asociado al código.
        Si el código no existe, devuelve un error estructurado.
        """

        if code not in TREATMENT_MAP:
            return {
                "error": True,
                "message": f"Código clínico no encontrado: {code}",
                "available_codes": list(TREATMENT_MAP.keys())
            }

        # Devuelve EXACTAMENTE la estructura del catálogo
        data = TREATMENT_MAP[code]
        return {
            "error": False,
            "code": code,
            "meta": data.get("meta", {}),
            "treatment": data.get("treatment", {}),
            "master_treatment": data.get("master_treatment", {}),
        }