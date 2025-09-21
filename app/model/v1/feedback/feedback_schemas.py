"""
Feedback Schema
---------------
Schema untuk entitas Feedback.
"""

from pydantic import BaseModel, Field
from datetime import datetime




class FeedbackBase(BaseModel):
    """Schema dasar untuk Feedback"""
    id_customer: int = Field(..., description="ID customer yang memberikan feedback")
    id_reservation: int = Field(..., description="ID reservasi terkait feedback")
    rating: int = Field(..., ge=1, le=5, description="Rating (1-5)")
    comment: str | None = Field(None, description="Komentar feedback")




class FeedbackCreate(FeedbackBase):
    """Schema untuk membuat feedback baru"""
    pass


class FeedbackUpdate(BaseModel):
    """Schema untuk update feedback"""
    rating: int | None = Field(None, ge=1, le=5, description="Rating (1-5)")
    comment: str | None = None


class FeedbackResponse(FeedbackBase):
    """Schema response feedback dari DB"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
