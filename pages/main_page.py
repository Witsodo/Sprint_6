import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class MainPage(BasePage):
    @allure.step("Получить количество вопросов FAQ")
    def get_faq_count(self):
        return len(self.find_elements(MainPageLocators.FAQ_ITEMS))

    @allure.step("Получить список вопросов FAQ")
    def get_faq_questions(self):
        return self.find_elements(MainPageLocators.FAQ_HEADERS)

    @allure.step("Получить список блоков с ответами FAQ")
    def get_faq_answers(self):
        return self.find_elements(MainPageLocators.FAQ_ITEMS)

    @allure.step("Нажать на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        questions = self.find_elements(MainPageLocators.FAQ_HEADERS)
        if index >= len(questions):
            raise IndexError(f"FAQ с индексом {index} не существует")
        self.scroll_to_element(questions[index])
        self.click_element(questions[index])

    @allure.step("Получить текст ответа для вопроса с индексом {index}")
    def get_faq_answer_text(self, index):
        items = self.find_elements(MainPageLocators.FAQ_ITEMS)
        if index >= len(items):
            raise IndexError(f"FAQ с индексом {index} не существует")

        answer = self.find_child_element(
            items[index],
            MainPageLocators.FAQ_ANSWER
        )
        self.wait.until(
            lambda _: answer.is_displayed(),
            message=f"Ответ для вопроса {index} не отобразился"
        )
        return answer.text

    @allure.step("Нажать на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM),
            message=f"Кнопка 'Заказать' (нижняя) не стала кликабельной"
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.wait.until(
            EC.visibility_of(button),
            message=f"Кнопка 'Заказать' (нижняя) не отобразилась после скролла"
        ).click()

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)