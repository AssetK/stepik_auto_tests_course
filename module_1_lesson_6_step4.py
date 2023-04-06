import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    #time.sleep(10)
    browser.get(link)

    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Python")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("3")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("L.A")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("USA")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

