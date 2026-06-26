import requests
from endpoints.auth_endpoints import AuthEndpoint


class AuthClient:

    @staticmethod
    def login(username: str, password: str):
        url = AuthEndpoint.LOGIN
        payload = {
            "username": username,
            "password": password
        }
        headers = {"Content-Type": "application/json"}
        return requests.post(url, json=payload, headers=headers)

    @staticmethod
    def get_me(token: str):
        url = AuthEndpoint.ME
        headers = {"Authorization": f"Bearer {token}"}
        return requests.get(url, headers=headers)

    @staticmethod
    def refresh(refresh_token: str, expires_in_mins: int = 60):
        url = AuthEndpoint.REFRESH
        payload = {
            "refreshToken": refresh_token,
            "expiresInMins": expires_in_mins
        }
        headers = {"Content-Type": "application/json"}
        return requests.post(url, json=payload, headers=headers)
