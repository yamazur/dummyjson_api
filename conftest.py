import pytest
from clients.auth_client import AuthClient
from entity.user import LoginResponse, User


@pytest.fixture
def auth_token():
    response = AuthClient.login("emilys", "emilyspass")
    data = LoginResponse(**response.json())
    return data.accessToken

@pytest.fixture
def auth_user(auth_token):
    response = AuthClient.get_me(auth_token)
    return User(**response.json())