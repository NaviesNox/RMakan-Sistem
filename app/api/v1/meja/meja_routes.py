from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.model.v1.meja.meja_schemas import (
    MejaCreate,
    MejaUpdate,
    MejaResponse,
    MejaDeleteResponse as DeleteMejaResponse
    )
from app.api.v1.meja import meja_service
from models import Users
from app.core.auth import get_current_admin , get_current_manager, get_current_petugas

router = APIRouter(tags=["Meja"])


""" GET /meja = semua meja """
@router.get("/", response_model=list[MejaResponse])
def list_meja(db: Session = Depends(get_db)):
    return meja_service.get_all_meja(db)

"""Get all available meja/ menampilkan semua meja yang statusnya tersedia"""
@router.get("/available", response_model=list[MejaResponse])
def list_available_meja(db: Session = Depends(get_db)):
    return meja_service.get_available_meja(db)


""" GET /meja/{kode_meja} = detail meja """
@router.get("/{kode_meja}", response_model=MejaResponse)
def get_meja(kode_meja: str, db: Session = Depends(get_db)):
    meja = meja_service.get_meja_by_kode_meja(db, kode_meja)
    if not meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return meja


""" POST /meja = tambah meja baru """
@router.post("/", response_model=MejaResponse, status_code=201)
def create_meja(
    meja: MejaCreate,
    db: Session = Depends(get_db),
    current_manager : Users = Depends(get_current_manager)
):
    return meja_service.create_meja(db, meja)


""" PUT /meja/{kode_meja} = update meja """
@router.patch("/{kode_meja}", response_model=MejaResponse)
def update_meja(
    kode_meja: int,
    meja: MejaUpdate,
    db: Session = Depends(get_db),
    current_petugas: Users = Depends(get_current_petugas)
):
    updated_meja = meja_service.update_meja(db, kode_meja, meja)
    if not updated_meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return updated_meja



""" DELETE /meja/{kode_meja} = hapus meja """
@router.delete("/{kode_meja}", response_model=DeleteMejaResponse)
def delete_meja(kode_meja: str, db: Session = Depends(get_db),
                current_manager: Users = Depends(get_current_manager)):
    deleted_meja = meja_service.delete_and_return_meja(db, kode_meja)
    if deleted_meja:
        return {
            "detail": "Meja deleted successfully",
            "data": deleted_meja
        }
    raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
