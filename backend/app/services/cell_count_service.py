from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.cecl_count import CellCount
from app.models.analysis_result import AnalysisResult
from pathlib import Path
from app.schemas.cell_count import CellCountCreate

def create_cell_count(db: Session,analysis_result_id):
    result = db.query(AnalysisResult).filter(AnalysisResult.id == analysis_result_id).first()
    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Analysis result not found")

    image_path = Path(result.image_path)
    if not image_path.is_absolute():
        image_path = Path.cwd() / image_path
    if not image_path.is_file():
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Analysis image not found")

    rbc_count=0
    wbc_count=0
    platelet_count=0
                                               
    record = CellCount(
        rbc_count=rbc_count,
        wbc_count=wbc_count,
        platelet_count=platelet_count,
        analysis_result_id=analysis_result_id
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_cell_count(db: Session, cell_count_id: int) -> CellCount:
    record = db.query(CellCount).filter(CellCount.id == cell_count_id).first()
    if not record:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Cell count not found")
    return record


def get_by_analysis_result(db: Session, analysis_result_id: int) -> list[CellCount]:
    return db.query(CellCount).filter(CellCount.analysis_result_id == analysis_result_id).all()


def delete_cell_count(db: Session, cell_count_id: int) -> bool:
    record = db.query(CellCount).filter(CellCount.id == cell_count_id).first()
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True