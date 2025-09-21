from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.model.v1.staff.staff_schemas import(
     StaffCreate,
     StaffUpdate, 
     StaffResponse
     )
from app.api.v1.staff import staff_service
from app.core.auth import  require_role
from  app.core.auth import TokenData 

router = APIRouter( tags=["Staff"])

@router.get("/all-reservations")
def all_reservations(token_data: TokenData = Depends(require_role("admin", "reservation_staff"))):
    return {"msg": "Staff can see all reservations"}


""" GET /staff = daftar staff """
@router.get("/", response_model=list[StaffResponse])
def list_staff(db: Session = Depends(get_db)):
    return staff_service.get_all_staff(db)


""" GET /staff/{id} = detail staff """
@router.get("/{id}", response_model=StaffResponse)
def get_staff(id: int, db: Session = Depends(get_db)):
    staff = staff_service.get_staff_by_id(db, id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff tidak ditemukan")
    return staff


""" POST /staff = tambah staff"""
@router.post("/", response_model=StaffResponse, status_code=201)
def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    return staff_service.create_staff(db, staff)


""" PUT /staff/{id} = update staff"""
@router.put("/{id}", response_model=StaffResponse)
def update_staff(id: int, staff: StaffUpdate, db: Session = Depends(get_db)):
    updated_staff = staff_service.update_staff(db, id, staff)
    if not updated_staff:
        raise HTTPException(status_code=404, detail="Staff tidak ditemukan")
    return updated_staff


"""DELETE /staff/{id} = hapus staff"""
@router.delete("/{id}", response_model=StaffResponse)
def delete_staff(id: int, db: Session = Depends(get_db)):
    deleted_staff = staff_service.delete_staff(db, id)
    if not deleted_staff:
        raise HTTPException(status_code=404, detail="Staff tidak ditemukan")
    return deleted_staff
