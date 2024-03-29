from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #link = "http://suninjuly.github.io/registration1.html"
    new_reg_link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()

    #browser.get(link)
    browser.get(new_reg_link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("dsd")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("qqq")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("qatest@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
