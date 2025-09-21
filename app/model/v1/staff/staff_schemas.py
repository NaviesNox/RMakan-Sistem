"""
Staff Schema
------------
Schema untuk entitas Staff.
"""

from pydantic import BaseModel, Field
from enum import Enum 




class RoleEnum(str, Enum):
    admin = "admin"
    waiter = "waiter"
    manager = "manager"
    reservationstaff = "reservationstaff"



class StaffBase(BaseModel):
    """Schema dasar untuk Staff"""
    name: str = Field(..., example="Budi")
    username: str 
    password: str
    role: RoleEnum
    phone: str = Field(..., example="08123456789")


class StaffCreate(StaffBase):
    """Schema untuk membuat staff baru"""
    pass


class StaffUpdate(BaseModel):
    """Schema untuk update data staff"""
    name: str | None = None
    username: str | None = None
    passsword: str | None = None
    role: RoleEnum | None = None
    phone: str | None = None


class StaffResponse(StaffBase):
    """Schema response staff dari DB"""
    id: int

    class Config:
        from_attributes = True

