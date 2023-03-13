SPRINT 4

_Необходимо наличие FirefoxWebDriver соответствующий версии установленного браузера_
### Инструкция по установке WebDriver ###
>https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
### Скачать WebDriver ###
>https://github.com/mozilla/geckodriver
### Установка зависимостей ###
>pip install -r requirements.txt

### Запуск из корня проекта с генерацией отчета ###
>pytest -v ./tests/ --alluredir=allure_results
### Открытие отчета ###
> allure serve allure_results

### Тестируемое приложение(сайт) ###
> https://qa-scooter.praktikum-services.ru/
### Содержимое директории tests ###
- test_question_page.py - тесты на форму "Вопросы о важном"
