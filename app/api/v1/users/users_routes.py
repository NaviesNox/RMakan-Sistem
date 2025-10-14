from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.model.v1.users.users_schemas import  UsersCreate,  UsersUpdate,  UsersResponse
from app.api.v1.users import users_service
from app.model.v1.users.users_schemas import DeleteUserResponse
from models import Users
from app.core.auth import get_current_user, get_current_admin, get_current_manager, get_current_petugas, get_current_reservationStaff
from uuid import UUID

router = APIRouter( tags=["User"])



""" GET /user = daftar user """
@router.get("/", response_model=list[UsersResponse])
def list_users(db: Session = Depends(get_db),
               user: Users = Depends(get_current_manager)
               ):
    return users_service.get_all_users(db)
"""=============================PROFILE TERITORI====================================="""
@router.get("/profile/", response_model=UsersResponse)
def get_profile(current_user: Users = Depends(get_current_user)):
    return current_user



@router.patch("/profile/", response_model=UsersResponse)
def update_profile(users_update: UsersUpdate, db: Session= Depends(get_db), current_user: Users = Depends(get_current_user)):
    updated_users = users_service.update_users(db, current_user.id, users_update)
    if not updated_users:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return updated_users

"""=============================PROFILE TERITORI====================================="""



""" GET /user/{uuid} = detail user """
@router.get("/{uuid}", response_model=UsersResponse)
def get_users(id:UUID, db: Session = Depends(get_db),
              current_manager: Users= Depends(get_current_manager)
              ):
    users = users_service.get_users_by_id(db, id)
    if not users:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return users


""" POST /user = tambah user"""
@router.post("/", response_model=UsersResponse, status_code=201)
def create_users(users: UsersCreate, db: Session = Depends(get_db),
                 current_admin: Users = Depends(get_current_admin)
                 ):
    return users_service.create_users(db, users)



""" PUT /user/{uuid} = update user"""
@router.patch("/{uuid}", response_model=UsersResponse)
def update_users(id: UUID, users: UsersUpdate, db: Session = Depends(get_db),
                 current_admin: Users = Depends(get_current_admin)
                 ):
    updated_users = users_service.update_users(db, id, users)
    if not updated_users:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return updated_users



@router.delete("/{uuid}", response_model=DeleteUserResponse)
def delete_users(id: UUID, db: Session = Depends(get_db),
                 current_admin: Users = Depends(get_current_admin)):
    deleted_user = users_service.delete_and_return_user(db, id)
    if deleted_user:
        return {
            "detail": "User deleted successfully",
            "data": deleted_user
        }
    raise HTTPException(status_code=404, detail="User tidak ditemukan")