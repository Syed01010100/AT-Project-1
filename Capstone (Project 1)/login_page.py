# login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.selectors = {
            "username": (By.NAME, "username"),
            "password": (By.NAME, "password"),
            "login_button": (By.XPATH, '//button[@type="submit"]'),
            "login_error": (By.XPATH, '//div[@class="oxd-alert oxd-alert--error oxd-alert--dismissible"]')
        }

    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def wait_and_find(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))




    def login(self, username="Admin", password="admin123"):
        self.wait_and_find(*self.selectors["username"]).send_keys(username)
        self.wait_and_find(*self.selectors["password"]).send_keys(password)
        self.wait_and_find(*self.selectors["login_button"]).click()

    def is_login_successful(self):
        """Check if the login was successful by verifying the presence of an error message."""
        try:
            self.wait_and_find(*self.selectors["login_error"])
            return False  # Error message found, login failed
        except:
            return True  # No error message, login successful