"""Homework 24 - saucedemo.com"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def click_button(locator, driver_web, timeout=10):
    """
    click button for common use
    """
    button = WebDriverWait(driver_web, timeout).until(
            EC.element_to_be_clickable((locator))
        )
    button.click()


# driver_web = webdriver.Chrome()
# driver_web.get("https://www.saucedemo.com")


def login_page(user, password, driver):
    """
    1. Экран логина:
    1.1 Ввод имени пользователя:
    1.2 Ввод пароля - password
    1.3 Нажатие кнопки 'Login':  #login-button
    """
    name_input = driver.find_element(By.CSS_SELECTOR, f'[name="{user}"]')
    name_input.clear()
    name_input.send_keys("standard_user")
    name_input = driver.find_element(By.CSS_SELECTOR, f'[name="{password}"]')
    name_input.clear()
    name_input.send_keys("secret_sauce")
    a_button = driver.find_element(By.ID, "login-button")
    click_button(a_button, driver, 5)
    if a_button:
        return True
    return False


# 2. Экран главной страницы:

def main_page_add(driver, el_num):
    """
    2.1 Нажать на кнопку "Add to cart"
    2.1.1 Нажать на кнопку - 1, 2 элемент
    """
    add_cart_button = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
    click_button(add_cart_button[el_num], driver, 5)
    if add_cart_button:
        return True
    return False


def main_page_remove(driver, el_num):
    """
    2.2 Нажать на кнопку "Remove":
    """
    remove_cart_button = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
    click_button(remove_cart_button[el_num], driver, 5)
    if remove_cart_button:
        return True
    return False

def cart_page_delete_el(driver):
    """
    # 3. Экран корзины заказов:
    3.1 Нажатие на ссылку 'Chopping Cart':
    3.2 Удалить 2 элемент из корзины:
    3.3 Нажатие на ссылку 'Continue Shopping':
    """
    chopping_cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    click_button(chopping_cart_button, driver, 5)
    remove_button = driver.find_elements(By.XPATH, "//button[contains(text(), 'Remove')]")
    remove_button[0].click()
    continue_shopping_el = driver.find_element(By.ID, "continue-shopping")
    click_button(continue_shopping_el, driver, 5)
    if remove_button:
        return True
    return False


def menu(driver):
    """
    4. Вызов всплывающего Меню:
    """
    menu_el = driver.find_element(By.ID, "react-burger-menu-btn")
    click_button(menu_el, driver, 5)
    if menu_el:
        return True
    return False

def log_out(driver):
    """
    5. Log out
    """
    log_out_el = driver.find_element(By.ID, "logout_sidebar_link")
    click_button(log_out_el, driver, 5)
    if log_out_el:
        return True
    return False
