
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    # Шаг 1: Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Добавление товаров в корзину
    main_page = MainPage(driver)
    main_page.add_item_to_cart(0)  # Добавляем "Sauce Labs Backpack"
    main_page.add_item_to_cart(1)  # Добавляем "Sauce Labs Bolt T-Shirt"
    main_page.add_item_to_cart(2)  # Добавляем "Sauce Labs Onesie"

    # Проверка, что товары добавлены в корзину
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    print(f"Items in cart: {cart_count}")  # Печать количества товаров в корзине
    assert cart_count == "3", f"Expected 3 items in cart, but got {cart_count}"

    # Шаг 3: Переход в корзину
    main_page.go_to_cart()

    # Шаг 4: Переход к оформлению заказа
    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    # Шаг 5: Заполнение формы оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("John", "Doe", "12345")

    # Шаг 6: Проверка итоговой стоимости
    total_price = checkout_page.get_total_price()
    print(f"Total Price on checkout page: {total_price}")  # Печать итоговой стоимости
    assert total_price == "Total: $58.29", f"Expected total price to be $58.29, but got {total_price}"

