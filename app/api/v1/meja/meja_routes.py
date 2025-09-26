from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.model.v1.meja.meja_schemas import (
    MejaCreate,
    MejaUpdate,
    MejaResponse
    )
from app.api.v1.meja import meja_service
from models import Users
from app.core.auth import get_current_admin

router = APIRouter(tags=["Meja"])


""" GET /meja = semua meja """
@router.get("/", response_model=list[MejaResponse])
def list_meja(db: Session = Depends(get_db)):
    return meja_service.get_all_meja(db)


""" GET /meja/{id} = detail meja """
@router.get("/{id}", response_model=MejaResponse)
def get_meja(id: int, db: Session = Depends(get_db)):
    meja = meja_service.get_meja_by_id(db, id)
    if not meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return meja


""" POST /meja = tambah meja baru """
@router.post("/", response_model=MejaResponse, status_code=201)
def create_meja(
    meja: MejaCreate,
    db: Session = Depends(get_db),
    current_admin: Users = Depends(get_current_admin)
):
    return meja_service.create_meja(db, meja)


""" PUT /meja/{id} = update meja """
@router.put("/{id}", response_model=MejaResponse)
def update_meja(
    id: int,
    meja: MejaUpdate,
    db: Session = Depends(get_db),
    current_admin: Users = Depends(get_current_admin)
):
    updated_meja = meja_service.update_meja(db, id, meja)
    if not updated_meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return updated_meja



""" DELETE /meja/{id} = hapus meja """
@router.delete("/{id}", response_model=MejaResponse)
def delete_meja(
    id: int,
    db: Session = Depends(get_db),
    current_admin: Users = Depends(get_current_admin)   
):
    deleted_meja = meja_service.delete_meja(db, id)
    if not deleted_meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return deleted_meja