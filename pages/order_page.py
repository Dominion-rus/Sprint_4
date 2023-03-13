import allure
from allure_commons.types import AttachmentType
from locators.order_page import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Нажать кнопку для создания заказа')
    def click_order_button(self, by_button):
        self.click(by_button)

    @allure.step('Заполнить данные пользователя')
    def fill_customer_data(self, firstname, lastname, address, station, phone):
        self.send_data(OrderPageLocators.name, firstname)
        self.send_data(OrderPageLocators.lastname, lastname)
        self.send_data(OrderPageLocators.adress, address)
        self.send_data(OrderPageLocators.station, station)
        self.click(OrderPageLocators.selected_station)
        self.send_data(OrderPageLocators.phone, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        self.click(OrderPageLocators.button_next)

    @allure.step('Заполняем детали заказа')
    def fill_order_data(self, date, duration, color, comment):
        self.send_data(OrderPageLocators.date, date)
        self.click(OrderPageLocators.dropdown_arrow)
        self.click(OrderPageLocators.dropdown_arrow_option[duration])
        self.click(OrderPageLocators.colors[color])
        self.send_data(OrderPageLocators.comment, comment)

    @allure.step('Нажать кнопку для отправки заказа')
    def click_button_to_submit(self):
        self.click(OrderPageLocators.button_order)

    @allure.step('Нажать кнопку для подтверждения заказа')
    def click_button_confirm(self):
        self.click(OrderPageLocators.button_yes)

    @allure.step('Проверяем наличие окна с номером заказа')
    def verify_if_order_is_created(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        return self.find_text(OrderPageLocators.order_number)


