from masesora_backend.database.database import get_collection

def clients_collection():
    return get_collection("clients")