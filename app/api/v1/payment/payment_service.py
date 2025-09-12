from app.model.v1.payment.payment_schemas import (
    PaymentCreate,
    PaymentUpdate,
    PaymentResponse,
)

# Simulasi database sementara
_payment_db: list[PaymentResponse] = []
_id_counter = 1

""" Fungsi untuk operasi pengambilan data pembayaran """
def get_all_payments():
    return _payment_db

""" Fungsi untuk mendapatkan pembayaran berdasarkan ID """
def get_payment_by_id(payment_id: int):
    for payment in _payment_db:
        if payment.id == payment_id:
            return payment
    return None

""" Fungsi untuk membuat pembayaran baru """
def create_payment(payment: PaymentCreate):
    global _id_counter
    new_payment = PaymentResponse(id=_id_counter, **payment.dict())
    _payment_db.append(new_payment)
    _id_counter += 1
    return new_payment

""" Fungsi untuk memperbarui pembayaran """
def update_payment(payment_id: int, payment_update: PaymentUpdate):
    payment = get_payment_by_id(payment_id)
    if not payment:
        return None
    """ Update fields that are provided """
    update_data = payment_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(payment, key, value)

    return payment

""" Fungsi untuk menghapus pembayaran """
def delete_payment(payment_id: int):
    global _payment_db
    payment = get_payment_by_id(payment_id)
    if not payment:
        return None
    """ Remove payment from the simulated database """
    _payment_db = [p for p in _payment_db if p.id != payment_id]
    return payment
