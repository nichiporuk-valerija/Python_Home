import unittest
from selenium import webdriver
from Pages.calculator_page import CalculatorPage  # импортируем Page Object


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Настройка драйвера"""
        self.driver = webdriver.Chrome()  # Можно использовать любой драйвер, который у вас установлен
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.page = CalculatorPage(self.driver)  # Создаем объект страницы

    def tearDown(self):
        """Закрытие драйвера после теста"""
        self.driver.quit()

    def test_calculate(self):
        """Тест для проверки калькулятора"""
        self.page.perform_calculation(45, self.page.button_7_locator, self.page.button_plus_locator,
                                      self.page.button_8_locator)

        # Получаем результат после выполнения операции
        result = self.page.get_result()

        # Проверяем, что результат равен 15 (после 45 секунд)
        self.assertEqual(result, "15")


if __name__ == "__main__":
    unittest.main()
