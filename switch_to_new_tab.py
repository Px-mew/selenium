"""
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x = browser.find_element(By.ID, "input_value")
    x = x.text

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
