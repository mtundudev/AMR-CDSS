import shutil
from enum import Enum
from fastapi import UploadFile,HTTPException,status
from pathlib import Path
from uuid import uuid4

class UploadCatgory(str, Enum):
    AMR_PHOTO = "amr_photo"

IMAGE_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp"
]

BASE_UPLOAD_FILE = Path("uploads")

def save_upload_file (
        file:UploadFile,
        allowed_types:list[str],
        category:UploadCatgory
) -> str:
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail= f"File type '{file.content_type}' is not allowed"
        )

    target_dir = BASE_UPLOAD_FILE/category.value
    target_dir.mkdir(parents=True, exist_ok=True)

    extension = Path(file.filename).suffix if file.filename else ""
    unique_filename = f"{uuid4()}{extension}"

    file_path = target_dir/unique_filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


        return str(file_path)



def delete_upload_file(path : str) -> bool:
    file_path = Path(path)


    if file_path.exists():
        file_path.unlink()
        return True

    return False


    