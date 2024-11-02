# pim_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.selectors = {
            "pim_menu": (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"),
            "add_emp": (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'),
            "first_name": (By.NAME, "firstName"),
            "last_name": (By.NAME, "lastName"),
            "middle_name": (By.NAME,"middleName"),
            "emp_id": (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"),
            "emp_list": (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a"),
            "delete_button": (By.XPATH, '//button[@class="oxd-icon-button oxd-table-cell-action-space"]//i[@class="oxd-icon bi-trash"]'),
            "emp_name_search": (By.XPATH, '//input[@placeholder="Type for hints..."]'),
            "confirm_delete": (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'),
            "edit_button": (By.XPATH, '//i[@class="oxd-icon bi-pencil-fill"]'),
            "edit_save":(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'),
        }

    def wait_and_find(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def add_employee(self, first_name, last_name, emp_id):
        self.wait_and_find(*self.selectors["pim_menu"]).click()
        self.wait_and_find(*self.selectors["add_emp"]).click()
        self.wait_and_find(*self.selectors["first_name"]).send_keys(first_name)
        self.wait_and_find(*self.selectors["last_name"]).send_keys(last_name)
        self.wait_and_find(*self.selectors["emp_id"]).send_keys(emp_id)
        self.wait_and_find(By.XPATH, '//button[@type="submit"]').click()

    def edit_employee(self,first_name, middle_name):
        self.wait_and_find(*self.selectors["emp_list"]).click()
        self.wait_and_find(*self.selectors["emp_name_search"]).send_keys(first_name)
        self.wait_and_find(*self.selectors["edit_button"]).click()
        self.wait_and_find(*self.selectors["first_name"]).send_keys(first_name)
        self.wait_and_find(*self.selectors["middle_name"]).send_keys(middle_name)
        self.wait_and_find(By.XPATH, '//button[@type="submit"]').click()




    def delete_employee(self, emp_name):
        self.wait_and_find(*self.selectors["emp_list"]).click()
        self.wait_and_find(*self.selectors["emp_name_search"]).send_keys(emp_name)
        self.wait_and_find(*self.selectors["delete_button"]).click()
        self.wait_and_find(*self.selectors["confirm_delete"]).click()