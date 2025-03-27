from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_shop():
    # Данные для авторизации
    URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    # Данные для оформления заказа
    FIRST_NAME = "Test"
    LAST_NAME = "User"
    POSTAL_CODE = "12345"
    EXPECTED_TOTAL = "$58.29"

    # Инициализация WebDriver
    browser = webdriver.Chrome()
    browser.get(URL)
    time.sleep(2)

    # Авторизация
    browser.find_element(By.ID, "user-name").send_keys(USERNAME)
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Добавление товаров в корзину
    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item in items:
        browser.find_element(By.ID, item).click()
    time.sleep(2)

    # Переход в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Оформление заказа
    browser.find_element(By.ID, "checkout").click()
    time.sleep(2)

    # Заполнение формы
    browser.find_element(By.ID, "first-name").send_keys(FIRST_NAME)
    browser.find_element(By.ID, "last-name").send_keys(LAST_NAME)
    browser.find_element(By.ID, "postal-code").send_keys(POSTAL_CODE)
    browser.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Получение итоговой суммы
    total_price = browser.find_element(By.CLASS_NAME, "summary_total_label").text.split()[-1]

    # Закрытие браузера
    browser.quit()

    # Проверка итоговой суммы
    assert total_price == EXPECTED_TOTAL, f"Ожидалось {EXPECTED_TOTAL}, но получено {total_price}"