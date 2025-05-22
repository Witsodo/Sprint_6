from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


#Базовый класс с общими методами
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент по локатору {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти элементы по локатору {locator}")
    def find_elements(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы по локатору {locator} не найдены"
        )

    @allure.step("Найти элемент внутри родителя")
    def find_child_element(self, parent, child_locator):
        return parent.find_element(*child_locator)

    @allure.step("Кликнуть по элементу {element}")
    def click_element(self, element):
        self.wait.until(EC.element_to_be_clickable(element)).click()

    @allure.step("Получить текст элемента")
    def get_element_text(self, element):
        return self.wait.until(EC.visibility_of(element)).text

    @allure.step("Скроллить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидать кликабельности элемента {locator}")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def input_text(self, locator, text):
        element = self.wait_for_clickable(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()