from pydantic import BaseModel, field_validator
from typing import Optional
from app.models.ckinical_rule import RuleSeverity


class ClinicalRuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    pathogen_id: Optional[int] = None
    antimicrobial_id: Optional[int] = None
    condition_expression: str
    recommendation: str
    severity: RuleSeverity = RuleSeverity.WARNING
    is_active: bool = True

    @field_validator("name", "condition_expression", "recommendation")
    @classmethod
    def not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Field cannot be empty")
        return value.strip()


class ClinicalRuleCreate(ClinicalRuleBase):
    pass


class ClinicalRuleUpdate(ClinicalRuleBase):
    pass


class ClinicalRuleOut(ClinicalRuleBase):
    id: int

    class Config:
        from_attributes = True