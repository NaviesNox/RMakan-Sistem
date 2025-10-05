from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_list_meja(auth_token):
    response = client.get(
        "/meja/",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():  # Pastikan ada data untuk diuji
        meja = response.json()[0]
        assert "id" in meja
        assert "table_number" in meja
        assert "capacity" in meja
        assert "location" in meja
        assert "status" in meja

def test_create_meja(auth_token):
    response = client.post(
        "/meja/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "table_number": 11,
            "capacity": 4,
            "location": "vip",
            "status": "tersedia"
        }
    )
    assert response.status_code == 201
    meja = response.json()
    assert meja["table_number"] == 11
    assert meja["capacity"] == 4
    assert meja["location"] == "vip"
    assert meja["status"] == "tersedia"
    assert "id" in meja
   
def test_update_meja(auth_token):
    # Pertama, buat meja baru untuk diupdate
    create_response = client.post(
        "/meja/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "table_number": 12,
            "capacity": 2,
            "location": "indoor",
            "status": "tersedia"
        }
    )
    id = create_response.json()["id"]

    # Kemudian, update meja tersebut
    update_response = client.patch(
        f"/meja/{id}",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={

            "capacity":2,
            "status": "tidaktersedia"
        }
    )
    assert update_response.status_code == 200
    updated_meja = update_response.json()
    assert updated_meja["capacity"] == 2
    assert updated_meja["status"] == "tidaktersedia"

def test_get_meja_by_id(auth_token):
    # Pertama, buat meja baru untuk mendapatkan ID-nya
    create_response = client.post(
        "/meja/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "table_number": 13,
            "capacity": 6,
            "location": "outdoor",
            "status": "tersedia"
        }
    )
    id = create_response.json()["id"]

    # Sekarang, dapatkan meja berdasarkan ID
    response = client.get(f"/meja/{id}", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    meja = response.json()
    assert meja["id"] == id
    assert meja["table_number"] == 13
    assert meja["capacity"] == 6
    assert meja["location"] == "outdoor"
    assert meja["status"] == "tersedia"

def test_delete_meja(auth_token):
    # Pertama, buat meja baru untuk mendapatkan ID-nya
    create_response = client.post(
        "/meja/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "table_number": 14,
            "capacity": 8,
            "location": "vip",
            "status": "tersedia"
        }
    )
    id = create_response.json()["id"]

    # Sekarang, hapus meja berdasarkan ID
    delete_response = client.delete(f"/meja/{id}", headers={"Authorization": f"Bearer {auth_token}"})
    assert delete_response.status_code == 200
    delete_data = delete_response.json()
    assert delete_data["detail"] == "Meja deleted successfully"
    assert delete_data["data"]["id"] == id
    assert delete_data["data"]["table_number"] == 14
    assert delete_data["data"]["capacity"] == 8
    assert delete_data["data"]["location"] == "vip"
    assert delete_data["data"]["status"] == "tersedia"