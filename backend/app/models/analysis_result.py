from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    visit_id = Column(Integer, ForeignKey("clinical_visits.id"), nullable=False, index=True)
    pathogen_id = Column(Integer, ForeignKey("pathogens.id"), nullable=True)
    image_path = Column(String(255), nullable=False)
    confidence_score = Column(Float, nullable=True)
    detection_summary = Column(Text, nullable=True)

    analyzed_at = Column(DateTime,default=datetime.now())
    created_at = Column(DateTime,default=datetime.now,onupdate=datetime.now())

    visit = relationship("ClinicalVisit", back_populates="analysis_results")
    pathogen = relationship("Pathogen",back_populates="analysis")
    cell_counts=relationship("CellCount",back_populates="analysis_result")
    