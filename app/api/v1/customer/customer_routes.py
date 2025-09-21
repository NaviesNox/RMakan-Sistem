from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.model.v1.customer.customer_schemas import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse,
)
from app.api.v1.customer import customer_service
from app.core.auth import verify_token, require_role

router = APIRouter(tags=["Customer"])

# customer_routes.py
@router.get("/my-reservations")
def my_reservations(token_data = Depends(verify_token)):
    return {"user_id": token_data.user_id, "role": token_data.role}


"""GET /customer = semua customer"""
@router.get("/", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return customer_service.get_all_customers(db)


""" GET /customer/{id} = detail customer"""
@router.get("/{id}", response_model=CustomerResponse)
def get_customer(id: int, db: Session = Depends(get_db)):
    customer = customer_service.get_customer_by_id(db, id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer tidak ditemukan")
    return customer


""" POST /customer = tambah customer baru """
@router.post("/", response_model=CustomerResponse, status_code=201)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    try:
        return customer_service.create_customer(db, customer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


""" /customer/{id} → update customer """
@router.put("/{id}", response_model=CustomerResponse)
def update_customer(id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    try:
        updated_customer = customer_service.update_customer(db, id, customer)
        if not updated_customer:
            raise HTTPException(status_code=404, detail="Customer tidak ditemukan")
        return updated_customer
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


""" DELETE /customer/{id} → hapus customer """
@router.delete("/{id}", response_model=CustomerResponse)
def delete_customer(id: int, db: Session = Depends(get_db)):
    deleted_customer = customer_service.delete_customer(db, id)
    if not deleted_customer:
        raise HTTPException(status_code=404, detail="Customer tidak ditemukan")
    return deleted_customer
