import pytest
from selenium import webdriver
from locators.question_page import QuestionPageLocators
from locators.base_page import BasePageLocators
from datetime import datetime, timedelta
LINK_BASE_PAGE = 'https://qa-scooter.praktikum-services.ru/'
LINK_YANDEX = 'https://dzen.ru/?yredirect=true'
WAIT_TIME = 15
QUASTION_ABOUT_TEXT='Вопросы о важном'
QUESTIONS_AND_ANSWERS = [[QuestionPageLocators.question_1, QuestionPageLocators.answer_1],
                         [QuestionPageLocators.question_2, QuestionPageLocators.answer_2],
                         [QuestionPageLocators.question_3, QuestionPageLocators.answer_3],
                         [QuestionPageLocators.question_4, QuestionPageLocators.answer_4],
                         [QuestionPageLocators.question_5, QuestionPageLocators.answer_5],
                         [QuestionPageLocators.question_6, QuestionPageLocators.answer_6],
                         [QuestionPageLocators.question_7, QuestionPageLocators.answer_7],
                         [QuestionPageLocators.question_8, QuestionPageLocators.answer_8]]


ORDER_OK_TEXT = "Заказ оформлен"

ORDERS= [{"by_button": BasePageLocators.order_button_middle,
           "firstname": 'Иван',
           "lastname": 'Иванов',
           "address": 'Москва, ул.Мира, 1 кв.5',
           "phone": '+79260000011',
           "subway_station": 'Лубянка ',
           "date": (datetime.now() + timedelta(days=7)).strftime("%d.%m.%Y"),
           "duration": 5,
           "color": 'black',
           "comment": 'Домофон не работает'
           },
          {"by_button": BasePageLocators.order_button_header,
           "firstname": 'Наталья',
           "lastname": 'Петровна',
           "address": 'Москва, пер. Колотушкина, 10Б - 201',
           "phone": '+79260000022',
           "subway_station": 'Спортивная ',
           "date": (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y"),
           "duration": 2,
           "color": 'grey',
           "comment": 'ПоЗвонить за час!!! '
           }
          ]


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(LINK_BASE_PAGE)

    yield driver

    driver.quit()
