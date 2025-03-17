"""Homework 14 - 3.Проверка паролей"""

import re


# 3. Проверка паролей
class Parol:
    """
    some refactoring - for Factory Method
    """
    def __init__(self, some_parol):
        self.some_parol = some_parol

    def print_self(self):
        """
        to print
        """
        print(self.some_parol)

    @staticmethod
    def useless_func():
        """
        to make smth in the future
        """
        print('to make smth in the future')


def parol_function():
    """
    check parol by its length and given letters
    """
    parol_data = input('введите пароль:')
    if len(parol_data) < 4:
        print('something went wrong!!!!!')
        return False
    parol_is = Parol(parol_data)
    return parol_is


def check_is_latin_language(a_text):
    """
    check text on latin_language
    """
    try:
        a_text.encode(encoding='utf-8').decode('ascii')
        return 'is_latin'
    except UnicodeDecodeError:
        return 'not_latin'


def language_serialize(a_language):
    """
    takes correct validator depending on language
    """
    validators_lat = ('[0-9]', '[A-Z]', '[a-z]')
    validators_kir = ('[0-9]', '[А-Я]', '[а-я]')
    if a_language == 'is_latin':
        return validators_lat
    # if a_language == 'not_latin':
    return validators_kir


def validate(a_parol, validator):
    """
    starts checks depending on language
    """
    for valid in validator:
        if re.search(valid, a_parol):
            return print('success!')
        return print('something went wrong!')


def check_parol():
    """
    gives a result
    """
    got_parol = parol_function()
    if got_parol:
        got_language = check_is_latin_language(got_parol.some_parol)
        got_validator = language_serialize(got_language)
        validate(got_parol.some_parol, got_validator)


if __name__ == "__main__":
    check_parol()
