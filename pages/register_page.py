from selenium.webdriver.common.by import By

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    PASSWORD = (By.ID, "password")
    REGISTER_BTN = (By.ID, "register")

    def register(self, username, email, password):

        self.driver.find_element(*self.USERNAME).send_keys(username)

        self.driver.find_element(*self.EMAIL).send_keys(email)

        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.REGISTER_BTN).click()