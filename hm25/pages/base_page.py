"""Homework 25 - saucedemo.com - BASE"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    base class for all pages
    """
    def __init__(self, driver, url):
        """
        init
        """
        self.driver = driver
        self.url = url

    def open(self):
        """
        open page
        """
        self.driver.get(self.url)

    def click_button(self, locator):
        """
        simple click button
        """
        button = self.driver.find_element(*locator)
        button.click()

    def choose_el(self, locator, timeout=2):
        """
         click button with timeout check
         """
        button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator))
        )
        button.click()
        return button

    def check_el(self, locator):
        """
         return text of el
         """
        el_text = self.driver.find_element(*locator).text
        return el_text

    def send_text(self, locator, text):
        """
         insert data to field
         """
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def is_url_correct(self, url):
        """
         check the url
         """
        return (self.driver.current_url == url,
                f"Expected to get {url} but got {self.driver.current_url}")

    def is_element_present(self, locator):
        """
         check if el exist
         """
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
