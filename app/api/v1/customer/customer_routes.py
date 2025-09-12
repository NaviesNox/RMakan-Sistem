from fastapi import APIRouter, HTTPException
from app.model.v1.customer.customer_schemas import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse,
)
from app.api.v1.customer import customer_service

router = APIRouter( tags=["Customer"])


"""GET /customer = semua customer"""
@router.get("/", response_model=list[CustomerResponse])
def list_customers():
    return customer_service.get_all_customers()


""" GET /customer/{id} = detail customer"""
@router.get("/{id}", response_model=CustomerResponse)
def get_customer(id: int):
    customer = customer_service.get_customer_by_id(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer tidak ditemukan")
    return customer


""" POST /customer = tambah customer baru """
@router.post("/", response_model=CustomerResponse, status_code=201)
def create_customer(customer: CustomerCreate):
    try:
        return customer_service.create_customer(customer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


""" /customer/{id} → update customer """
@router.put("/{id}", response_model=CustomerResponse)
def update_customer(id: int, customer: CustomerUpdate):
    try:
        updated_customer = customer_service.update_customer(id, customer)
        if not updated_customer:
            raise HTTPException(status_code=404, detail="Customer tidak ditemukan")
        return updated_customer
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


""" DELETE /customer/{id} → hapus customer """
@router.delete("/{id}", response_model=CustomerResponse)
def delete_customer(id: int):
    deleted_customer = customer_service.delete_customer(id)
    if not deleted_customer:
        raise HTTPException(status_code=404, detail="Customer tidak ditemukan")
    return deleted_customer
