from sqlalchemy.orm import Session
from app.core.security import verify_password
from models import Customer, Staff

def authenticate_customer(db: Session, username: str, password: str):
    user = db.query(Customer).filter(Customer.username == username).first()
    if not user:
        return None
    # cek password hash
    if not verify_password(password, user.password):
        return None
    return user

def authenticate_staff(db: Session, username: str, password: str):
    staff = db.query(Staff).filter(Staff.username == username).first()
    if not staff:
        return None
    if not verify_password(password, staff.password):
        return None
    return staff
