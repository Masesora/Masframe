from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Contract(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    client_id: str
    signed: bool = False
    signed_at: Optional[datetime] = None
    plan_name: Optional[str] = None