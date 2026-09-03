from app.services.ml_services import image_analysis
from fastapi import APIRouter,File,UploadFile,HTTPException,status,Depends
from pathlib import Path
from app.models.user import User,UserRole
from app.core.dependencies import get_current_user



router=APIRouter(prefix="/image",tags=["Image analysis"])

@router.post("")
async def uplaod_image(file:UploadFile=File(...),Current_user:User=Depends(get_current_user)):
    if Current_user.role not in  (UserRole.LAB_TECHNICIAN,UserRole.ADMIN):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you not have action to perform this")
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
    
    with open(file_path, "wb") as buffer:
        buffer.write(image)
        
    return{
        "filename":file.filename,
        "file_path":file_path,
        "analysis":analysis,
    }    
        
        


