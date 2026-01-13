from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Client(BaseModel):
    """
    Modelo MAS® para clientes.
    Compatible con MongoDB y con EPIC 0.
    """

    id: Optional[str] = Field(default=None, alias="_id")
    name: Optional[str] = None
    email: EmailStr
    codigo: str
    is_active: bool = True
    empresa: Optional[str] = None  # opcional, pero útil para MAS®

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True
    }