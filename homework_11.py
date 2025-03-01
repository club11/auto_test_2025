"""Homework 11"""

import random


# 1. Положительные аргументы функции
def validate_arguments(some_function):
    """
    1. simple check if number is positive
    """
    def wrapper(*args):
        for number in args:
            if number < 0:
                raise ValueError("Недопустимое значение.")
        some_function(*args)
    return wrapper


@validate_arguments
def get_values_from_user(*args):
    """
    1. just print given numbers
    """
    return print(args, 'first answer')


# 1. Положительные аргументы функции - расширенный вариант
class MyException(Exception):
    """
    1. custom Exception
    """
    def __init__(self, value):
        message = f"{value} не является положительным числом."
        super().__init__(message)


def validate_arguments_2(some_function):
    """
    1. simple check if number is positive var. 2
    """
    def wrapper():
        got_arguments = some_function()
        for number in got_arguments:
            if number < 0:
                raise MyException(number)
    return wrapper

@validate_arguments_2
def get_values_from_user_2():
    """
    1. second var of function including some input checks
    """
    while True:
        given_data = input('please, enter positive numbers, would you kindly!: ')
        temp_str = given_data.replace(',', '').replace(' ', '').replace('-', '')
        if temp_str.isdigit():
            break
    split_val = given_data.split(',')
    int_in_tuple = tuple(map(int, split_val))
    def function_with_arguments_given(*args):
        print(args, ' - arguments were given')
        return args
    return function_with_arguments_given(*int_in_tuple)


# 2. Вернуть число
def is_digit_decorator(some_function):
    """
    1. verify and return answer
    """
    def wrapper():
        got_data = some_function()
        if not isinstance(got_data, int):
            return print(f"{got_data} - введенные данные не являются числом")
        return print(f"{got_data} -введенные данные являются числом")
    return wrapper


@is_digit_decorator
def function_that_gives_something():
    """
    2. simple list of values for random
    """
    choices_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                    'a', 'b', 'c', 'Z', 'W', 'Y', 'V']
    random_data = random.choices(choices_list, k=1)
    return random_data[0]


# 3. Декоратор типов
def type_is(val_type):
    """
    3. check type and summarize
    """
    def type_decorator(func):
        def wrapper(*args):
            temp_value = val_type()
            for n in args:
                temp_value += val_type(n)
            func(temp_value)
        return wrapper
    return type_decorator


@type_is(val_type=int)
def add_useless_func_with_arguments(*arg_a):
    """
    3. show result
    """
    return print('result_is:', *arg_a)


# 4. Функция кэширования * -звездочка распаковки - это очень важно
def cache(func):
    """
    4. here I really stuck and broke my head for couple hours
    adds data to dict if not exist already = func(*args)!
    """
    cache_dict = {}
    def wrapper(*args):
        key_dict = args
        #print('*args ===', *args)
        if key_dict not in cache_dict:
            cache_dict[key_dict] = func(*args)
        return cache_dict[key_dict]
    return wrapper

@cache
def fibonacci(n):
    """
    # 4. поможет лечение – золотое сечение
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def call_funct_create_dict(some_func):
    """
    4. automatic doublecheck of functionality
    """
    argument = int(input('Введите аргумент:'))
    print(some_func(argument))
    print('============')
    print(some_func(argument))


if __name__ == "__main__":
    #get_values_from_user(1, -5, 6)
    #get_values_from_user_2()
    #function_that_gives_something()
    add_useless_func_with_arguments(2, 5, 18)
    #call_funct_create_dict(fibonacci)
