import requests

from endpoints.cart_endpoints import CartEndpoint
from entity.cart import CartProductRequest


class CartClient:

    @staticmethod
    def get_cart_by_user_id(user_id: int):
        url = CartEndpoint.GET_USER_CART+f"{user_id}"
        return requests.get(url)

    @staticmethod
    def get_cart_by_cart_id(cart_id: int):
        url = CartEndpoint.GET_1_CART+f"{cart_id}"
        return requests.get(url)

    @staticmethod
    def post_cart(user_id: int, products: list[CartProductRequest]):
        url = CartEndpoint.POST_CART
        payload = {
            "userId": user_id,
            "products": [product.model_dump() for product in products],
        }
        headers = {"Content-Type": "application/json"}
        return requests.post(url, json=payload, headers=headers)

    @staticmethod
    def put_cart(cart_id: int, products: list, merge: bool = False):
        url = CartEndpoint.PUT_CART+f"{cart_id}"
        payload = {
            "merge": merge,
            "products": products
        }
        headers = {"Content-Type": "application/json"}
        return requests.put(url, json=payload, headers=headers)

    @staticmethod
    def delete_cart(cart_id: int):
        url = CartEndpoint.DELETE_CART+f"{cart_id}"
        return requests.delete(url)
