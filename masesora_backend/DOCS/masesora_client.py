import requests

# Backend MAS@FRAME® local
BASE_URL = "http://127.0.0.1:8000"


# =========================
#  CATÁLOGO DE SÍNTOMAS
# =========================

def get_symptoms():
    """
    Obtiene el catálogo maestro de síntomas.
    GET /symptom-master/
    """
    url = f"{BASE_URL}/symptom-master/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# =========================
#  EVALUACIÓN CLÍNICA
# =========================

def evaluate_symptom(client_id: str, master_id: str, data: dict):
    """
    Evalúa un síntoma concreto para un cliente.
    POST /clinical/client/{client_id}/symptom/{master_id}
    """
    url = f"{BASE_URL}/clinical/client/{client_id}/symptom/{master_id}"
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()


def get_department_overview(client_id: str, department: str):
    """
    Obtiene el overview clínico de un departamento para un cliente.
    GET /clinical/client/{client_id}/department/{department}
    """
    url = f"{BASE_URL}/clinical/client/{client_id}/department/{department}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# =========================
#  SCANNER & TRIAJE
# =========================

def get_scanner_result(codigo: str):
    """
    Ejecuta el scanner y devuelve el triaje completo para un código.
    GET /scanner/result/{codigo}
    """
    url = f"{BASE_URL}/scanner/result/{codigo}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# =========================
#  TESTS RÁPIDOS DE FASE 6
# =========================

def test_scanner_and_triaje(codigo: str):
    """
    Test clínico completo para Fase 6:
    - Llama al scanner
    - Devuelve diagnóstico, presupuesto y síntomas
    """
    data = get_scanner_result(codigo)

    return {
        "codigo": data.get("codigo"),
        "diagnostico": data.get("diagnostico"),
        "presupuesto_base": data.get("presupuesto_base"),
        "num_sintomas": len(data.get("sintomas", [])),
        "especialidades": [e.get("nombre", "Sin nombre") for e in data.get("especialidades", [])]
    }


def test_symptom_flow(client_id: str, master_id: str, payload: dict):
    """
    Test de flujo de síntoma:
    - Evalúa un síntoma
    - Recupera overview del departamento
    """
    eval_result = evaluate_symptom(client_id, master_id, payload)

    department = eval_result.get("department") or payload.get("department", "general")
    overview = get_department_overview(client_id, department)

    return {
        "eval_result": eval_result,
        "department_overview": overview
    }


# =========================
#  BLOQUE DE PRUEBA MANUAL
# =========================

if __name__ == "__main__":
    # ⚠️ Ajusta estos valores a datos reales de tu base:
    TEST_CODIGO = "MAS-OX2JMK46"       # Código de scanner válido
    TEST_CLIENT_ID = "CLIENTE_DEMO"    # ID de cliente válido
    TEST_MASTER_ID = "SYMPTOM_DEMO"    # ID de síntoma maestro válido

    print("=== TEST SCANNER & TRIAJE ===")
    try:
        triaje = test_scanner_and_triaje(TEST_CODIGO)
        print(triaje)
    except Exception as e:
        print("Error en test_scanner_and_triaje:", e)

    # Ejemplo de payload para síntoma
    symptom_payload = {
        "severity": 5,
        "frequency": "daily",
        "duration_days": 30,
        "department": "general"
    }

    print("\n=== TEST EVALUACIÓN DE SÍNTOMA ===")
    try:
        result = test_symptom_flow(TEST_CLIENT_ID, TEST_MASTER_ID, symptom_payload)
        print(result)
    except Exception as e:
        print("Error en test_symptom_flow:", e)