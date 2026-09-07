import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class UserRole(str, enum.Enum):
    DOCTOR= "doctor"
    LAB_TECHNICIAN = "lab_technician"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.DOCTOR)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    visit= relationship("ClinicalVisit",back_populates="user")
    patient=relationship("Patient",back_populates="user")