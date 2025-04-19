"""Homework 24 Test case - conf test"""

import pytest
from selenium import webdriver


@pytest.fixture()
def driver_got():
    """
    webdriver fixture
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.close()


@pytest.fixture
def test_data():
    """
    test data
    """
    user_name = "user-name"
    password = "password"
    return user_name, password
