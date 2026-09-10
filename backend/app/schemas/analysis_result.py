from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime


class AnalysisResultCreate(BaseModel):
    visit_id: int
    pathogen_id: Optional[int] = None
    image_path: str
    confidence_score: Optional[float] = None
    detection_summary: Optional[str] = None

    @field_validator("confidence_score")
    @classmethod
    def score_in_range(cls, value: Optional[float]) -> Optional[float]:
        if value is not None and not (0.0 <= value <= 1.0):
            raise ValueError("confidence_score must be between 0.0 and 1.0")
        return value


class AnalysisResultOut(BaseModel):
    id: int
    visit_id: int
    pathogen_id: Optional[int]
    image_path: str
    confidence_score: Optional[float]
    detection_summary: Optional[str]
    analyzed_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True