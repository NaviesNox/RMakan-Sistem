from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_payments(auth_token):
    response = client.get(
        "/payment/",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_payment_by_id(auth_token):
    # Pertama, buat payment baru untuk diuji
    create_response = client.post(
        "/payment/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_reservation": 8,
            "amount": 150.00,
            "method": "card",
            "status": "completed",
            "transaction_time": "2024-10-15T14:30:00"
        }
    )
    payment_id = create_response.json()["id"]

    # Kemudian, ambil payment berdasarkan ID
    response = client.get(
        f"/payment/{payment_id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    payment = response.json()
    assert payment["id"] == payment_id
    assert payment["id_reservation"] == 8
    assert payment["amount"] == 150.00
    assert payment["method"] == "card"
    assert payment["status"] == "completed"
    assert payment["transaction_time"] == "2024-10-15T14:30:00"

def test_create_payment(auth_token):
    response = client.post(
        "/payment/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_reservation": 7,
            "amount": 200.00,
            "method": "cash",
            "status": "pending",
            "transaction_time": "2024-11-01T12:00:00"
        }
    )
    assert response.status_code == 201
    payment = response.json()
    assert payment["id_reservation"] == 7
    assert payment["amount"] == 200.00
    assert payment["method"] == "cash"
    assert payment["status"] == "pending"
    assert payment["transaction_time"] == "2024-11-01T12:00:00"
    assert "id" in payment

def test_update_payment(auth_token):
    # Pertama, buat payment baru untuk diupdate
    create_response = client.post(
        "/payment/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_reservation": 6,
            "amount": 300.00,
            "method": "card",
            "status": "pending",
            "transaction_time": "2024-12-01T15:00:00"
        }
    )
    payment_id = create_response.json()["id"]

    # Kemudian, update payment tersebut
    update_response = client.patch(
        f"/payment/{payment_id}",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "amount": 350.00,
            "status": "completed"
        }
    )
    assert update_response.status_code == 200
    updated_payment = update_response.json()
    assert updated_payment["id"] == payment_id
    assert updated_payment["id_reservation"] == 6
    assert updated_payment["amount"] == 350.00
    assert updated_payment["method"] == "card"
    assert updated_payment["status"] == "completed"
    assert updated_payment["transaction_time"] == "2024-12-01T15:00:00"

def test_delete_payment(auth_token):
    # Pertama, buat payment baru untuk dihapus
    create_response = client.post(
        "/payment/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_reservation": 5,
            "amount": 400.00,
            "method": "cash",
            "status": "pending",
            "transaction_time": "2024-12-15T10:00:00"
        }
    )
    payment_id = create_response.json()["id"]

    # Kemudian, hapus payment tersebut
    delete_response = client.delete(
        f"/payment/{payment_id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert delete_response.status_code == 200

    # Verifikasi bahwa payment telah dihapus
    get_response = client.get(
        f"/payment/{payment_id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert get_response.status_code == 404