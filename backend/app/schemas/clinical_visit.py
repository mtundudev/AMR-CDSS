from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from app.models.clinical_visit import VisitStatus


class ClinicalVisitCreate(BaseModel):
    patient_id: int
    physician_id: Optional[int] = None
    chief_complaint: Optional[str] = None
    notes: Optional[str] = None


class ClinicalVisitDiagnosisUpdate(BaseModel):
    diagnosis: str
    notes: Optional[str] = None

    @field_validator("diagnosis")
    @classmethod
    def diagnosis_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Diagnosis cannot be empty")
        return value.strip()


class ClinicalVisitAssignPhysician(BaseModel):
    physician_id: int


class ClinicalVisitOut(BaseModel):
    id: int
    patient_id: int
    physician_id: Optional[int]
    visit_date: datetime
    chief_complaint: Optional[str]
    diagnosis: Optional[str]
    status: VisitStatus
    notes: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True