import allure
import requests

from clients.auth_client import AuthClient
from config.headers import Headers
from endpoints.auth_endpoints import AuthEndpoint
from entity.user import LoginRequest, LoginResponse, User


class TestAuth:

    @allure.title("Успешная авторизация")
    def test_success_login(self):
        response = AuthClient.login("emilys", "emilyspass")
        assert response.status_code == 200
        data = LoginResponse(**response.json())
        assert data.accessToken is not None

    @allure.title("Неуспешная авторизация")
    def test_failed_login(self):
        response = AuthClient.login("emilys", "wrong_password")
        assert response.status_code == 401
        assert "accessToken" not in response.json()

    @allure.title("Получение текущего пользователя с токеном")
    def test_get_me_with_token(self, auth_user):
        assert auth_user is not None
        assert auth_user.username == "emilys"
        assert auth_user.id is not None


    @allure.title("Получение текущего пользователя без токена")
    def test_get_me_without_token(self):
        response = AuthClient.get_me(token="")
        assert response.status_code == 401
        assert "Access Token is required" in response.text








