"""
Feedback Schema
---------------
Schema untuk entitas Feedback.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class RatingEnum(int, Enum):
    satu = 1
    dua = 2
    tiga = 3
    empat = 4
    lima = 5


class FeedbackBase(BaseModel):
    """Schema dasar untuk Feedback"""
    id_customer: int
    id_reservation: int
    rating: RatingEnum
    comment: str | None = None


class FeedbackCreate(FeedbackBase):
    """Schema untuk membuat feedback baru"""
    pass


class FeedbackUpdate(BaseModel):
    """Schema untuk update data feedback"""
    rating: RatingEnum | None = None
    comment: str | None = None


class FeedbackResponse(FeedbackBase):
    """Schema response feedback dari DB"""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
