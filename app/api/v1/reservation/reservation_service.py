from app.model.v1.reservation.reservation_schemas import (
    ReservationCreate,
    ReservationUpdate,
    ReservationResponse,
)

# Simulasi database
_reservation_db: list[ReservationResponse] = []
_id_counter = 1

""" Fungsi untuk mengambil semua reservasi """
def get_all_reservations():
    return _reservation_db

""" Fungsi untuk mengambil reservasi berdasarkan ID """
def get_reservation_by_id(reservation_id: int):
    for reservation in _reservation_db:
        if reservation.id == reservation_id:
            return reservation
    return None

""" Fungsi untuk membuat reservasi baru """
def create_reservation(reservation: ReservationCreate):
    global _id_counter
    new_reservation = ReservationResponse(id=_id_counter, **reservation.dict())
    _reservation_db.append(new_reservation)
    _id_counter += 1
    return new_reservation

""" Fungsi untuk memperbarui reservasi """
def update_reservation(reservation_id: int, reservation_update: ReservationUpdate):
    reservation = get_reservation_by_id(reservation_id)
    if not reservation:
        return None
    """ Perbarui hanya field yang disediakan """
    update_data = reservation_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(reservation, key, value)

    return reservation

""" Fungsi untuk menghapus reservasi """
def delete_reservation(reservation_id: int):
    global _reservation_db
    reservation = get_reservation_by_id(reservation_id)
    if not reservation:
        return None

    _reservation_db = [r for r in _reservation_db if r.id != reservation_id]
    return reservation
