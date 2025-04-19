"""Homework 24 - saucedemo.com"""

import pytest
from hm_24 import (login_page, main_page_add,
                   main_page_remove, cart_page_delete_el,
                   menu, log_out)


def test_login_page(test_data, driver_got):
    """
    1. Экран логина:
    1.1 Ввод имени пользователя:
    1.2 Ввод пароля - password
    1.3 Нажатие кнопки 'Login':  #login-button
    """
    res = login_page(test_data[0], test_data[1], driver_got)
    assert res, "Error here"


@pytest.mark.parametrize("el_num", [0, 1])
def test_main_page_add(driver_got, test_data, el_num):
    """
    2. Экран главной страницы:
    2.1 Нажать на кнопку "Add to cart"
    2.1.1 Нажать на кнопку - 1, 2 элемент
    """
    login_page(test_data[0], test_data[1], driver_got)
    res = main_page_add(driver_got, el_num)
    assert res, "Error here"


@pytest.mark.parametrize("el_num", [0, 1])
def test_main_page_remove(driver_got, test_data, el_num):
    """
    2.2 Нажать на кнопку "Remove":
    """
    login_page(test_data[0], test_data[1], driver_got)
    main_page_add(driver_got, el_num)
    res = main_page_remove(driver_got, el_num)
    assert res, "Error here"


@pytest.mark.parametrize("el_num", [0, 1])
def test_cart_page_delete_el(driver_got, test_data, el_num):
    """
    # 3. Экран корзины заказов:
    3.1 Нажатие на ссылку 'Chopping Cart':
    3.2 Удалить 2 элемент из корзины:
    3.3 Нажатие на ссылку 'Continue Shopping':
    """
    login_page(test_data[0], test_data[1], driver_got)
    main_page_add(driver_got, el_num)
    res = cart_page_delete_el(driver_got)
    assert res, "Error here"


def test_menu(driver_got, test_data):
    """
    4. Вызов всплывающего Меню:
    """
    login_page(test_data[0], test_data[1], driver_got)
    res = menu(driver_got)
    assert res, "Error here"


def test_log_out(driver_got, test_data):
    """
    5. Log out
    """
    login_page(test_data[0], test_data[1], driver_got)
    menu(driver_got)
    res = log_out(driver_got)
    assert res, "Error here"
