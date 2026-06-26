from config.settings import BASE_URL


class CartEndpoint:
    GET_CARTS = f"{BASE_URL}/carts"
    GET_1_CART = f"{BASE_URL}/carts/1"
    GET_USER_CART = f"{BASE_URL}/carts/user/5"
    POST_CART = f"{BASE_URL}/carts/add"
    PUT_CART = f"{BASE_URL}/carts/1"
    DELETE_CART = f"{BASE_URL}/carts/1"
