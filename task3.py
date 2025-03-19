""" Task 3"""


def all_numb_sum(n):
    """
    сумму всех чисел до заданного
    """
    if n == 1:
        return 1
    return n + all_numb_sum(n - 1)


result = all_numb_sum(22)
print(result)
