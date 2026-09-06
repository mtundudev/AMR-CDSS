from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.core.dependencies import get_current_user
from app.schemas.user import UserCreate, UserResponse
from app.services.user_services import User_Serviices
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse, status_code=201)
def register(data:UserCreate, db: Session = Depends(get_db)):
    return User_Serviices.create_user(db, data)

@router.post("/login")
def login(data:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db)):
   return User_Serviices.login(db,data.username,data.password)

@router.get("/me", response_model=UserResponse)
def myprofile(current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==current_user.id).first()
    return user
    