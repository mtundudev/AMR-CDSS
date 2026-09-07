from pydantic import BaseModel, field_validator
from datetime import date,datetime
from typing import Optional
from app.models.patient import Gender

class PatientCreate(BaseModel):
    full_name: str
    date_of_birth: date
    gender: Gender
    phone_number: Optional[str] = None
    address: Optional[str] = None

    @field_validator("date_of_birth")
    @classmethod
    def dob_not_future(cls, value: date):
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")
        return value
    
    
class PatientUpdate(BaseModel):
    full_name:Optional[str]=None
    date_of_birth: Optional[date]=None
    gender: Optional[Gender]=None
    phone_number: Optional[str] = None
    address: Optional[str] = None

    @field_validator("date_of_birth")
    @classmethod
    def dob_not_future(cls, value: date):
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")
        return value
    
class PatientResponse(BaseModel):
    id: int
    patient_code: str
    full_name: str
    date_of_birth: date
    age:int
    created_by:int
    gender: Gender
    phone_number: Optional[str]
    address: Optional[str]
    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True