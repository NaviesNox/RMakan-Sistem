"""
Staff Schema
------------
Schema untuk entitas USER.
"""
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr
from enum import Enum 
from typing import Optional
from datetime import datetime




class RoleEnum(str, Enum):
    customer = "customer"
    admin = "admin"
    waiter = "waiter"
    manager = "manager"
    reservationstaff = "reservationStaff"



class UsersBase(BaseModel):
    """Schema dasar untuk User"""
    name: str = Field(..., json_schema_extra="Budi")
    username: str 
    password: str
    role: RoleEnum
    email: EmailStr = Field(..., description="Email unik customer")
    phone: str = Field(..., json_schema_extra="08123456789")


class UsersCreate(UsersBase):
    """Schema untuk membuat User baru"""
    pass

class RegisterCreate (BaseModel):
    name: str = Field(..., json_schema_extra="Budi")
    username: str 
    password: str 
    email: EmailStr = Field(..., description="Email unik customer")
    phone: str = Field(..., json_schema_extra="08123456789")

"""=============================================================================="""
class UsersUpdate(BaseModel):
    """Schema untuk update data staff"""
    name: Optional[str] | None = None
    username: Optional[str] | None = None
    password:Optional [str] | None = None
    role: RoleEnum | None = None
    email: Optional [str] = None
    phone: Optional [str] | None = None


class UsersResponse(UsersBase):
    """Schema response user dari DB"""
    id: UUID
    created_at: datetime

    class ConfigDict:
        from_attributes = True

class DeleteUserResponse(BaseModel):
    detail: str
    data: UsersResponse