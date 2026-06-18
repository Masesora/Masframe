from pydantic import BaseModel
from typing import Optional

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    pago_confirmado: Optional[bool] = None