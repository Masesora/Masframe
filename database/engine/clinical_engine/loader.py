import json
from pathlib import Path

# Ruta absoluta hasta /masesora_backend
# loader.py está en: masesora_backend/database/engine/clinical_engine/loader.py
# parents[0] = clinical_engine
# parents[1] = engine
# parents[2] = database
# parents[3] = masesora_backend  ✅
BASE_DIR = Path(__file__).resolve().parents[3]

# Ruta real del catálogo de síntomas
SYMPTOMS_PATH = BASE_DIR / "data" / "symptoms.json"


def load_symptoms() -> list:
    # Verificación explícita para depurar ruta
    if not SYMPTOMS_PATH.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {SYMPTOMS_PATH}")

    # Carga del JSON
    with open(SYMPTOMS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    # Aplanado del catálogo por bloques de specialty
    flattened = []
    for block in data:
        specialty = block.get("specialty")
        symptoms = block.get("symptoms", [])
        for symptom in symptoms:
            if "specialty" not in symptom:
                symptom["specialty"] = specialty
            flattened.append(symptom)

    return flattened