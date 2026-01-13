def activate_permissions(client_id, plan):
    """
    PIE → acceso limitado
    PRE → acceso completo
    """
    if plan == "PRE":
        return {"client_id": client_id, "permissions": "partial"}
    return {"client_id": client_id, "permissions": "full"}