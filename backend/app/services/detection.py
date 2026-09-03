from app.models.patient import Patient
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

class DetactionService:
    @staticmethod
    def createDetection(patient_id:int,db:Session):
        patient = db.query(Patient).filter(
            Patient.id == patient_id
        ).first()

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="patient with that id not found"
            )
        

        return 