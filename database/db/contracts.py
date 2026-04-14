from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Contract(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    codigo: str
    empresa: str
    plan: str
    segment: str
    price: Optional[float]
    specialties: List[str]
    guarantee: Optional[dict]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "draft"  # draft | sent | signed | cancelled
    signed_at: Optional[datetime] = None
    signed_by_client: Optional[str] = None