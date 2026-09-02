from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
import enum
from datetime import datetime
from app.core.database import Base

class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    patient_code = Column(String(20), unique=True, index=True, nullable=True)
    full_name = Column(String(150), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    age=Column(Integer,nullable=True)
    phone_number = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    created_at = Column(DateTime,default=datetime.now())
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
