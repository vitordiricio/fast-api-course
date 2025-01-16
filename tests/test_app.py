from http import HTTPStatus


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_user(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "alice",
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "vitor",
            "password": "secret",
            "email": "alice@example.com",
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "vitor",
        "email": "alice@example.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.json() == {"message": "User deleted successfully"}


def test_update_user_not_found(client):
    response = client.put(
        "/users/2",
        json={
            "username": "vitor",
            "password": "secret",
            "email": "alice@example.com",
            "id": 2,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_not_found(client):
    response = client.delete("/users/2")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
