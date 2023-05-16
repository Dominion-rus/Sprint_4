from selenium.webdriver.common.by import By

class BasePageLocators():
    cookie_button = (By.ID, 'rcc-confirm-button')
    logo_yandex=(By.XPATH, ".//img[@alt='Yandex']")
    logo_samokat=(By.XPATH, ".//img[@alt='Scooter']")
    order_button = (By.XPATH, ".//button[text()='Заказать']")
    down_order_button=(By.CLASS_NAME,"Button_Button__ra12g Button_Middle__1CSJM")
    order_button_header = (By.XPATH, "(//button[text()='Заказать'])[1]")
    order_button_middle = (By.XPATH, "(//button[text()='Заказать'])[2]")




