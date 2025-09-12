from app.model.v1.staff.staff_schemas import StaffCreate, StaffUpdate, StaffResponse

# Penyimpanan sementara (simulasi database)
_staff_db: list[StaffResponse] = []
_id_counter = 1

""" Function untuk ambil data staff """
def get_all_staff():
    return _staff_db

""" Function untuk ambil data staff berdasarkan ID """
def get_staff_by_id(staff_id: int):
    for staff in _staff_db:
        if staff.id == staff_id:
            return staff
    return None

""" Function untuk tambah data staff """
def create_staff(staff: StaffCreate):
    global _id_counter
    new_staff = StaffResponse(id=_id_counter, **staff.dict())
    _staff_db.append(new_staff)
    _id_counter += 1
    return new_staff

""" Function untuk update data staff """
def update_staff(staff_id: int, staff_update: StaffUpdate):
    staff = get_staff_by_id(staff_id)
    if not staff:
        return None
    """ Update fields """
    update_data = staff_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(staff, key, value)

    return staff

""" Function untuk hapus data staff """
def delete_staff(staff_id: int):
    global _staff_db
    staff = get_staff_by_id(staff_id)
    if not staff:
        return None
    """ Hapus staff dari database """
    _staff_db = [s for s in _staff_db if s.id != staff_id]
    return staff
