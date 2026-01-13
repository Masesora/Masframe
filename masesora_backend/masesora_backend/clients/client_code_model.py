from pydantic import BaseModel, EmailStr


class ClientCode(BaseModel):
    email: EmailStr
    codigo: str
    is_active: bool = True