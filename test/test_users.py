from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/user/",
        headers=headers,
        json={
            "name": "Test User",
            "username": "testuser",
            "password": "testpassword",
            "role": "customer",
            "email": "cus@gmail.com",
            "phone": "081234567800000"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert data["username"] == "testuser"
    assert data["role"] == "customer"
    assert data["email"] == "cus@gmail.com"
    assert data["phone"] == "081234567800000"

def test_get_users(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/user/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:  # Pastikan ada data untuk diuji
        assert "name" in data[0]
        assert "username" in data[0]
        assert "role" in data[0]
        assert "email" in data[0]
        assert "phone" in data[0]
        assert "id" in data[0]
        assert "created_at" in data[0]
        
def test_get_user_by_id(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Pertama, buat user untuk mendapatkan ID-nya
    create_response = client.post(
        "/user/",
        headers=headers,
        json={
            "name": "Test User 2",
            "username": "testuser2",
            "password": "testpassword2",
            "role": "customer",
            "email": "cus2@gmail.com",
            "phone": "081234567800001"
        }
    )
    assert create_response.status_code == 201
    id = create_response.json()["id"]
    # Sekarang, dapatkan user berdasarkan ID
    response = client.get(f"/user/{id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == id
    assert data["name"] == "Test User 2"
    assert data["username"] == "testuser2"
    assert data["role"] == "customer"
    assert data["email"] == "cus2@gmail.com"
    assert data["phone"] == "081234567800001"
    assert "created_at" in data

def test_update_user(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Pertama, buat user untuk mendapatkan ID-nya
    create_response = client.post(
        "/user/",
        headers=headers,
        json={
            "name": "Test User 3",
            "username": "testuser3",
            "password": "testpassword3",
            "role": "customer",
            "email": "cus3@gmail.com",
            "phone": "081234567800002"
        }
    )
    assert create_response.status_code == 201
    id = create_response.json()["id"]
    # Sekarang, update user berdasarkan ID
    response = client.patch(
        f"/user/{id}",
        headers=headers,
        json={
            "name": "Updated User 3",
            "username": "testuser3",
            "passsword": "testpassword3",
            "role": "customer",
            "email": "cus3@gmail.com",
            "phone": "081234567899999"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == id
    assert data["name"] == "Updated User 3" 
    assert data["phone"] == "081234567899999"
    assert data["username"] == "testuser3"  # Tidak berubah
    assert data["role"] == "customer"  # Tidak berubah
    assert data["email"] == "cus3@gmail.com" # Tidak berubah
    assert "created_at" in data

def test_delete_user(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Pertama, buat user untuk mendapatkan ID-nya
    create_response = client.post(
        "/user/",
        headers=headers,
        json={
            "name": "Test User 4",
            "username": "testuser4",
            "password": "testpassword4",
            "role": "customer",
            "email": "cus4@gmail.com",
            "phone": "081234567800003"
        }
    )
    assert create_response.status_code == 201
    id = create_response.json()["id"]
    # Sekarang, delete user berdasarkan ID
    response = client.delete(f"/user/{id}", headers=headers)
    assert response.status_code == 200


"""============================= USERS ROUTES PROFILE ====================================="""

def test_get_profile(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/user/profile", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "username" in data
    assert "password" in data  
    assert "role" in data
    assert "email" in data
    assert "phone" in data
    assert "id" in data
    assert "created_at" in data

def test_update_profile(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.patch(
        "/user/profile/",
        headers=headers,
        json={
            "name": "Updated Profile User",
            "phone": "081234567899998"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Profile User"
    assert data["phone"] == "081234567899998"
    assert "username" in data  # Tidak berubah
    assert "role" in data  # Tidak berubah
    assert "email" in data  # Tidak berubah
    assert "id" in data
    assert "created_at" in data