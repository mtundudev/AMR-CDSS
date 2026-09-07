import enum
from sqlalchemy import Column, Integer, String, Text, Enum, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class AntimicrobialClass(str, enum.Enum):
    PENICILLIN = "penicillin"
    CEPHALOSPORIN = "cephalosporin"
    FLUOROQUINOLONE = "fluoroquinolone"
    AMINOGLYCOSIDE = "aminoglycoside"
    MACROLIDE = "macrolide"
    TETRACYCLINE = "tetracycline"
    CARBAPENEM = "carbapenem"
    SULFONAMIDE = "sulfonamide"
    GLYCOPEPTIDE = "glycopeptide"
    OTHER = "other"


class Antimicrobial(Base):
    __tablename__ = "antimicrobials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False, index=True)
    generic_name = Column(String(150), nullable=True)
    drug_class = Column(Enum(AntimicrobialClass), nullable=False, default=AntimicrobialClass.OTHER)
    description = Column(Text, nullable=True)
    route_of_administration = Column(String(50), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())