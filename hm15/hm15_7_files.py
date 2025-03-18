"""Homework 15 - 15 Iterator and generator *
Напишите программу, которая запрашивает у пользователя целое число N и
создает генераторную функцию для генерации чисел от 1 до N.
Выведите сумму всех чисел, сгенерированных этой функцией.
"""

import logging

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[stream_handler])


def fifteen(users_num):
    """
    task_fifteen
    """
    def gen_function(num):
        result = 0
        while num > 0:
            result += num
            yield result
            num -= 1

    gen = gen_function(users_num)
    sum_result = 0
    for _ in range(users_num):
        sum_result = next(gen)
    return sum_result


data_from_user = int(input('введите число: '))


try:
    logging.info('given data is {data_from_user} - the summ is: %s', fifteen(data_from_user))
except ProcessLookupError:
    logging.error("An ERROR")

if __name__ == "__main__":
    fifteen(data_from_user)
