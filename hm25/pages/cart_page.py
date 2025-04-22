"""Homework 25 - saucedemo.com - Cart page"""

from base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    """
   Cart page class
  """
    el_num = 1
    remove_button = (By.XPATH, f"(//button[text()='Remove'])[{el_num}]")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")
    continue_shopping_el = (By.ID, "continue-shopping")

    def remove_el_from_bucket(self):
        """
     remove el from the bucket
    """
        self.click_el(self.remove_button)

    def el_is_deleted(self):
        """
     check el is removed from the bucket
    """
        return not self.is_element_present(self.remove_button)

    def continue_shopping(self):
        """
     push button continue shopping
    """
        self.click_el(self.continue_shopping_el)
