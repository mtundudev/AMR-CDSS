from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate,PatientUpdate
from datetime import date
from app.models.user import UserRole
from fastapi import HTTPException,status

def auto_patient_code(patient_id: int):
    return f"HOSP-PAT-{patient_id:06d}"

def calc_age(dob:date):
    today=date.today()
    age=today.year-dob.year-((today.month,today.day)>(dob.month,dob.day))
    return age

class Patient_Services():
    @staticmethod
    def create_patient(db: Session, data: PatientCreate,current_user):
        if current_user.role not in (UserRole.ADMIN,UserRole.DOCTOR):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you not have action to perform this")
        patient=(db.query(Patient).filter(Patient.full_name==data.full_name,
                                        Patient.date_of_birth==data.date_of_birth,
                                        Patient.gender==data.gender).first())
        if patient:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Patient alredy registered")
        patient = Patient(
            full_name=data.full_name,
            address=data.address,
            date_of_birth=data.date_of_birth,
            age=calc_age(data.date_of_birth),
            gender=data.gender,
            phone_number=data.phone_number
        )
        
        db.add(patient)
        db.flush() 
        patient.patient_code = auto_patient_code(patient.id)
    
        db.commit()
        db.refresh(patient)
        return patient

    @staticmethod
    def get_patient(db: Session, patient_id: int):
        patient=db.query(Patient).filter(Patient.id == patient_id).first()
        return patient
    @staticmethod
    def get_patient_by_code(db: Session, code: str):
        patient=db.query(Patient).filter(Patient.patient_code == code).first()
        return patient

    @staticmethod
    def list_patients(db: Session, skip: int = 0, limit: int = 50):
        patient= db.query(Patient).offset(skip).limit(limit).all()
        return patient

    @staticmethod
    def update_patient(db: Session, patient_id: int, data: PatientUpdate ,current_user):
        if current_user.role not in (UserRole.ADMIN,UserRole.DOCTOR):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you not have action to perform this")
                
        patient =db.query(Patient).filter(Patient.id==patient_id).first()
        if not patient:
         raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"patient with id {patient_id} not found")
        if data.full_name:
         patient.full_name=data.full_name
        if data.gender:
         patient.gender==data.gender
        if data.date_of_birth:
            patient.date_of_birth=data.date_of_birth
            patient.age=calc_age(data.date_of_birth)        
        if data.address:
            patient.address=data.address    
    
        db.commit()
        db.refresh(patient)
        return patient
    
    @staticmethod
    def delete_patient(db: Session, patient_id: int,current_user):
        if current_user.role != UserRole.ADMIN:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you not have action to perform this")
                
        patient =db.query(Patient).filter(Patient.id==patient_id).first()
        if not patient:
            raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"patient with id {patient_id} not found")
        db.delete(patient)
        db.commit()
        
        return {
        "message":"patient info deleted"
    }
