from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_password_hash(password: str):
    return pwd_context.hash(password)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
SECRET_KEY= "my_super_secret_key"
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire_time =datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_time})
    Token =jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role = payload.get("role")

        if role is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
            
        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
     
def check_admin(payload: dict = Depends(get_current_user), token: str = Depends(oauth2_scheme)):
    role = payload.get("role")
    if role != "Admin":
        raise HTTPException(status_code=403, detail="You are not an admin! Only admins can do this.")
    return payload

def check_passenger(payload: dict = Depends(get_current_user), token: str = Depends(oauth2_scheme)):
    role = payload.get("role")
    if role != "Passenger":
        raise HTTPException(status_code=403, detail="Only passengers can book flights!")
    return payload