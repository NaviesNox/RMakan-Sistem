from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.model.v1.users.users_schemas import  UsersCreate,  UsersUpdate,  UsersResponse
from app.api.v1.users import users_service
from app.model.v1.users.users_schemas import DeleteUserResponse
from models import Users
from app.core.auth import get_current_user, get_current_admin

router = APIRouter( tags=["User"])



""" GET /user = daftar user """
@router.get("/", response_model=list[UsersResponse])
def list_users(db: Session = Depends(get_db),
               current_admin: Users = Depends(get_current_admin)
               ):
    return users_service.get_all_users(db)
"""=============================PROFILE TERITORI====================================="""
@router.get("/profile", response_model=UsersResponse)
def get_profile(current_user: Users = Depends(get_current_user)):
    return current_user



@router.patch("/profile/", response_model=UsersResponse)
def update_profile(users_update: UsersUpdate, db: Session= Depends(get_db), current_user: Users = Depends(get_current_user)):
    updated_users = users_service.update_users(db, current_user.id, users_update)
    if not updated_users:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return updated_users

"""=============================PROFILE TERITORI====================================="""



""" GET /user/{id} = detail user """
@router.get("/{id}", response_model=UsersResponse)
def get_users(id: int, db: Session = Depends(get_db),
              current_admin: Users= Depends(get_current_admin)
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



""" PUT /user/{id} = update user"""
@router.patch("/{id}", response_model=UsersResponse)
def update_users(id: int, users: UsersUpdate, db: Session = Depends(get_db),
                 current_admin: Users = Depends(get_current_admin)
                 ):
    updated_users = users_service.update_users(db, id, users)
    if not updated_users:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return updated_users



@router.delete("/{id}", response_model=DeleteUserResponse)
def delete_users(id: int, db: Session = Depends(get_db),
                 current_admin: Users = Depends(get_current_admin)):
    deleted_user = users_service.delete_and_return_user(db, id)
    if deleted_user:
        return {
            "detail": "User deleted successfully",
            "data": deleted_user
        }
    raise HTTPException(status_code=404, detail="User tidak ditemukan")