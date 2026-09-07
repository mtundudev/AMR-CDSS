from sqlalchemy.orm import Session
from app.models.antinicrobial import Antimicrobial
from app.schemas.antimicrobial import AntimicrobialCreate, AntimicrobialUpdate


def create_antimicrobial(db: Session, data: AntimicrobialCreate) -> Antimicrobial:
    record = Antimicrobial(**data.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_antimicrobial(db: Session, antimicrobial_id: int) -> Antimicrobial | None:
    return db.query(Antimicrobial).filter(Antimicrobial.id == antimicrobial_id).first()


def get_by_name(db: Session, name: str) -> Antimicrobial | None:
    return db.query(Antimicrobial).filter(Antimicrobial.name == name).first()


def list_antimicrobials(
    db: Session,
    drug_class: str | None = None,
    active_only: bool = False,
    skip: int = 0,
    limit: int = 50,
) -> list[Antimicrobial]:
    query = db.query(Antimicrobial)
    if drug_class:
        query = query.filter(Antimicrobial.drug_class == drug_class)
    if active_only:
        query = query.filter(Antimicrobial.is_active == True)
    return query.offset(skip).limit(limit).all()


def update_antimicrobial(db: Session, antimicrobial_id: int, data: AntimicrobialUpdate) -> Antimicrobial | None:
    record = get_antimicrobial(db, antimicrobial_id)
    if not record:
        return None
    for key, value in data.model_dump().items():
        setattr(record, key, value)
    db.commit()
    db.refresh(record)
    return record


def delete_antimicrobial(db: Session, antimicrobial_id: int) -> bool:
    record = get_antimicrobial(db, antimicrobial_id)
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True