from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    # Явное ожидание: ожидание, пока поле для ввода логина будет доступно
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    # Авторизация
    browser.find_element(By.ID, "user-name").send_keys(USERNAME)
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "login-button").click()

    # Явное ожидание: ожидание, пока элемент для добавления в корзину будет видимым
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
    )

    # Добавление товаров в корзину
    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item in items:
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, item))
        ).click()

    # Явное ожидание: ожидание, пока ссылка на корзину станет доступной
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    # Явное ожидание: ожидание, пока кнопка для оформления заказа станет доступной
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Заполнение формы
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys(FIRST_NAME)

    browser.find_element(By.ID, "last-name").send_keys(LAST_NAME)
    browser.find_element(By.ID, "postal-code").send_keys(POSTAL_CODE)
    browser.find_element(By.ID, "continue").click()

    # Явное ожидание: ожидание, пока итоговая сумма станет доступной
    total_price = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text.split()[-1]

    # Закрытие браузера
    browser.quit()

    # Проверка итоговой суммы
    assert total_price == EXPECTED_TOTAL, f"Ожидалось {EXPECTED_TOTAL}, но получено {total_price}"

