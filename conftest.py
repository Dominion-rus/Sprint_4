import pytest
from selenium import webdriver








@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(LINK_BASE_PAGE)

    yield driver

    driver.quit()