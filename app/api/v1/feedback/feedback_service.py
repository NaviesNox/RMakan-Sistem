from datetime import datetime
from app.model.v1.feedback.feedback_schemas import (
    FeedbackCreate,
    FeedbackUpdate,
    FeedbackResponse,
)

# Simulasi database sementara
_feedback_db: list[FeedbackResponse] = []
_id_counter = 1

""" Service functions untuk feedback """
def get_all_feedback():
    return _feedback_db

""" Helper function untuk mendapatkan feedback berdasarkan ID """
def get_feedback_by_id(feedback_id: int):
    for feedback in _feedback_db:
        if feedback.id == feedback_id:
            return feedback
    return None

""" Function untuk menambah feedback baru """
def create_feedback(feedback: FeedbackCreate):
    global _id_counter
    new_feedback = FeedbackResponse(
        id=_id_counter,
        created_at=datetime.now(),
        **feedback.model_dump(),
    )
    """ Simpan ke "database" """
    _feedback_db.append(new_feedback)
    _id_counter += 1
    return new_feedback

""" Function untuk mengupdate data feedback """
def update_feedback(feedback_id: int, feedback_update: FeedbackUpdate):
    feedback = get_feedback_by_id(feedback_id)
    if not feedback:
        return None
    """ Update fields yang diubah """
    update_data = feedback_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(feedback, key, value)

    return feedback

""" Function untuk menghapus feedback """
def delete_feedback(feedback_id: int):
    global _feedback_db
    feedback = get_feedback_by_id(feedback_id)
    if not feedback:
        return None
    """ini Hapus feedback dari "database" """
    _feedback_db = [f for f in _feedback_db if f.id != feedback_id]
    return feedback
