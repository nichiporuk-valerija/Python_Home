import pytest
from selenium import webdriver
from Pages.calculator_page import CalculatorPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  # Открываем страницу калькулятора
    yield driver
    driver.quit()

def test_calculate(driver):

   #Тест для проверки калькулятора
    page = CalculatorPage(driver)

   # Выполнение вычислений
    page.perform_calculation(45, page.button_7_locator, page.button_plus_locator, page.button_8_locator)

    # Получаем результат после выполнения операции
    result = page.get_result()

    # Проверяем, что результат равен 15
    assert result == "15", f"Expected result to be 15, but got {result}"
