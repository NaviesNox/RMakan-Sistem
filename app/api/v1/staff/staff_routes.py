from fastapi import APIRouter, HTTPException
from app.model.v1.staff.staff_schemas import StaffCreate, StaffUpdate, StaffResponse
from app.api.v1.staff import staff_service

router = APIRouter( tags=["Staff"])


""" GET /staff = daftar staff """
@router.get("/", response_model=list[StaffResponse])
def list_staff():
    return staff_service.get_all_staff()


""" GET /staff/{id} = detail staff """
@router.get("/{id}", response_model=StaffResponse)
def get_staff(id: int):
    staff = staff_service.get_staff_by_id(id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff tidak ditemukan")
    return staff


""" POST /staff = tambah staff"""
@router.post("/", response_model=StaffResponse, status_code=201)
def create_staff(staff: StaffCreate):
    return staff_service.create_staff(staff)


""" PUT /staff/{id} = update staff"""
@router.put("/{id}", response_model=StaffResponse)
def update_staff(id: int, staff: StaffUpdate):
    updated_staff = staff_service.update_staff(id, staff)
    if not updated_staff:
        raise HTTPException(status_code=404, detail="Staff tidak ditemukan")
    return updated_staff


"""DELETE /staff/{id} = hapus staff"""
@router.delete("/{id}", response_model=StaffResponse)
def delete_staff(id: int):
    deleted_staff = staff_service.delete_staff(id)
    if not deleted_staff:
        raise HTTPException(status_code=404, detail="Staff tidak ditemukan")
    return deleted_staff
