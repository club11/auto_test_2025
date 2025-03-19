"""
    Напишите программу, которая принимает от
    пользователя строку или число и проверяет,
    является ли она палиндромом (читается одинаково слева направо и справа налево)
"""

# num % 2 == 0

def get_data(some_data):
    """
    check a palindrome
    """
    if len(some_data) % 2 == 0:
        for n in some_data:
            first, second = n, some_data[-some_data.index(n)]
            print(first, second)
            if first != second:
                print('Not a palindrome')
        print('Is a palindrome')


get_data('abcdcba')
