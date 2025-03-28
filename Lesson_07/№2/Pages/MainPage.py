from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = [
            (By.ID, "add-to-cart-sauce-labs-backpack"),
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            (By.ID, "add-to-cart-sauce-labs-onesie")
        ]
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, index):
        self.driver.find_element(*self.add_to_cart_buttons[index]).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
