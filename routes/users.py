from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db
import models, auth
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(prefix="/users", tags=["Users"])
class Userceate(BaseModel):
    email: str
    password: str
    name : str
    role: str = "Passenger"
@router.post("/signup", status_code=status.HTTP_201_CREATED)
def sign_up(user_data:Userceate, db:Session= Depends(get_db) ):
    Existing_user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if Existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hased_pass = auth.get_password_hash(user_data.password)
    new_user = models.User(name = user_data.name, email= user_data.email, hashed_password = hased_pass,role=user_data.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException (status_code=403, detail= "Invalid Credentials")
    access_token = auth.create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

