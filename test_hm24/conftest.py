"""Homework 24 Test case - conf test"""

import pytest
from selenium import webdriver
from test_data import user_data_dict


@pytest.fixture
def web_driver():
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
    user_name = user_data_dict['user_name']
    password = user_data_dict['password']
    return user_name, password
