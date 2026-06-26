import pytest

import config.credentials as credentials
from clients.auth_client import AuthClient
from entity.user import LoginResponse, User

@pytest.fixture
def login_response():
    response = AuthClient.login(credentials.USERNAME, credentials.PASSWORD)
    return LoginResponse(**response.json())

@pytest.fixture
def get_me_response(login_response):
    response = AuthClient.get_me(login_response.accessToken)
    return User(**response.json())

@pytest.fixture
