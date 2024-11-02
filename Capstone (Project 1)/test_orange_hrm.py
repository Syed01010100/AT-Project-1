#test_orange_hrm.py

import pytest
from selenium import webdriver
from login_page import LoginPage
from pim_page import PIMPage


@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestOrangeHrm:

    def test_invalid_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.browse()  # Navigate to the login page

        # Use invalid credentials
        invalid_username = "InvalidUser"
        invalid_password = "InvalidPass"

        # Add a debug statement to show what's happening
        print("Attempting to login with invalid credentials...")
        self.login_page.login(invalid_username, invalid_password)
        print("invalid")

    def test_valid_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.browse()

        valid_username = "Admin"
        valid_password = "admin123"
        self.login_page.login(valid_username, valid_password)

        assert self.login_page.is_login_successful(), "Login failed with valid credentials."
        print("Login was successful.")
    def test_add_employee(self):
        # This test can be included if successful logins are handled elsewhere
        self.pim_page = PIMPage(self.driver)

        # Add employee if logged in
        self.pim_page.add_employee("SyedAli", "Aseeka", "145326")
        print("successful employee addition.")

    def test_edit_employee(self):
        self.pim_page = PIMPage(self.driver)

        # Provide values for all required parameters

        self.pim_page.edit_employee(first_name="Faruk", middle_name="raja")
        print("successful employee updated")

    def test_delete_employee(self):
        # This test can also be included if necessary
        self.pim_page = PIMPage(self.driver)

        # Deletion should only proceed if a valid context is established
        self.pim_page.delete_employee("Faruk")
        print("successful employee deletion.")