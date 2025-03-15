"""Homework 14 - 2.Re:"dd.mm.yyyy"""

import re

FILE_NAME = 'hm_14_re.txt'


def find_data_re(some_file):
    """
    to find data in text
    """
    dates_list: list = []
    with open(some_file, mode='r+', encoding='utf-8', errors='replace') as re_file:
        for some_line in re_file:
            a_date = re.search("([0-9]{2}.[0-9]{2}.[0-9]{4})", some_line)
            if a_date:
                dates_list.append(a_date.group())
    return print(dates_list)


if __name__ == "__main__":
    find_data_re(FILE_NAME)
