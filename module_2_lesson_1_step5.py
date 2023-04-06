from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)


    # Отправляем заполненную форму
    checbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checbox.click()

    radiotn = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radiotn.click()

    time.sleep(1)

    submit = browser.find_element(By.XPATH, "/html/body/div/form/button")
    submit.click()


finally:
    time.sleep(5)
    browser.quit()
