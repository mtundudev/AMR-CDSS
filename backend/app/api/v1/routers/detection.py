from app.services.ml_services import image_analysis
from app.services.patient import Patient_Services
from fastapi import APIRouter,File,UploadFile,Depends
from app.services.storage.storage import save_upload_file,IMAGE_TYPES,UploadCatgory
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.dependencies import get_current_user
from app.core.database import get_db



router=APIRouter(prefix="/image",tags=["Image analysis"])

@router.post("/{patient_id}")
async def uplaod_image(patient_id,db:Session=Depends(get_db),file:UploadFile=File(...),
                       current_user:User=Depends(get_current_user)):


    
    
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
        "analysis":analysis,
    }    
        
        


