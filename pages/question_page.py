import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.question_page import QuestionPageLocators
from pages.base_page import BasePage
from conftest import WAIT_TIME, QUASTION_ABOUT_TEXT


class QuestionsPage(BasePage):
    @allure.step('Проверка текста Вопросы о важном')
    def find_and_check_question_about_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*QuestionPageLocators.question_about_text))
        assert self.driver.find_element(*QuestionPageLocators.question_about_text).text == QUASTION_ABOUT_TEXT
    @allure.step('Найти вопрос и нажать на него по порядку')
    def find_question(self, question_locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question_locator))
        WebDriverWait(self.driver, WAIT_TIME).until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()

    @allure.step('Найти ответ и проверить текст')
    def find_answer(self, answer_locator):
        WebDriverWait(self.driver, WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(QuestionPageLocators.open_text_answer))
        assert self.driver.find_element(*QuestionPageLocators.open_text_answer).text == answer_locator[1].split('\'')[1]