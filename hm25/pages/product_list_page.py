"""Homework 25 - saucedemo.com - Main (ProductList) page"""

from base_page import BasePage
from selenium.webdriver.common.by import By
from hm25.pages.cart_page import CartPage


class ProductListPage(BasePage):
    """
   Main page class
  """
    el_num = 1
    add_button = (By.CSS_SELECTOR, f".btn_inventory:nth-of-type({el_num})")
    remove_button = (By.XPATH, f"(//button[contains(@class, 'btn_inventory')])[{el_num}]")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")
    bucket_page = (By.CLASS_NAME, "shopping_cart_link")
    menu = (By.ID, "react-burger-menu-btn")
    log_out = (By.ID, "logout_sidebar_link")
    login_button = (By.CLASS_NAME, "btn_action")

    # def __init__(self, driver, url):
    #     """
    #  init
    # """
    #     super().__init__(driver, url)

    def add_el_to_bucket(self):
        """
     add to bucket
    """
        self.choose_el(self.add_button)

    def el_is_added(self):
        """
     check el is added to bucket
    """
        return not self.is_element_present(self.error_message)

    def check_el_is(self):
        """
     check el exist
    """
        return self.check_el(self.add_button)

    def remove_el_from_bucket(self):
        """
     remove el from bucket
    """
        self.choose_el(self.remove_button)

    def to_bucket_page(self):
        """
     click bucket icon
    """
        self.choose_el(self.bucket_page)
        return CartPage(self.driver, self.url)

    def click_menu(self):
        """
     choose el menu
    """
        self.choose_el(self.menu)

    def is_menu_clickable(self):
        """
     check out menu
    """
        return self.is_element_present(self.menu)

    def log_out_menu(self):
        """
     choose el log out menu
    """
        self.choose_el(self.log_out)

    def is_log_out_successful(self):
        """
     check is log out successful
    """
        return not self.is_element_present(self.login_button)
