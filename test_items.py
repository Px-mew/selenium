"""
Запуск автотестов для разных языков интерфейса.
Проверка есть ли на странице кнопка 'Добавить в корзину'
"""
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_available_basket(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button is not None
