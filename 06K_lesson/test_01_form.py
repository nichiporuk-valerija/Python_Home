from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")  # Оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")


    # Нажать кнопку
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

     # Проверка красного поля
    alert_danger_color = "rgba(248, 215, 218, 1)"
    sleep(1)
    css_value = driver.find_element(By.ID, "zip-code").value_of_css_property(
              "background-color")
    assert alert_danger_color == css_value



    # Проверка остальных полец
    fields = [
            "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
        ]
    for field_name in fields:
            field = driver.find_element(By.ID, field_name)
            field_border_color = field.value_of_css_property("background-color")
            assert field_border_color == "rgba(209, 231, 221, 1)", f"Expected green border color for {field_name}, but got {field_border_color}"