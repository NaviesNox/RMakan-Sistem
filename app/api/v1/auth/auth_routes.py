from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import create_access_token
from app.core.deps import get_db
from app.api.v1.auth import auth_service
from datetime import timedelta

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    # cek ke customer
    user = auth_service.authenticate_customer(db, username, password)
    if not user:
        # kalau gagal, cek ke staff
        user = auth_service.authenticate_staff(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # buat JWT token
    access_token_expires = timedelta(minutes=30)
    token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": token, "token_type": "bearer"}
