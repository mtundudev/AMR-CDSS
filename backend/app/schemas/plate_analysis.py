from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class SusceptibilityStatus(str, Enum):
    SUSCEPTIBLE = "Susceptible"
    INTERMEDIATE = "Intermediate"
    RESISTANT = "Resistant"

class DiskPrediction(BaseModel):
    antibiotic_name: str = Field(..., example="Ciprofloxacin")
    zone_diameter_mm: float = Field(..., description="Measured clearance zone diameter in mm", example=22.4)
    status: SusceptibilityStatus = Field(..., description="CLSI/EUCAST standard classification")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Model prediction confidence score")

class LabAnalysisResponse(BaseModel):
    sample_id: str
    total_disks_detected: int
    predictions: List[DiskPrediction]
    status_summary: str = Field(default="Analysis Complete")