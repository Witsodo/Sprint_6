import pytest
import allure
from data import ORDER_TEST_DATA


@allure.suite('Тесты создания заказа')
class TestOrderCreation:
    @allure.feature('Создание заказа через верхнюю кнопку')
    @allure.story('Оформление заказа через кнопку "Заказать" в хедере')
    @allure.title('Заказ через верхнюю кнопку для пользователя {ORDER_TEST_DATA[0]["user_data"]["name"]}')
    def test_order_creation_via_top_button(self, main_page, order_page):
        user_data = ORDER_TEST_DATA[0]["user_data"]

        main_page.click_order_button_top()
        order_page.fill_user_info(user_data)
        order_page.fill_rental_info(user_data)
        assert order_page.is_order_confirmed(), "Модальное окно подтверждения не отобразилось"

    @allure.feature('Создание заказа через нижнюю кнопку')
    @allure.story('Оформление заказа через кнопку "Заказать" в футере')
    @allure.title('Заказ через нижнюю кнопку для пользователя {ORDER_TEST_DATA[1]["user_data"]["name"]}')
    def test_order_creation_via_bottom_button(self, main_page, order_page):
        user_data = ORDER_TEST_DATA[1]["user_data"]

        main_page.click_order_button_bottom()
        order_page.fill_user_info(user_data)
        order_page.fill_rental_info(user_data)
        assert order_page.is_order_confirmed(), "Модальное окно подтверждения не отобразилось"