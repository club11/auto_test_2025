""" Task 2"""


def square_func():
    """
     запрашивает у пользователя число и выводит его квадр
    :return:
    """
    get_data = input('enter some value:')
    return int(get_data)  ** 2

def even_func():
    """
    определяет, является ли оно четным или нечетным
    """
    get_even_data = input('enter some value:')
    if int(get_even_data) % 2 == 0:
        return print('EVEN')
    return print('NOT EVEN')
