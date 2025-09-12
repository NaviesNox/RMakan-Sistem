from datetime import datetime
from app.model.v1.customer.customer_schemas import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse,
)

""" Simulasi database sementara """
_customer_db: list[CustomerResponse] = []
_id_counter = 1

""" Service functions untuk customer """
def get_all_customers():
    return _customer_db

""" Helper function untuk mendapatkan customer berdasarkan ID """
def get_customer_by_id(customer_id: int):
    for customer in _customer_db:
        if customer.id_customer == customer_id:
            return customer
    return None

""" Function untuk menambah customer baru  """
def create_customer(customer: CustomerCreate):
    """ Validasi: email harus unik """
    for c in _customer_db:
        if c.email == customer.email:
            raise ValueError("Email sudah digunakan customer lain")
    """ Menambahkan customer baru ke "database" """
    global _id_counter
    new_customer = CustomerResponse(
        id_customer=_id_counter,
        created_at=datetime.now(),
        **customer.model_dump(),
    )
    """ Simpan ke "database" """
    _customer_db.append(new_customer)
    _id_counter += 1
    return new_customer

""" Function untuk mengupdate data customer """
def update_customer(customer_id: int, customer_update: CustomerUpdate):
    customer = get_customer_by_id(customer_id)
    if not customer:
        return None
    """
    # Validasi email unik jika diupdate
      """
    if customer_update.email:
        for c in _customer_db:
            if c.email == customer_update.email and c.id_customer != customer_id:
                raise ValueError("Email sudah digunakan customer lain")
    """ Update fields yang diubah """
    update_data = customer_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(customer, key, value)
    """ Return updated customer """
    return customer

""" Function untuk menghapus customer """
def delete_customer(customer_id: int):
    global _customer_db
    customer = get_customer_by_id(customer_id)
    if not customer:
        return None
    """ Hapus customer dari "database" """
    _customer_db = [c for c in _customer_db if c.id_customer != customer_id]
    return customer
