"""Homework 15 - 14 Logger
Расширьте программу из задания 1 таким образом, чтобы логи также
выводились на консоль с использованием отдельного обработчика.
"""

import logging
from hm14_1_files import task_one

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[stream_handler])


def four_teen():
    """
    four_teen
    """
    try:
        students_data = task_one
        logging.info(':a function "task_one" is handled successfully: %s', students_data)
    except ProcessLookupError:
        logging.error("An ERROR")


if __name__ == "__main__":
    four_teen()
