import allure

import config.credentials as credentials
from clients.auth_client import AuthClient
from entity.user import LoginResponse


class TestAuth:

    @allure.title("Успешная авторизация")
    def test_success_login(self):
        response = AuthClient.login(credentials.USERNAME, credentials.PASSWORD)
        assert response.status_code == 200
        data = LoginResponse(**response.json())
        assert data.accessToken is not None

    @allure.title("Неуспешная авторизация")
    def test_failed_login(self):
        response = AuthClient.login(credentials.USERNAME, credentials.WRONG_PASSWORD)
        assert response.status_code == 400
        assert "accessToken" not in response.json()

    @allure.title("Получение текущего пользователя с токеном")
    def test_get_me_with_token(self, get_me_response):
        assert get_me_response is not None
        assert get_me_response.username == credentials.USERNAME

    @allure.title("Получение текущего пользователя без токена")
    def test_get_me_without_token(self):
        response = AuthClient.get_me(token="")
        assert response.status_code == 401
        assert "Invalid/Expired Token!" in response.text

    @allure.title("Обновление сесси аутентификации")
    def test_refresh_token(self, login_response):
        refresh_response = AuthClient.refresh(login_response.refreshToken)
        assert refresh_response.status_code == 200
        new_token = refresh_response.json()["accessToken"]
        me_response = AuthClient.get_me(new_token)
        assert me_response.status_code == 200
