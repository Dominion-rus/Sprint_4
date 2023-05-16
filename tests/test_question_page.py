import pytest
import allure
from pages.question_page import QuestionsPage
from conftest import QUESTIONS_AND_ANSWERS


@allure.suite('Тестирование формы Вопрос-Ответ')
class TestQuestionPage:
    @allure.title('Проверка наличия текста Вопросы о Важном')
    def test_find_and_check_question_about_text(self,driver):
        page=QuestionsPage(driver)
        page.accept_cookies()
        page.find_and_check_question_about_text()

    @allure.title('Открыть вопрос и проверить текст ответа')
    @pytest.mark.parametrize('question, answer', QUESTIONS_AND_ANSWERS)
    def test_answer_matches_question_true(self, driver, question, answer):
        page = QuestionsPage(driver)
        page.accept_cookies()
        page.find_question(question)
        page.find_answer(answer)