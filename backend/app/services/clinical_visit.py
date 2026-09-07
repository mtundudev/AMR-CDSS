from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.clinical_visit import ClinicalVisit, VisitStatus
from app.models.patient import Patient
from app.models.user import User, UserRole
from app.schemas.clinical_visit import ClinicalVisitCreate, ClinicalVisitDiagnosisUpdate


def create_visit(db: Session, data: ClinicalVisitCreate):
    patient = db.query(Patient).filter(Patient.id == data.patient_id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")

    if data.physician_id is not None:
        physician = db.query(User).filter(
            User.id == data.physician_id, User.role == UserRole.PHYSICIAN
        ).first()
        if not physician:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="physician_id does not refer to a valid physician")

    visit = ClinicalVisit(
        patient_id=data.patient_id,
        physician_id=data.physician_id,
        chief_complaint=data.chief_complaint,
        notes=data.notes,
        status=VisitStatus.PENDING_ANALYSIS,
    )
    db.add(visit)
    db.commit()
    db.refresh(visit)
    return visit


def get_visit(db: Session, visit_id: int) -> ClinicalVisit:
    visit = db.query(ClinicalVisit).filter(ClinicalVisit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Visit not found")
    return visit


def list_visits_by_patient(db: Session, patient_id: int):
    return (
        db.query(ClinicalVisit)
        .filter(ClinicalVisit.patient_id == patient_id)
        .order_by(ClinicalVisit.visit_date.desc())
        .all()
    )


def list_visits_by_status(db: Session, status_filter: VisitStatus | None, skip: int = 0, limit: int = 50):
    query = db.query(ClinicalVisit)
    if status_filter:
        query = query.filter(ClinicalVisit.status == status_filter)
    return query.order_by(ClinicalVisit.visit_date.desc()).offset(skip).limit(limit).all()


def assign_physician(db: Session, visit_id: int, physician_id: int):
    visit = get_visit(db, visit_id)
    physician = db.query(User).filter(
        User.id == physician_id, User.role == UserRole.DOCTOR
    ).first()
    if not physician:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="physician_id does not refer to a valid physician")

    visit.physician_id = physician_id
    db.commit()
    db.refresh(visit)
    return visit


def submit_diagnosis(db: Session, visit_id: int, data: ClinicalVisitDiagnosisUpdate):
    visit = get_visit(db, visit_id)

    if visit.status == VisitStatus.PENDING_ANALYSIS:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail= "Cannot submit diagnosis before analysis is complete")
    if visit.status == VisitStatus.CLOSED:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail= "Visit is already closed")

    visit.diagnosis = data.diagnosis
    if data.notes is not None:
        visit.notes = data.notes
    visit.status = VisitStatus.CONFIRMED
    visit.updated_at = datetime.now()

    db.commit()
    db.refresh(visit)
    return visit


def mark_awaiting_review(db: Session, visit_id: int):
    visit = get_visit(db, visit_id)
    if visit.status != VisitStatus.PENDING_ANALYSIS:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Visit is not in pending_analysis state")
    visit.status = VisitStatus.AWAITING_REVIEW
    db.commit()
    db.refresh(visit)
    return visit


def close_visit(db: Session, visit_id: int):
    visit = get_visit(db, visit_id)
    if visit.status != VisitStatus.CONFIRMED:
        raise HTTPException(status.HTTP_409_CONFLICT, "Only confirmed visits can be closed")
    visit.status = VisitStatus.CLOSED
    visit.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(visit)
    return visit