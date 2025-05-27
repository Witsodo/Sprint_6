import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import BASE_URL


#Фикстура для инициализации и закрытия браузера
@pytest.fixture(scope="function")
def driver():

    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

#Фикстура для работы с главной страницей
@pytest.fixture
def main_page(driver):

    driver.get(BASE_URL)
    return MainPage(driver)

#Фикстура для работы со страницей заказа
@pytest.fixture
def order_page(driver):

    return OrderPage(driver)
