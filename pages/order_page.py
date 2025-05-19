from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Заполнение информации о пользователе
    def fill_user_info(self, user_data):

        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NAME_INPUT)).send_keys(user_data["name"])
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.LAST_NAME_INPUT)).send_keys(user_data["last_name"])
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ADDRESS_INPUT)).send_keys(user_data["address"])

        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_INPUT)).click()
        metro_locator = (
OrderPageLocators.METRO_STATION[0], OrderPageLocators.METRO_STATION[1].format(user_data["metro"]))
        self.wait.until(EC.element_to_be_clickable(metro_locator)).click()

        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.PHONE_INPUT)).send_keys(user_data["phone"])
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)).click()

    # Заполнение информации об аренде
    def fill_rental_info(self, user_data):

        # 1. Заполнение даты
        date_input = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DATE_INPUT))
        date_input.click()
        date_input.clear()
        date_input.send_keys(user_data["date"])

        # 2. Закрытие календаря (клик в другое место)
        header = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DATE_PICKER_HEADER))
        header.click()

        # 3. Выбор срока аренды
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD))
        ActionChains(self.driver).move_to_element(dropdown).click().perform()

        period_locator = (
            OrderPageLocators.PERIOD_OPTION[0],
            OrderPageLocators.PERIOD_OPTION[1].format(user_data["period"])
        )
        self.wait.until(EC.element_to_be_clickable(period_locator)).click()

        # 4. Выбор цвета
        if user_data["color"] == "black":
            self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COLOR_BLACK)).click()
        else:
            self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COLOR_GREY)).click()

        # 5. Заполнение комментария
        if user_data.get("comment"):
            self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COMMENT_INPUT)).send_keys(user_data["comment"])

        # 6. Подтверждение заказа
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)).click()

    # Проверка подтверждения заказа (только проверка видимости элемента)
    def is_order_confirmed(self):

        return self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)).is_displayed()