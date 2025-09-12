from fastapi import APIRouter, HTTPException
from app.model.v1.meja.meja_schemas import MejaCreate, MejaUpdate, MejaResponse
from app.api.v1.meja import meja_service

router = APIRouter(tags=["Meja"])

""" GET /meja = semua meja """
@router.get("/", response_model=list[MejaResponse])
def list_meja():
    return meja_service.get_all_meja()

""" GET /meja/{id} = detail meja """
@router.get("/{id}", response_model=MejaResponse)
def get_meja(id: int):
    meja = meja_service.get_meja_by_id(id)
    if not meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return meja

""" POST /meja = tambah meja baru """
@router.post("/", response_model=MejaResponse, status_code=201)
def create_meja(meja: MejaCreate):
    return meja_service.create_meja(meja)

""" PUT /meja/{id} = update meja """
@router.put("/{id}", response_model=MejaResponse)
def update_meja(id: int, meja: MejaUpdate):
    updated_meja = meja_service.update_meja(id, meja)
    if not updated_meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return updated_meja

""" DELETE /meja/{id} = hapus meja """
@router.delete("/{id}", response_model=MejaResponse)
def delete_meja(id: int):
    deleted_meja = meja_service.delete_meja(id)
    if not deleted_meja:
        raise HTTPException(status_code=404, detail="Meja tidak ditemukan")
    return deleted_meja
