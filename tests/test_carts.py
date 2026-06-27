import allure
from clients.cart_client import CartClient
from entity.cart import Cart, CartListResponse, CartProductPositions


class TestCarts:

    @allure.title("Получение корзин пользователя")
    def test_get_carts_by_user_id(self):
        response = CartClient.get_cart_by_user_id(1)
        assert response.status_code == 200
        data = CartListResponse(**response.json())
        assert data.carts is not None
        assert len(data.carts) > 0

    @allure.title("Получение корзины по id")
    def test_get_cart_by_id(self):
        response = CartClient.get_cart_by_cart_id(1)
        assert response.status_code == 200
        data = Cart(**response.json())
        assert data.id is not None

    @allure.title("Создание корзины")
    def test_post_cart(self):
        products = [
            CartProductPositions(id=144, quantity=4),
            CartProductPositions(id=99, quantity=5),
        ]
        response = CartClient.post_cart(7, products)
        data = Cart(**response.json())
        assert response.status_code == 201
        assert data.id is not None

    @allure.title("Обновление корзины")
    def test_put_cart(self):
        products = [
            CartProductPositions(id=88, quantity=2),
            CartProductPositions(id=52, quantity=1),
        ]
        response = CartClient.put_cart(7, products, merge=False)
        data = Cart(**response.json())
        assert response.status_code == 200

        expected = {
            88: 2,
            52: 1,
        }

        actual = {
            product.id: product.quantity
            for product in data.products
        }

        assert actual == expected

    @allure.title("Удаление корзины")
    def test_delete_cart(self):
        response = CartClient.delete_cart(7)
        data = Cart(**response.json())
        assert response.status_code == 200
        assert data.isDeleted is True

    @allure.title("Проверка на несуществующий Cart ID")
    def test_get_cart_by_incorrect_id(self):
        response = CartClient.get_cart_by_cart_id(-99)
        assert response.status_code == 404
