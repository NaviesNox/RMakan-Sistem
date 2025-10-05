from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from models import Users
from app.model.v1.reservation.reservation_schemas import (
    ReservationCreate,
    ReservationUpdate,
    ReservationResponse
)
from app.api.v1.reservation import reservation_service
from app.core.auth import get_current_admin, get_current_user

router = APIRouter(tags=["Reservation"])


""" GET /reservation = semua reservasi """
@router.get("/", response_model=list[ReservationResponse])
def list_reservations(db: Session = Depends(get_db),
                      current_admin: Users =Depends(get_current_admin)
                      ):
    return reservation_service.get_all_reservations(db)


""" GET /reservation/{id} = detail reservasi berdasarkan ID """
@router.get("/{id}", response_model=ReservationResponse)
def get_reservation(id: int, db: Session = Depends(get_db),
                    current_admin: Users= Depends(get_current_admin)
                    ):
    reservation = reservation_service.get_reservation_by_id(db, id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation tidak ditemukan")
    return reservation


""" POST /reservation = buat reservasi baru """
@router.post("/", response_model=ReservationResponse, status_code=201)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db),
                        current_user: Users = Depends(get_current_user)
                       ):
    return reservation_service.create_reservation(db, reservation)


""" PUT /reservation/{id} = update reservasi berdasarkan ID """
@router.patch("/{id}", response_model=ReservationResponse)
def update_reservation(id: int, reservation: ReservationUpdate, db: Session = Depends(get_db),
                       current_admin: Users = Depends(get_current_admin)
                       ):
    updated_reservation = reservation_service.update_reservation(db, id, reservation)
    if not updated_reservation:
        raise HTTPException(status_code=404, detail="Reservation tidak ditemukan")
    return updated_reservation


""" DELETE /reservation/{id} = hapus reservasi """
@router.delete("/{id}", response_model=ReservationResponse)
def delete_reservation(id: int, db: Session = Depends(get_db),
                       current_admin: Users = Depends(get_current_admin)
                       ):
    deleted_reservation = reservation_service.delete_reservation(db, id)
    if not deleted_reservation:
        raise HTTPException(status_code=404, detail="Reservation tidak ditemukan")
    return deleted_reservation
