import pytest
import allure
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_TEST_DATA
from urls import BASE_URL

@allure.suite('Тесты создания заказа')
class TestOrderCreation:
    @classmethod
    def setup_class(cls):
        options = webdriver.FirefoxOptions()
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.set_window_size(1920, 1080)
        cls.main_page = MainPage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

    @pytest.mark.parametrize('test_data', ORDER_TEST_DATA)
    @allure.feature('Создание заказа самоката')
    @allure.story('Полный процесс оформления заказа')
    @allure.title('Создание заказа через {test_data[entry_point]} кнопку')
    def test_order_creation(self, test_data):
        # 1. Открытие главной страницы
        self.driver.get(BASE_URL)

        # 2. Клик по кнопке заказа
        if test_data['entry_point'] == 'top':
            self.main_page.click_order_button_top()
        else:
            self.main_page.click_order_button_bottom()

        # 3. Заполнение форм
        self.order_page.fill_user_info(test_data['user_data'])
        self.order_page.fill_rental_info(test_data['user_data'])

        # 4. Проверка подтверждения заказа
        assert self.order_page.is_order_confirmed(), "Модальное окно подтверждения не отобразилось"

        # 5. Дополнительные проверки можно добавить здесь

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()