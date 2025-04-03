from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_calc():
    # Настройка WebDriver
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    time.sleep(2)  # Ожидание загрузки страницы

    # Вводим значение 45 в поле задержки
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ждем выполнения операции (указанная задержка 45 сек)
    time.sleep(46)

    # Проверяем результат
    result = driver.find_element(By.CLASS_NAME, "screen").text.strip()
    assert result == "15", f"Ожидалось 15, но получено {result}"

    driver.quit()
