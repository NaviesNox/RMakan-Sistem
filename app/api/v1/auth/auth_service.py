from sqlalchemy.orm import Session
from app.core.security import verify_password
from models import Users

def authenticate_customer(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return None
    # cek password hash
    if not verify_password(password, user.password):
        return None
    return user

def authenticate_staff(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    # cek role staff
    if user.role not in ["admin", "waiter", "manager", "reservationStaff"]:
        return None
    return user
