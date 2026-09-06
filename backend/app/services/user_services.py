from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException,status

class User_Serviices():
    @staticmethod
    def create_user(db: Session, data: UserCreate):
        existing = db.query(User).filter(User.email == data.email).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail= "Email already registered")
        user = User(
            full_name=data.full_name,
            email=data.email,
            password=hash_password(data.password),
            role=data.role,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def login(db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=" wrong email")
        if not verify_password(password,user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=" wrong password")
        token =create_access_token({"sub":user.email})   
    
        return {
            "access_token":token,
            "token_type":"Bearer"
        }
