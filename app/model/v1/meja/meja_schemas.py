"""
Meja Schema
-----------
Schema untuk entitas Meja.
"""

from pydantic import BaseModel, Field
from enum import Enum


class LocationEnum(str, Enum):
    indoor = "indoor"
    outdoor = "outdoor"
    vip = "vip"



class StatusEnum(str, Enum):
    tersedia = "tersedia"
    tidaktersedia = "tidaktersedia"



class MejaBase(BaseModel):
    """Schema dasar untuk Meja"""
    kode_meja: str = Field(..., description="Nomor meja unik")
    capacity: int = Field(..., gt=0, description="Kapasitas kursi")
    location: LocationEnum = Field(..., description="Lokasi meja")
    status: StatusEnum = Field(..., description="Status ketersediaan")


class MejaCreate(MejaBase):
    """Schema untuk membuat meja baru"""
    pass


class MejaUpdate(BaseModel):
    """Schema untuk update data meja"""
    kode_meja: int | None = None
    capacity: int | None = None
    location: LocationEnum | None = None
    status: StatusEnum | None = None


class MejaResponse(MejaBase):
    """Schema response meja dari DB"""
    id: int

    class ConfigDict:
          from_attributes = True

class MejaDeleteResponse(BaseModel):
    detail: str
    data: MejaResponse

    class ConfigDict:
        from_attributes = True