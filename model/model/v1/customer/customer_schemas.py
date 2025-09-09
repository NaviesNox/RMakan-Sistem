"""
Customer Schema
---------------
Schema untuk entitas Customer.
"""

from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class CustomerBase(BaseModel):
    """Schema dasar untuk Customer"""
    name: str = Field(..., example="John Doe")
    phone: str = Field(..., example="08123456789")
    email: EmailStr = Field(..., description="Email unik customer")


class CustomerCreate(CustomerBase):
    """Schema untuk membuat customer baru"""
    pass


class CustomerUpdate(BaseModel):
    """Schema untuk update data customer"""
    name: str | None = None
    phone: str | None = None
    email: EmailStr | None = None


class CustomerResponse(CustomerBase):
    """Schema response customer dari DB"""
    id_customer: int
    created_at: datetime

    class Config:
        orm_mode = True
