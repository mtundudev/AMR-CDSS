from pydantic import BaseModel, field_validator
from typing import Optional


class CellCountBase(BaseModel):
    rbc_count: Optional[float] = None
    wbc_count: Optional[float] = None
    platelet_count: Optional[float] = None
    hemoglobin_level: Optional[float] = None
    hematocrit: Optional[float] = None

    @field_validator("rbc_count", "wbc_count", "platelet_count", "hemoglobin_level", "hematocrit")
    @classmethod
    def non_negative(cls, value: Optional[float]) -> Optional[float]:
        if value is not None and value < 0:
            raise ValueError("Value cannot be negative")
        return value


class CellCountCreate(CellCountBase):
    analysis_result_id: int


class CellCountOut(CellCountBase):
    id: int
    analysis_result_id: int

    class Config:
        from_attributes = True