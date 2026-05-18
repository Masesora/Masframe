# backend/models/lead.py
# Crea este archivo en: C:\Masframe\masesora_backend\models\lead.py

from pydantic import BaseModel, Field
from typing import Any, Dict, Optional
from datetime import datetime


class LeadIn(BaseModel):
    name: str
    email: str
    company: Optional[str] = None
    consent: bool
    consentComercial: Optional[bool] = False
    emailIsFree: Optional[bool] = None
    context: Optional[Dict[str, Any]] = {}
    diagnosis: Optional[Dict[str, Any]] = {}
    damage: Optional[Dict[str, Any]] = {}


class LeadDB(LeadIn):
    createdAt: datetime = Field(default_factory=datetime.utcnow)
