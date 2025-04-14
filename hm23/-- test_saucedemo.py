"""Homework 23 - saucedemo.com"""

# https://www.saucedemo.com
# 1. Экран логина:

# 1.1 Ввод имени пользователя: #user-name
# 1.2 Ввод пароля - password
# 1.3 Нажатие кнопки 'Login':  #login-button

# 2. Экран главной страницы:

# 2.1 Нажать на кнопку "Add to cart":
# 2.1.1 Нажать на кнопку - 1 элемент:
# .inventory_list  > .inventory_item:nth-child(1)  > .inventory_item_description > .pricebar > [class="inventory_item_price"]
# 2.1.1 Нажать на кнопку - 2 элемент:
# .inventory_list  > .inventory_item:nth-child(2)  > .inventory_item_description > .pricebar > [class="inventory_item_price"]
# ...
# через xpath:
# 2.1.1 Нажать на кнопку - 1 элемент. Но через id...:
# //button[@id='add-to-cart-sauce-labs-backpack']
# 2.1.1 Нажать на кнопку - 2 элемент:
# //button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]
# ...

# 2.2 Нажатие на ссылку 'Chopping Cart':  .shopping_cart_link

# 3. Экран корзины заказов:

# 3.1 Удалить 1 элемент из корзины:
# .cart_list > :nth-child(3) > .cart_item_label > .item_pricebar > button
# 3.1 Удалить 2 элемент из корзины:
# .cart_list > :nth-child(4) > .cart_item_label > .item_pricebar > button
# ...

# 3.2 Нажатие на ссылку 'Continue Shopping':   #continue-shopping


# 4. Вызов всплывающего Меню:       #react-burger-menu-btn

# 5. Log out             #logout_sidebar_link
