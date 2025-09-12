from pydantic import BaseModel, Field, EmailStr, constr
from typing_extensions import Annotated
from typing import Optional
from datetime import datetime


class CustomerBase(BaseModel):
    """Schema dasar untuk Customer"""
    name: str = Field(..., example="John Doe")
    phone: Annotated[str, Field(pattern=r"^\d{10,15}$", example="08123456789")]  # hanya angka, 10-15 digit
    email: EmailStr = Field(..., description="Email unik customer")


class CustomerCreate(CustomerBase):
    """Schema untuk membuat customer baru"""
    pass


class CustomerUpdate(BaseModel):
    """Schema untuk update data customer"""
    name: Optional[str] = Field(None, example="John Doe")
    phone: Optional[Annotated[str, Field(pattern=r"^\d{10,15}$", example="08123456789")]] = None
    email: Optional[EmailStr] = Field(None, description="Email unik customer")


class CustomerResponse(CustomerBase):
    """Schema response customer dari DB"""
    id_customer: int
    created_at: datetime

    class Config:
        orm_mode = True
