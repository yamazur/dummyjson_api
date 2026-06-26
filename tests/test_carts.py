import allure

from clients.auth_client import AuthClient
from clients.cart_client import CartClient
from entity.cart import Cart, CartListResponse, CartProductPositions


class TestCarts:

    @allure.step("Получение корзин пользователя")
    def test_get_carts_by_user_id(self):
        response = CartClient.get_cart_by_user_id(1)
        assert response.status_code == 200
        data = CartListResponse(**response.json())
        assert data.id is not None

    @allure.step("Получение корзины по id")
    def test_get_cart_by_id(self):
        response = CartClient.get_cart_by_cart_id(1)
        assert response.status_code == 200
        data = Cart(**response.json())
        assert data.id is not None

    @allure.step("Создаие корзины")
    def test_post_cart(self):
        products = [
            CartProductPositions(id=144, quantity=4),
            CartProductPositions(id=99, quantity=5),
        ]
        response = CartClient.post_cart(7, products)
        data = Cart(**response.json())
        assert response.status_code == 200
        assert data.id is not None




