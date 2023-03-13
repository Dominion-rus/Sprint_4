import pytest
import allure
from pages.order_page import OrderPage
from conftest import ORDERS, LINK_YANDEX, LINK_BASE_PAGE, ORDER_OK_TEXT


@allure.suite('Тестрование создания заказа')
class TestCreateOrder:
    @allure.title('Создать заказ')
    @allure.description('Заполнение всех форм для формирования заказа')
    @pytest.mark.parametrize('order', ORDERS)
    def test_order_from_header_success(self, driver, order):

        page = OrderPage(driver)
        page.accept_cookies()
        page.click_order_button(order['by_button'])
        page.fill_customer_data(
            order['firstname'],
            order['lastname'],
            order['address'],
            order['subway_station'],
            order['phone']
        )
        page.click_button_next()
        page.fill_order_data(
            order['date'],
            order['duration'],
            order['color'],
            order['comment']
        )
        page.click_button_to_submit()
        page.click_button_confirm()
        page.verify_if_order_is_created()
        assert ORDER_OK_TEXT in page.verify_if_order_is_created()
        assert LINK_YANDEX == page.verify_if_link_to_yandex_works()
        assert LINK_BASE_PAGE == page.verify_if_link_to_base_page_works()