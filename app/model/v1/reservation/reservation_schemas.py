"""
Reservation Schema
------------------
Schema untuk entitas Reservation.
"""

from pydantic import BaseModel, Field, Field as json_schema_extra
from datetime import datetime
from enum import Enum  



class ReservationStatusEnum(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"


class ReservationBase(BaseModel):
    """Schema dasar untuk Reservation"""
    id_meja: int = Field(..., description="ID Meja")
    id_user: int = Field(..., description="ID Customer")
    reservation_time: datetime
    guest_count: int = Field(..., gt=0)
    notes: str | None = None


class ReservationCreate(ReservationBase):
    """Schema untuk membuat reservasi baru"""
    pass


class ReservationUpdate(BaseModel):
    """Schema untuk update reservasi"""
    id_meja: int | None = None
    reservation_time: datetime | None = None
    guest_count: int | None = None
    notes: str | None = None
    status: ReservationStatusEnum | None = None
    id_staff: int | None = None  


class ReservationResponse(ReservationBase):
    """Schema response reservasi dari DB"""
    id: int
    status: ReservationStatusEnum
    id_staff: int | None = None

    class ConfigDict:
        from_attributes = True