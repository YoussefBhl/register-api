import base64
from fastapi.testclient import TestClient

from app.main import app

email = "hellossss@wrold.com"
password = "password"

def test_create_user():
    with TestClient(app) as client:
        response = client.post(
            "/users/",
            json={"email": email, "password": password},
        )
        assert response.status_code == 200
        json = response.json()
        assert json['email'] == email
        assert json['status'] == 'pending'

def test_create_already_exist_user():
    with TestClient(app) as client:
        client.post(
            "/users/",
            json={"email": email, "password": password},
        )
        response = client.post(
            "/users/",
            json={"email": email, "password": password},
        )
        assert response.status_code == 409

def test_confirm_code_bad_authorization():
    with TestClient(app) as client:
        
        client.post(
            "/users/",
            json={"email": email, "password": password},
        )

        encoded = base64.b64encode(b'data to be encoded')
        response = client.post(
            "/users/confirm-code/",
            headers={"Authorization": "Basic none"},
            json={"email": email, "password": "test"},
        )
        assert response.status_code == 401
