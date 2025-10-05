"""
Payment Schema
--------------
Schema untuk entitas Payment.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum



class PaymentMethodEnum(str, Enum):
    cash = "cash"
    card = "card"
    e_wallet = "e_wallet"


class PaymentStatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"


class PaymentBase(BaseModel):
    """Schema dasar untuk Payment"""
    id_reservation: int
    amount: float 
    method: PaymentMethodEnum
    status: PaymentStatusEnum
    transaction_time: datetime


class PaymentCreate(PaymentBase):
    """Schema untuk membuat pembayaran baru"""
    pass


class PaymentUpdate(BaseModel):
    """Schema untuk update data payment"""
    id_reservation: int | None = None
    amount: float | None = None
    method: PaymentMethodEnum | None = None
    status: PaymentStatusEnum | None = None
    transaction_time: datetime | None = None


class PaymentResponse(PaymentBase):
    """Schema response payment dari DB"""
    id: int

    class ConfigDict:
        from_attributes = True
