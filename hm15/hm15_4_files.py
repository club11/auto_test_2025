"""Homework 15 - 12 Logger
 Напишите программу, которая будет логировать информацию о действиях пользователя.
 Логи должны записываться в файл "user_actions.log" и содержать время события, уровень логирования
 и сообщение с описанием действия пользователя. Используйте соответствующий уровень логирования
 в зависимости от типа действия (например, INFO для успешных действий и ERROR для ошибок).
"""

import logging

# filemode="a"
logging.basicConfig(level=logging.INFO, filename="../user_actions.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")


def task_twelve():
    """
    task_twelve
    """
    try:
        input_data = input('ведите данные:')
        logging.info('data given by user:%s', input_data)
    except ValueError:
        logging.error("An ERROR")


if __name__ == "__main__":
    task_twelve()
