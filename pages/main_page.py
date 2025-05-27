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

        # Получаем родительский элемент вопроса
        question_item = items[index]

        # Находим ответ внутри вопроса (используя локатор)
        answer = question_item.find_element(*MainPageLocators.FAQ_ANSWER)

        # Проверяем видимость через базовый класс
        if not self.is_element_displayed(answer):
            raise ValueError(f"Ответ для вопроса {index} не отобразился")

        return answer.text

    @allure.step("Нажать на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.close_cookies_if_present()  # Закрываем куки если есть
        self.safe_scroll_and_click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)