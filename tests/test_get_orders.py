import allure
from handlers.handlers import get_orders


@allure.epic("HTTP")
@allure.feature("v1/orders")
@allure.suite('Проверка ручку получения заказов')
class TestGetOrders:

    @allure.title(f'Получаем все заказы')
    def test_get_orders(
            self,
    ):
        response = get_orders()
        assert response.ok
