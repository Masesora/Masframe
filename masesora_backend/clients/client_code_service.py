from masesora_backend.database.database import get_collection

async def validate_cliente_login(email: str, codigo: str) -> dict | None:
    """
    Valida acceso de cliente por email + código MAS®.
    """

    collection = get_collection("clients")  # <-- colección correcta

    email = email.strip().lower()
    codigo = codigo.strip()

    cliente = await collection.find_one({
        "email": email,
        "codigo": codigo
    })

    if not cliente:
        return None

    return cliente