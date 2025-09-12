from fastapi import APIRouter, HTTPException
from app.model.v1.reservation.reservation_schemas import (
    ReservationCreate,
    ReservationUpdate,
    ReservationResponse,
)
from app.api.v1.reservation import reservation_service

router = APIRouter(tags=["Reservation"])


""" GET /reservation = semua reservasi """
@router.get("/", response_model=list[ReservationResponse])
def list_reservations():
    return reservation_service.get_all_reservations()


""" GET /reservation/{id} = detail reservasi berdasarkan ID """
@router.get("/{id}", response_model=ReservationResponse)
def get_reservation(id: int):
    reservation = reservation_service.get_reservation_by_id(id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation tidak ditemukan")
    return reservation


""" POST /reservation = buat reservasi baru """
@router.post("/", response_model=ReservationResponse, status_code=201)
def create_reservation(reservation: ReservationCreate):
    return reservation_service.create_reservation(reservation)


""" PUT /reservation/{id} = update reservasi berdasarkan ID """
@router.put("/{id}", response_model=ReservationResponse)
def update_reservation(id: int, reservation: ReservationUpdate):
    updated_reservation = reservation_service.update_reservation(id, reservation)
    if not updated_reservation:
        raise HTTPException(status_code=404, detail="Reservation tidak ditemukan")
    return updated_reservation


""" DELETE /reservation/{id} = hapus reservasi """
@router.delete("/{id}", response_model=ReservationResponse)
def delete_reservation(id: int):
    deleted_reservation = reservation_service.delete_reservation(id)
    if not deleted_reservation:
        raise HTTPException(status_code=404, detail="Reservation tidak ditemukan")
    return deleted_reservation
