from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.ckinical_rule import ClinicalRule
from app.models.pathogen import Pathogen
from app.models.antinicrobial import Antimicrobial
from app.schemas.clinical_rule import ClinicalRuleCreate, ClinicalRuleUpdate


def _validate_references(db: Session, pathogen_id: int | None, antimicrobial_id: int | None):
    if pathogen_id is not None and not db.query(Pathogen).filter(Pathogen.id == pathogen_id).first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Pathogen not found")
    if antimicrobial_id is not None and not db.query(Antimicrobial).filter(Antimicrobial.id == antimicrobial_id).first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Antimicrobial not found")


def create_rule(db: Session, data: ClinicalRuleCreate) -> ClinicalRule:
    _validate_references(db, data.pathogen_id, data.antimicrobial_id)
    rule = ClinicalRule(**data.model_dump())
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule


def get_rule(db: Session, rule_id: int) -> ClinicalRule:
    rule = db.query(ClinicalRule).filter(ClinicalRule.id == rule_id).first()
    if not rule:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Rule not found")
    return rule


def list_rules(db: Session, active_only: bool = False, pathogen_id: int | None = None, skip: int = 0, limit: int = 50) -> list[ClinicalRule]:
    query = db.query(ClinicalRule)
    if active_only:
        query = query.filter(ClinicalRule.is_active == True)
    if pathogen_id is not None:
        query = query.filter(ClinicalRule.pathogen_id == pathogen_id)
    return query.offset(skip).limit(limit).all()


def update_rule(db: Session, rule_id: int, data: ClinicalRuleUpdate) -> ClinicalRule:
    rule = get_rule(db, rule_id)
    _validate_references(db, data.pathogen_id, data.antimicrobial_id)
    for key, value in data.model_dump().items():
        setattr(rule, key, value)
    db.commit()
    db.refresh(rule)
    return rule


def deactivate_rule(db: Session, rule_id: int) -> ClinicalRule:
    rule = get_rule(db, rule_id)
    rule.is_active = False
    db.commit()
    db.refresh(rule)
    return rule


def delete_rule(db: Session, rule_id: int) -> bool:
    rule = db.query(ClinicalRule).filter(ClinicalRule.id == rule_id).first()
    if not rule:
        return False
    db.delete(rule)
    db.commit()
    return True