from config.settings import BASE_URL

class AuthEndpoint:
    LOGIN = f"{BASE_URL}/auth/login"
    ME = f"{BASE_URL}/auth/me"
    REFRESH = f"{BASE_URL}/auth/refresh"
