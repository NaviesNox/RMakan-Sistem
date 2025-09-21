from datetime import datetime
from app.model.v1.customer.customer_schemas import (
    CustomerCreate,
    CustomerUpdate
)
from sqlalchemy.orm import Session
from models import Customer
from fastapi import HTTPException, status
from app.core.security import hash_password
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_customer(db: Session, username: str, password: str):
    user = db.query(Customer).filter(Customer.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


""" Service functions untuk customer """
def get_all_customers(db: Session):
    return db.query(Customer).all()

""" Helper function untuk mendapatkan customer berdasarkan ID """
def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id_customer == customer_id).first()

""" Function untuk menambah customer baru  """
def create_customer(db: Session, customer: CustomerCreate):
    # Validasi email & username
    if db.query(Customer).filter(Customer.email == customer.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email sudah digunakan")
    if db.query(Customer).filter(Customer.username == customer.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username sudah digunakan")

    data = customer.model_dump()
    data["password"] = hash_password(data["password"])
    new_customer = Customer(**data)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

""" Function untuk mengupdate data customer """
def update_customer(db: Session, customer_id: int, customer_update: CustomerUpdate):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        return None
    """
    # Validasi email unik jika diupdate
      """
    if customer_update.email:
        existing = (
            db.query(Customer)
            .filter(Customer.email == customer_update.email, Customer.id_customer != customer_id)
            .first()
        )
        if existing:
            raise ValueError("Email sudah digunakan customer lain")
    """ Update fields yang diubah """
    update_data = customer_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(customer, key, value)

    db.commit()
    db.refresh(customer)
    """ Return updated customer """
    return customer

""" Function untuk menghapus customer """
def delete_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        return None
    """ Hapus customer dari "database" """
    db.delete(customer)
    db.commit()
    return customer