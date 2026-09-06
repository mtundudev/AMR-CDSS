from app.core.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer,primary_key=True,index=True,nullable=False)
    file_name = Column(String)
    file_path = Column(String)
    created_by = Column(DateTime(timezone=True),server_default=func.now())

    patient = relationship("Patient",back_populates="media")
