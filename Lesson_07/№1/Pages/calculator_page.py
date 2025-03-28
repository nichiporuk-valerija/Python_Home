from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    delay_input_locator = (By.ID, "delay")
    button_7_locator = (By.XPATH, "//span[text()='7']")
    button_8_locator = (By.XPATH, "//span[text()='8']")
    button_plus_locator = (By.XPATH, "//span[text()='+']")
    button_equals_locator = (By.XPATH, "//span[text()='=']")
    result_output_locator = (By.CLASS_NAME, "screen")

    def set_delay(self, delay):
        """Метод для установки значения задержки"""
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_locator):
        """Метод для клика по кнопке калькулятора"""
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self):
        """Метод для получения результата из поля вывода"""
        result = self.driver.find_element(*self.result_output_locator)
        return result.text

    def perform_calculation(self, delay, num1, operator, num2):
        """Метод для выполнения вычислений на калькуляторе"""
        self.set_delay(delay)
        time.sleep(1)  # Ждем немного, чтобы задать задержку
        self.click_button(num1)
        self.click_button(operator)
        self.click_button(num2)
        self.click_button(self.button_equals_locator)
        time.sleep(delay)  # Ожидаем нужную задержку
