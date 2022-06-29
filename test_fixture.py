"""
открыть страницу 
ввести правильный ответ 
нажать кнопку "Отправить" 
дождаться фидбека о том, что ответ правильный 
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
"""

import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
    ]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', links)
def test_guest_should_see_login_link(browser, links):
    browser.get(links)
    textarea = browser.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    label = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    print(label.text)
    assert label.text == 'Correct!', "Послание инопланетян"
    
