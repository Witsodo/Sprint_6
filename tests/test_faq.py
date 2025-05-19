import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from data import FAQ_DATA
from urls import BASE_URL

@allure.suite('Тесты FAQ')
class TestFAQ:

    @classmethod
    def setup_class(cls):
        # Инициализация драйвера
        options = Options()
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(BASE_URL)
        # Инициализация Page Object
        cls.main_page = MainPage(cls.driver)

    @pytest.mark.parametrize('faq_item', FAQ_DATA, ids=[f"Question {item['question_index']}" for item in FAQ_DATA])
    @allure.feature('Проверка ответов в FAQ')
    @allure.story('Раскрытие вопросов и проверка ответов')
    @allure.title('Проверка ответа на вопрос #{faq_item[question_index]}')
    def test_faq_question_opens_correct_answer(self, faq_item):
        # Прокрутка до FAQ
        faq_section = self.main_page.get_faq_answers()[0]
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)

        # Клик по вопросу
        self.main_page.click_faq_question(faq_item["question_index"])

        # Проверка ответа
        actual_answer = self.main_page.get_faq_answer_text(faq_item["question_index"])
        assert actual_answer == faq_item["expected_answer"], f"Ожидался ответ: '{faq_item['expected_answer']}', получен: '{actual_answer}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()