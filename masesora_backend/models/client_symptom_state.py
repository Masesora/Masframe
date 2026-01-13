from pydantic import BaseModel, Field, field_validator
from bson import ObjectId
from enum import Enum
from typing import Optional

class StatusColor(str, Enum):
    verde = "verde"
    ambar = "ambar"
    rojo = "rojo"

class ClientSymptomState(BaseModel):
    id: str | None = Field(default=None, alias="_id")
    client_id: str
    master_id: str
    short_code: str
    department: str
    specialty: str
    kpi_value: float
    status: StatusColor
    notes: Optional[str] = None
    timestamp: str
    fuente: str

    @field_validator("id", mode="before")
    @classmethod
    def convert_objectid(cls, v):
        return str(v) if isinstance(v, ObjectId) else v

ClientSymptomState.model_rebuild()