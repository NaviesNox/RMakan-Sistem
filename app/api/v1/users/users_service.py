from sqlalchemy.orm import Session
from app.model.v1.users.users_schemas import (
    UsersCreate,
    UsersUpdate,
    RegisterCreate
)
from models import Users
from app.core.security import hash_password
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    users = db.query(Users).filter(UsersCreate.username == username).first()
    if not users:
        return None
    if not verify_password(password, users.password):
        return None
    return users

""" Function untuk ambil data user """
def get_all_users(db: Session):
    return db.query(Users).all()


""" Function untuk ambil data user berdasarkan ID """
def get_users_by_id(db: Session, users_id: int):
    return db.query(Users).filter(Users.id == users_id).first()


""" Function untuk tambah data user """
def create_users(db: Session, users: UsersCreate):
    new_users_data = users.model_dump()
    new_users_data["password"] = hash_password(new_users_data["password"])
    
    new_users = Users(**new_users_data)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return new_users

def create_register(db: Session, users: RegisterCreate):
    new_users_data = users.model_dump()
    new_users_data["password"] = hash_password(new_users_data["password"])
    new_users_data["role"] = "customer" 
    new_users = Users(**new_users_data)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return new_users


    """===================================================================================="""
    
""" Function untuk update data user """
def update_users(db: Session, users_id: int, users_update: UsersUpdate):
    users = get_users_by_id(db, users_id)
    if not users:
        return None

    update_data = users_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(users, key, value)

    db.commit()
    db.refresh(users)
    return users


""" Function untuk hapus data user """
def delete_users(db: Session, users_id: int):
    users = get_users_by_id(db, users_id)
    if not users:
        return None

    db.delete(users)
    db.commit()
    return users
