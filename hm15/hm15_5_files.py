"""Homework 15 - 13 Logger
 Настройте ротацию файлов логов, чтобы каждый день создавался новый файл
 с датой в имени файла. Ограничьте количество хранимых файлов логов до 7,
 чтобы старые файлы автоматически удалялись.
"""

import os
import logging
import datetime
from dateutil.relativedelta import relativedelta


def task_thirteen():
    """
    task_thirteen
    """
    today_date = datetime.datetime.now().date()
    date_to_delete = today_date - relativedelta(days=7)
    date_to_delete_str = date_to_delete.strftime('%Y-%m-%d')
    today_date = today_date.strftime('%Y-%m-%d')
    try:
        os.remove(f'{date_to_delete_str}.log')
    except FileNotFoundError:
        print(f'No file {date_to_delete_str}.log')
    logging.basicConfig(level=logging.INFO, filename=f"{today_date}.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")


if __name__ == "__main__":
    task_thirteen()
