from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_list_reservations(auth_token):
    response = client.get(
        "/reservation/",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():  # Pastikan ada data untuk diuji
        reservation = response.json()[0]
        assert "id" in reservation
        assert "id_meja" in reservation
        assert "id_users" in reservation
        assert "reservation_time" in reservation
        assert "guest_count" in reservation
        assert "notes" in reservation
        assert "status" in reservation
        assert "id_staff" in reservation

def test_create_reservation(auth_token):
    response = client.post(
        "/reservation/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_meja": 6,
            "id_users": 1,
            "reservation_time": "2024-12-31T19:00:00",
            "guest_count": 4,
            "notes": "Birthday celebration",
            "status": "pending",
            "id_staff": None
        }
    )
    assert response.status_code == 201
    reservation = response.json()
    assert reservation["id_meja"] == 6
    assert reservation["id_users"] == 1
    assert reservation["reservation_time"] == "2024-12-31T19:00:00"
    assert reservation["guest_count"] == 4
    assert reservation["notes"] == "Birthday celebration"
    assert reservation["status"] == "pending"
    assert reservation["id_staff"] is None
    assert "id" in reservation

def test_get_reservation_by_id(auth_token):
    # Pertama, buat reservasi baru untuk diuji
    create_response = client.post(
        "/reservation/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_meja": 5,
            "id_users": 9,
            "reservation_time": "2024-11-30T20:00:00",
            "guest_count": 2,
            "notes": "Anniversary dinner",
            "status": "pending",
            "id_staff": None
        }
    )
    id = create_response.json()["id"]

    # Kemudian, ambil reservasi tersebut berdasarkan ID
    get_response = client.get(
        f"/reservation/{id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert get_response.status_code == 200
    reservation = get_response.json()
    assert reservation["id"] == id
    assert reservation["id_meja"] == 5
    assert reservation["id_users"] == 9
    assert reservation["reservation_time"] == "2024-11-30T20:00:00"
    assert reservation["guest_count"] == 2
    assert reservation["notes"] == "Anniversary dinner"
    assert reservation["status"] == "pending"
    assert reservation["id_staff"] is None

def test_update_reservation(auth_token):
    # Pertama, buat reservasi baru untuk diupdate
    create_response = client.post(
        "/reservation/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_meja": 18,
            "id_user": 11,
            "reservation_time": "2024-10-15T18:30:00",
            "guest_count": 3,
            "notes": "Business meeting",
            "status": "pending",
            "id_staff": None
        }
    )
    id = create_response.json()["id"]

    # Kemudian, update reservasi tersebut
    update_response = client.patch(
        f"/reservation/{id}",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "guest_count": 4,
            "notes": "Updated to 4 guests",
            "status": "confirmed",
            "id_staff": 10
        }
    )
    assert update_response.status_code == 200
    updated_reservation = update_response.json()
    assert updated_reservation["guest_count"] == 4
    assert updated_reservation["notes"] == "Updated to 4 guests"
    assert updated_reservation["status"] == "confirmed"
    assert updated_reservation["id_staff"] == 10

def test_delete_reservation(auth_token):
    # Pertama, buat reservasi baru untuk dihapus
    create_response = client.post(
        "/reservation/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_meja": 20,
            "id_user": 12,
            "reservation_time": "2024-09-20T19:30:00",
            "guest_count": 2,
            "notes": "Casual dinner",
            "status": "pending",
            "id_staff": None
        }
    )
    id = create_response.json()["id"]

    # Kemudian, hapus reservasi tersebut
    delete_response = client.delete(
        f"/reservation/{id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert delete_response.status_code == 200

    # Pastikan reservasi sudah dihapus
    get_response = client.get(
        f"/reservation/{id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert get_response.status_code == 404