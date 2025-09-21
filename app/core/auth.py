# app/core/auth.py

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.deps import get_db
from app.api.v1.customer import customer_service
from app.api.v1.staff import staff_service

# ================= CONFIG =================
SECRET_KEY = "$2b$12$eO0maVR9xWGY2c7aPfB0f.GbtLy6saBUJBAEQfiz3N9leR/5D5zgu"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

""" satu tempat login """
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

# ================= SCHEMA =================
class TokenData(BaseModel):
    user_id: int
    role: Optional[str] = None   # customer atau staff


""" ================= JWT FUNCTIONS ================= """
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str = Depends(oauth2_scheme)) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        role: str = payload.get("role")
        if user_id is None or role is None:
            raise credentials_exception
        return TokenData(user_id=user_id, role=role)
    except JWTError:
        raise credentials_exception


""" ================= ROLE CHECK DEPENDENCY ================= """
def require_role(*allowed_roles: str):
    """
    Dependency reusable untuk membatasi akses endpoint berdasarkan role.
    """
    def dependency(token_data: TokenData = Depends(verify_token)):
        if token_data.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return token_data
    return dependency


""" ================= OPTIONAL HELPER ================= """
def get_current_user(expected_role: Optional[str] = None, token_data: TokenData = Depends(verify_token)):
    """
    Bisa dipakai untuk cek role optional di route tertentu.
    """
    if expected_role and token_data.role != expected_role:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return token_data


""" ================= UNIVERSAL LOGIN ================= """
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Universal login untuk Swagger (Customer & Staff).
    """
    # coba login sebagai customer
    user = customer_service.authenticate_customer(db, form_data.username, form_data.password)
    if user:
        token = create_access_token({"user_id": user.id, "role": "customer"})
        return {"access_token": token, "token_type": "bearer"}

    # coba login sebagai staff
    user = staff_service.authenticate_staff(db, form_data.username, form_data.password)
    if user:
        token = create_access_token({"user_id": user.id, "role": user.role})
        return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Invalid username or password")
