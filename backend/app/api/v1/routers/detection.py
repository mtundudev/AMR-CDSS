from app.services.ml_services import image_analysis
from app.services.patient import Patient_Services
from fastapi import APIRouter,File,UploadFile,Depends
from pathlib import Path
from fastapi import HTTPException,status
from app.services.storage.storage import IMAGE_TYPES,UploadCatgory,save_upload_file
from app.core.database import get_db
from sqlalchemy.orm import Session


router=APIRouter(prefix="/image",tags=["Image analysis"])

@router.post("/{patient_id}")
async def uplaod_image(patient_id:int,db:Session=Depends(get_db),file:UploadFile=File(...)):

    
    image=await file.read()
    analysis=image_analysis(image)

    
    file_path = save_upload_file(
        file=file,
        allowed_types=IMAGE_TYPES,
        category=UploadCatgory.AMR_PHOTO
    )
    upadete_image= Patient_Services.create_image(
        patent_id=patient_id,
        path = file_path,
        db=db
    )
    

    
    
    return{
        "filename":file.filename,
        "image details":[upadete_image],
        "analysis":analysis,
    }    
        
        


