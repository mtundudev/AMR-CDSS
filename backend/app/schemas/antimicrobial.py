from pydantic import BaseModel, field_validator
from typing import Optional
from app.models.antinicrobial import AntimicrobialClass


class AntimicrobialBase(BaseModel):
    name: str
    generic_name: Optional[str] = None
    drug_class: AntimicrobialClass = AntimicrobialClass.OTHER
    description: Optional[str] = None
    route_of_administration: Optional[str] = None
    is_active: bool = True

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip()


class AntimicrobialCreate(AntimicrobialBase):
    pass


class AntimicrobialUpdate(AntimicrobialBase):
    pass


class AntimicrobialOut(AntimicrobialBase):
    id: int

    class Config:
        from_attributes = True