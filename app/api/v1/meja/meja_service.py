from sqlalchemy.orm import Session
from app.model.v1.meja.meja_schemas import (         
    MejaCreate,   
    MejaUpdate,   
)
from models import Meja


def get_all_meja(db: Session):
    """Service functions untuk meja"""
    return db.query(Meja).all()

def get_available_meja(db: Session):
    """Service function untuk mendapatkan semua meja yang statusnya tersedia"""
    """Jika tidak ada meja yang tersedia, return massage "saat ini tidak ada meja yang tersedia" """
    if not db.query(Meja).filter(Meja.status == 'tersedia').all():
        return "Saat ini tidak ada meja yang tersedia"
    return db.query(Meja).filter(Meja.status == 'tersedia').all()
   
    


def get_meja_by_id(db: Session, meja_id: int):
    """Helper function untuk mendapatkan meja berdasarkan ID"""
    return db.query(Meja).filter(Meja.id == meja_id).first()


def create_meja(db: Session, meja: MejaCreate):
    """Function untuk menambah meja baru"""
    new_meja = Meja(**meja.model_dump())
    db.add(new_meja)

    """ check apakah table number yang diinput sudah ada atau belum, jika sudah ada maka return pesan "table number sudah ada" """
    existing_meja = db.query(Meja).filter(Meja.table_number == meja.table_number).first()
    if existing_meja:
        raise ValueError("Table number sudah ada")

    db.commit()
    db.refresh(new_meja)
    return new_meja


def update_meja(db: Session, meja_id: int, meja_update: MejaUpdate):
    """Function untuk mengupdate data meja"""
    meja = get_meja_by_id(db, meja_id)
    if not meja:
        return None

    update_data = meja_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(meja, key, value)

    db.commit()
    db.refresh(meja)
    return meja


def delete_and_return_meja(db: Session, meja_id: int):
    """Function untuk menghapus meja"""
    meja = get_meja_by_id(db, meja_id)
    if not meja:
        return None

    db.delete(meja)
    db.commit()
    return meja
