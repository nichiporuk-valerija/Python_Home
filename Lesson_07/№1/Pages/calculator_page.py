from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input_locator = (By.ID, "delay")
        self.button_7_locator = (By.XPATH, "//span[text()='7']")
        self.button_8_locator = (By.XPATH, "//span[text()='8']")
        self.button_plus_locator = (By.XPATH, "//span[text()='+']")
        self.button_equals_locator = (By.XPATH, "//span[text()='=']")
        self.result_output_locator = (By.CLASS_NAME, "screen")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_locator):
        button = self.driver.find_element(*button_locator)
        button.click()

    def perform_calculation(self, delay, num1, operator, num2):
        self.set_delay(delay)
        self.click_button(num1)
        self.click_button(operator)
        self.click_button(num2)
        self.click_button(self.button_equals_locator)

        # Ожидаем, пока результат будет доступен
        WebDriverWait(self.driver, delay + 5).until(
            EC.visibility_of_element_located(self.result_output_locator)
        )

    def get_result(self):
        # Ожидает изменения результата и возвращает его
        WebDriverWait(self.driver, 50).until(
            lambda driver: driver.find_element(*self.result_output_locator).text not in ["7+8", ""]
        )
        return self.driver.find_element(*self.result_output_locator).text.strip()
