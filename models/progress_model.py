# models/progress_model.py

class ProgressModel:
    """
    ProgressModel
    -------------
    Modelo mínimo para registrar el progreso clínico-operativo
    de un síntoma o tratamiento.

    No calcula.
    No interpreta.
    Solo almacena datos para que el orquestador pueda
    construir el informe final.
    """

    def __init__(
        self,
        code: str,
        kpi_before: float = None,
        kpi_after: float = None,
        impact: dict = None,
        treatment: dict = None,
        master_treatment: dict = None,
    ):
        self.code = code                    # Ej: "UNI-S3"
        self.kpi_before = kpi_before        # Valor inicial del KPI
        self.kpi_after = kpi_after          # Valor final del KPI
        self.impact = impact or {}          # Resultado del ImpactEngine
        self.treatment = treatment or {}    # Bloque treatment del catálogo
        self.master_treatment = master_treatment or {}  # Bloque master_treatment

    def to_dict(self) -> dict:
        """
        Devuelve el progreso en formato serializable.
        """
        return {
            "code": self.code,
            "kpi_before": self.kpi_before,
            "kpi_after": self.kpi_after,
            "impact": self.impact,
            "treatment": self.treatment,
            "master_treatment": self.master_treatment,
        }