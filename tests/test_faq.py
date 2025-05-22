import pytest
import allure
from data import FAQ_DATA
from pages.main_page import MainPage


@allure.suite('Тесты FAQ')
class TestFAQ:

    @allure.feature('Проверка ответов в FAQ')
    @allure.story('Раскрытие вопросов и проверка ответов')
    @allure.title('Проверка ответа на вопрос #{faq_item["question_index"]}')
    @pytest.mark.parametrize('question_data', FAQ_DATA, ids=lambda x: f"Question {x['question_index']}")
    def test_faq_question_opens_correct_answer(self, main_page, question_data):
        index = question_data["question_index"]
        expected = question_data["expected_answer"]

        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)
        assert actual_answer == expected