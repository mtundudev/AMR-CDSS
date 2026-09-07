from sqlalchemy.orm import Session
from app.models.pathogen import Pathogen
from app.schemas.pathogen import PathogenCreate, PathogenUpdate


def create_pathogen(db: Session, data: PathogenCreate):
    record = Pathogen(**data.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_pathogen(db: Session, pathogen_id: int) -> Pathogen | None:
    return db.query(Pathogen).filter(Pathogen.id == pathogen_id).first()


def get_by_name(db: Session, name: str) -> Pathogen | None:
    return db.query(Pathogen).filter(Pathogen.name == name).first()


def list_pathogens(
    db: Session,
    family: str | None = None,
    active_only: bool = False,
    skip: int = 0,
    limit: int = 50,
) -> list[Pathogen]:
    query = db.query(Pathogen)
    if family:
        query = query.filter(Pathogen.family == family)
    if active_only:
        query = query.filter(Pathogen.is_active == True)
    return query.offset(skip).limit(limit).all()


def update_pathogen(db: Session, pathogen_id: int, data: PathogenUpdate):
    record = get_pathogen(db, pathogen_id)
    if not record:
        return None
    for key, value in data.model_dump().items():
        setattr(record, key, value)
    db.commit()
    db.refresh(record)
    return record


def delete_pathogen(db: Session, pathogen_id: int):
    record = get_pathogen(db, pathogen_id)
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True