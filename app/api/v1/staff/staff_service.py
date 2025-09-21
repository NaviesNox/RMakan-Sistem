from sqlalchemy.orm import Session
from app.model.v1.staff.staff_schemas import (
    StaffCreate,
    StaffUpdate,
)
from models import Staff
from app.core.security import hash_password
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_staff(db: Session, username: str, password: str):
    user = db.query(Staff).filter(Staff.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

""" Function untuk ambil data staff """
def get_all_staff(db: Session):
    return db.query(Staff).all()


""" Function untuk ambil data staff berdasarkan ID """
def get_staff_by_id(db: Session, staff_id: int):
    return db.query(Staff).filter(Staff.id == staff_id).first()


""" Function untuk tambah data staff """
def create_staff(db: Session, staff: StaffCreate):
    new_staff_data = staff.model_dump()
    new_staff_data["password"] = hash_password(new_staff_data["password"])
    
    new_staff = Staff(**new_staff_data)
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

""" Function untuk update data staff """
def update_staff(db: Session, staff_id: int, staff_update: StaffUpdate):
    staff = get_staff_by_id(db, staff_id)
    if not staff:
        return None

    update_data = staff_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(staff, key, value)

    db.commit()
    db.refresh(staff)
    return staff


""" Function untuk hapus data staff """
def delete_staff(db: Session, staff_id: int):
    staff = get_staff_by_id(db, staff_id)
    if not staff:
        return None

    db.delete(staff)
    db.commit()
    return staff
