from selenium.webdriver.common.by import By


class BasePageLocators():
    cookie_button = (By.ID, 'rcc-confirm-button')
    logo_yandex=(By.XPATH, ".//img[@alt='Yandex']")
    logo_samokat=(By.XPATH, ".//img[@alt='Scooter']")
    order_button = (By.XPATH, ".//button[text()='Заказать']")




