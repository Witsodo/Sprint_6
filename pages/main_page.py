from selenium.webdriver import ActionChains
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class MainPage(BasePage):
    # Получение списка вопросов FAQ
    def get_faq_questions(self):

        return self.driver.find_elements(*MainPageLocators.FAQ_HEADERS)

    # Получение списка блоков с ответами FAQ
    def get_faq_answers(self):

        return self.driver.find_elements(*MainPageLocators.FAQ_ITEMS)

    # Нажатие на вопрос FAQ по индексу
    def click_faq_question(self, index):

        questions = self.get_faq_questions()
        questions[index].click()

    # Получение текста ответа FAQ по индексу
    def get_faq_answer_text(self, index):

        answers = self.get_faq_answers()
        return answers[index].find_element(*MainPageLocators.FAQ_ANSWER).text

    # Клик по верхней кнопке 'Заказать'
    def click_order_button_top(self):

        self.find_element(MainPageLocators.ORDER_BUTTON_TOP).click()

    # Клик по нижней кнопке 'Заказать'
    def click_order_button_bottom(self):

        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.3)
        button.click()

    # Клик по логотипу Самоката
    def click_scooter_logo(self):

        self.find_element(MainPageLocators.SCOOTER_LOGO).click()

    # Клик по логотипу Яндекса
    def click_yandex_logo(self):

        self.find_element(MainPageLocators.YANDEX_LOGO).click()