from masesora_backend.database.database import get_collection


async def validate_cliente_login(email: str, codigo: str) -> dict | None:
    """
    Valida acceso de cliente por código MAS®.
    Reglas:
    - el código existe
    - el email coincide
    - el código está activo
    - devuelve el cliente completo (Mongo document)
    """

    collection = get_collection("clients")

    cliente = await collection.find_one({"codigo": codigo})

    if not cliente:
        return None

    if cliente.get("email") != email:
        return None

    if not cliente.get("is_active", False):
        return None

    return cliente