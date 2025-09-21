from sqlalchemy.orm import Session
from app.model.v1.reservation.reservation_schemas import (
    ReservationCreate,
    ReservationUpdate,
)
from models import Reservation


""" Fungsi untuk mengambil semua reservasi """
def get_all_reservations(db: Session):
    return db.query(Reservation).all()


""" Fungsi untuk mengambil reservasi berdasarkan ID """
def get_reservation_by_id(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()


""" Fungsi untuk membuat reservasi baru """
def create_reservation(db: Session, reservation: ReservationCreate):
    new_reservation = Reservation(**reservation.model_dump())
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation


""" Fungsi untuk memperbarui reservasi """
def update_reservation(db: Session, reservation_id: int, reservation_update: ReservationUpdate):
    reservation = get_reservation_by_id(db, reservation_id)
    if not reservation:
        return None

    update_data = reservation_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(reservation, key, value)

    db.commit()
    db.refresh(reservation)
    return reservation


""" Fungsi untuk menghapus reservasi """
def delete_reservation(db: Session, reservation_id: int):
    reservation = get_reservation_by_id(db, reservation_id)
    if not reservation:
        return None

    db.delete(reservation)
    db.commit()
    return reservation
