"""Homework 25 - saucedemo.com - Tests"""

import pytest
from user_creds import UserCredentials
from env import Env
from hm25.pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.smoke
def test_login_w_right_creds(driver):
    """
   test login page
  """
    lp = LoginPage(driver, Env.URL)
    lp.open()
    lp.complete_login(UserCredentials.standart_user, UserCredentials.standart_password)
    assert lp.is_login_successful()


@pytest.mark.main_page
@pytest.mark.smoke
def test_add_remove_bucket(driver):
    """
   test main page
  """
    lp = LoginPage(driver, Env.URL)
    lp.open()
    main_paige = lp.complete_login(UserCredentials.standart_user, UserCredentials.standart_password)
    main_paige.add_el_to_bucket()
    assert main_paige.el_is_added()
    assert main_paige.check_el_is() == "Remove"
    main_paige.remove_el_from_bucket()
    assert main_paige.check_el_is() == "Add to cart"
    assert main_paige.is_menu_clickable()


@pytest.mark.cart
@pytest.mark.smoke
def test_cart(driver):
    """
   test cart page
  """
    lp = LoginPage(driver, Env.URL)
    lp.open()
    main_paige = lp.complete_login(UserCredentials.standart_user, UserCredentials.standart_password)
    main_paige.add_el_to_bucket()
    cp = main_paige.to_bucket_page()
    cp.remove_el_from_bucket()
    assert cp.el_is_deleted()
    cp.continue_shopping()


@pytest.mark.log_out
@pytest.mark.smoke
def test_log_out(driver):
    """
   test log_out
  """
    lp = LoginPage(driver, Env.URL)
    lp.open()
    main_paige = lp.complete_login(UserCredentials.standart_user, UserCredentials.standart_password)
    assert main_paige.is_menu_clickable()
    main_paige.click_menu()
    main_paige.log_out_menu()
    assert main_paige.is_log_out_successful()
