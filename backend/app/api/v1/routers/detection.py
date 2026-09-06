from app.services.ml_services import image_analysis
from app.services.patient import Patient_Services
from fastapi import APIRouter,File,UploadFile,HTTPException,status,Depends,Depends
from pathlib import Path
from fastapi import HTTPException,status



router=APIRouter(prefix="/image",tags=["Image analysis"])

@router.post("")
async def uplaod_image(file:UploadFile=File(...)):
    allowed_extensions={
        ".png",".jpg","jpeg"
        
    }
    extension=Path(file.filename).suffix.lower()
    if extension not in allowed_extensions:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="only image")
    if not file.content_type:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="check your uploaded file")
    
    UPLOAD_DIR=Path("uploads/model/images")
    UPLOAD_DIR.mkdir(parents=True,exist_ok=True)
    
    file_path=UPLOAD_DIR/file.filename
    
    
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
        
        


