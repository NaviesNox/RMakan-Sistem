from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_list_feedback(auth_token):
    response = client.get(
        "/feedback/",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():  # Pastikan ada data untuk diuji
        feedback = response.json()[0]
        assert "id" in feedback
        assert "id_reservation" in feedback
        assert "rating" in feedback
        assert "comment" in feedback
        assert "created_at" in feedback
        assert "id_users" in feedback


def test_create_feedback(auth_token):
    response = client.post(
        "/feedback/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_users": 9,
            "id_reservation": 2,
            "rating": 5,
            "comment": "Layanan sangat baik!"
        }
    )
    assert response.status_code == 201
    feedback = response.json()
    assert feedback["id_users"] == 9
    assert feedback["id_reservation"] == 2
    assert feedback["rating"] == 5
    assert feedback["comment"] == "Layanan sangat baik!"
    assert "id" in feedback

def test_update_feedback(auth_token):
    # Pertama, buat feedback baru untuk diupdate
    create_response = client.post(
        "/feedback/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_users": 9,
            "id_reservation": 2,
            "rating": 4,
            "comment": "Makanan enak, tapi pelayanannya biasa saja."
        }
    )
    id = create_response.json()["id"]

    # Kemudian, update feedback tersebut
    update_response = client.patch(
        f"/feedback/{id}",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "rating": 5,
            "comment": "Sekarang pelayanannya sangat baik!"
        }
    )
    assert update_response.status_code == 200
    updated_feedback = update_response.json()
    assert updated_feedback["rating"] == 5
    assert updated_feedback["comment"] == "Sekarang pelayanannya sangat baik!"
    assert updated_feedback["id"] == id

def test_get_feedback_by_id(auth_token):
    # Pertama, buat feedback baru untuk diambil
    create_response = client.post(
        "/feedback/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_users": 9,
            "id_reservation": 4,
            "rating": 3,
            "comment": "Rasanya biasa saja."
        }
    )
    id = create_response.json()["id"]

    # Kemudian, ambil feedback tersebut berdasarkan ID
    get_response = client.get(
        f"/feedback/{id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert get_response.status_code == 200
    feedback = get_response.json()
    assert feedback["id"] == id
    assert feedback["id_users"] == 9
    assert feedback["id_reservation"] == 4
    assert feedback["rating"] == 3
    assert feedback["comment"] == "Rasanya biasa saja."

def test_delete_feedback(auth_token):
    # Pertama, buat feedback baru untuk dihapus
    create_response = client.post(
        "/feedback/",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "id_users": 9,
            "id_reservation": 4,
            "rating": 2,
            "comment": "Pelayanannya lambat."
        }
    )
    id = create_response.json()["id"]

    # Kemudian, hapus feedback tersebut
    delete_response = client.delete(
        f"/feedback/{id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert delete_response.status_code == 200

    # Pastikan feedback tersebut sudah tidak ada
    get_response = client.get(
        f"/feedback/{id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert get_response.status_code == 404