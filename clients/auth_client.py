import requests
from endpoints.auth_endpoints import AuthEndpoint


class AuthClient:

    @staticmethod
    def login(username: str, password: str):
        return requests.post(
            AuthEndpoint.LOGIN,
            json={
                "username": username,
                "password": password
            }
        )

    @staticmethod
    def get_me(token: str):
        return requests.get(
            AuthEndpoint.ME,
            headers={"Authorization": f"Bearer {token}"}
        )