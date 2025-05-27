from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
import allure


class OrderPage(BasePage):  # Наследуемся от BasePage
    @allure.step("Заполнить информацию о пользователе")
    def fill_user_info(self, user_data):
        self._fill_name(user_data["name"])
        self._fill_last_name(user_data["last_name"])
        self._fill_address(user_data["address"])
        self._select_metro(user_data["metro"])
        self._fill_phone(user_data["phone"])
        self._click_next_button()

    @allure.step("Ввести имя: {name}")
    def _fill_name(self, name):
        self.input_text(OrderPageLocators.NAME_INPUT, name)

    @allure.step("Ввести фамилию: {last_name}")
    def _fill_last_name(self, last_name):
        self.input_text(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Ввести адрес: {address}")
    def _fill_address(self, address):
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Выбрать станцию метро: {station}")
    def _select_metro(self, station):
        self.click_element(OrderPageLocators.METRO_INPUT)
        metro_locator = (
            OrderPageLocators.METRO_STATION[0],
            OrderPageLocators.METRO_STATION[1].format(station)
        )
        self.click_element(metro_locator)

    @allure.step("Ввести телефон: {phone}")
    def _fill_phone(self, phone):
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def _click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить информацию об аренде")
    def fill_rental_info(self, user_data):
        self._set_delivery_date(user_data["date"])
        self._select_rental_period(user_data["period"])
        self._select_scooter_color(user_data["color"])
        if user_data.get("comment"):
            self._add_comment(user_data["comment"])
        self._confirm_order()

    @allure.step("Установить дату доставки: {date}")
    def _set_delivery_date(self, date):
        self.click_element(OrderPageLocators.DATE_INPUT)
        self.input_text(OrderPageLocators.DATE_INPUT, date)  # метод базового класса
        self.click_element(OrderPageLocators.DATE_PICKER_HEADER)  # Клик вне календаря

    @allure.step("Выбрать срок аренды: {period}")
    def _select_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        period_locator = (OrderPageLocators.PERIOD_OPTION[0],
                         OrderPageLocators.PERIOD_OPTION[1].format(period))
        self.click_element(period_locator)

    @allure.step("Выбрать цвет самоката: {color}")
    def _select_scooter_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        else:
            self.click_element(OrderPageLocators.COLOR_GREY)

    @allure.step("Добавить комментарий: {comment}")
    def _add_comment(self, comment):
        self.input_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Подтвердить заказ")
    def _confirm_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить подтверждение заказа")
    def is_order_confirmed(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL)