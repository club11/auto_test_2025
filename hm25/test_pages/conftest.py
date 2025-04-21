"""Homework 25 - saucedemo.com - Conftest file"""

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """
    run selenium webdriver
    """
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
