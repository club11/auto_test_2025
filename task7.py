"""task 7"""


def a_func(sign, numb):
    """
    count_file
    """
    some_string = sign[: numb]
    return print(some_string + some_string[-2::-1])


a_func('abcdef', 3)
