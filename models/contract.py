from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Contract(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    client_id: str
    plan_name: Optional[str] = None
    precio: Optional[float] = None
    signed: bool = False
    signed_at: Optional[datetime] = None

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True
    }