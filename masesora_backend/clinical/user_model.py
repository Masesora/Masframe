from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base  # Ajusta si tu Base está en otro sitio


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # "admin" | "cc" | "aci"
    is_active = Column(Boolean, default=True)