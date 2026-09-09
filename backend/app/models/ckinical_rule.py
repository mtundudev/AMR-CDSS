import enum
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class RuleSeverity(str, enum.Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class ClinicalRule(Base):
    __tablename__ = "clinical_rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)

    pathogen_id = Column(Integer, ForeignKey("pathogens.id"), nullable=True)
    antimicrobial_id = Column(Integer, ForeignKey("antimicrobials.id"), nullable=True)

    condition_expression = Column(Text, nullable=False)
    recommendation = Column(Text, nullable=False)
    severity = Column(Enum(RuleSeverity), nullable=False, default=RuleSeverity.WARNING)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    pathogen = relationship("Pathogen",back_populates="rules")
    antimicrobial = relationship("Antimicrobial",back_populates="rules")