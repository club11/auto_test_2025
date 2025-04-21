"""Homework 25 - saucedemo.com - Log in page"""

from base_page import BasePage
from product_list_page import ProductListPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """
     Login page class
    """
    user_name = (By.ID, "user-name")
    user_password = (By.ID, "password")
    login_button = (By.CLASS_NAME, "btn_action")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    # def __init__(self, driver, url):
    #     """
    #      init
    #     """
    #     super().__init__(driver, url)

    def complete_login(self, user_name, password):
        """
         to login on start page
        """
        self.send_text(self.user_name, user_name)
        self.send_text(self.user_password, password)
        self.click_button(self.login_button)
        return ProductListPage(self.driver, self.url)

    def is_login_successful(self):
        """
         check if log in is successful
        """
        return not self.is_element_present(self.error_message)
