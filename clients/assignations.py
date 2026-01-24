def assign_roles(client_id, contract):
    """
    Asigna:
    - CC Consultor Certificado
    - ACI Agente de Cambio Interno 
    - ADMIN Administrador
    - CLI Cliente
   
 """
    return {
        "client_id": client_id,
        "cc_assigned": "CC-001",
        "aci_assigned": "ACI-003"
        "admin_assigned": "ADM-003"
        "cli_assigned": "CLI-003"
    }