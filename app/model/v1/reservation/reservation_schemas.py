"""
Reservation Schema
------------------
Schema untuk entitas Reservation.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class ReservationStatusEnum(str, Enum):
    pending = "Pending"
    confirmed = "Confirmed"
    cancelled = "Cancelled"
    completed = "Completed"


class ReservationBase(BaseModel):
    """Schema dasar untuk Reservation"""
    id_customer: int = Field(..., description="ID Customer")
    id_table: int = Field(..., description="ID Meja")
    reservation_time: datetime
    guest_count: int = Field(..., gt=0)
    notes: str | None = None
    status: ReservationStatusEnum = Field(..., description="Status reservasi")


class ReservationCreate(ReservationBase):
    """Schema untuk membuat reservasi baru"""
    pass


class ReservationUpdate(BaseModel):
    """Schema untuk update reservasi"""
    id_customer: int | None = None
    id_table: int | None = None
    reservation_time: datetime | None = None
    guest_count: int | None = None
    notes: str | None = None
    status: ReservationStatusEnum | None = None


class ReservationResponse(ReservationBase):
    """Schema response reservasi dari DB"""
    id: int

    class Config:
        orm_mode = True
