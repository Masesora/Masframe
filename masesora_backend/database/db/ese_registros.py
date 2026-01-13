from masesora_backend.database.database import get_collection

# Colección oficial donde se guardan los ESE originales enviados desde la web
ese_registros_collection = get_collection("ese_registros")