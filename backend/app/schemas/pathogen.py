from pydantic import BaseModel, field_validator
from typing import Optional
from app.models.pathogen import PathogenFamily


class PathogenBase(BaseModel):
    name: str
    scientific_name: Optional[str] = None
    family: PathogenFamily
    description: Optional[str] = None
    common_resistance_profile: Optional[str] = None
    is_active: bool = True

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip()


class PathogenCreate(PathogenBase):
    pass


class PathogenUpdate(PathogenBase):
    pass


class PathogenOut(PathogenBase):
    id: int

    class Config:
        from_attributes = True