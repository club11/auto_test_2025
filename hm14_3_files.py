"""Homework 14 - 3.Проверка паролей"""

import re


# 3. Проверка паролей
def check_parol(some_parol):
    """
    to check_parol
    """
    # result = re.match('/^[0-9a-zA-Z]{4,}$', some_parol) # д.б. поверить
    if len(some_parol) < 4:
        return print('something went wrong!!!!!')
    success_check = True
    validators_lat = ('[0-9]', '[A-Z]', '[a-z]')
    validators_kir = ('[0-9]', '[А-Я]', '[а-я]')
    for valid in validators_lat:
        if not re.search(valid, some_parol):
            success_check = False
            break
    if success_check:
        return print('success!')
    for valid in validators_kir:
        if not re.search(valid, some_parol):
            success_check = False
            break
    if not success_check:
        return print('something went wrong!')
    return print('success!')


if __name__ == "__main__":
    check_parol('Chosen1')
