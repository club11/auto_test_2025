"""Homework 14"""

from hm14_1_files import task_one
from hm14_2_files import find_data_re, FILE_NAME
from hm14_3_files import check_parol
from hm14_4_files import task_four, A_STRING
from hm14_5_files import task_five
from hm14_6_files import json_football_clubs, JSON_FILE
from hm14_7_files import task_seven, YML_FILE

if __name__ == "__main__":
    task_one()
    find_data_re(FILE_NAME)
    parol_list = ['Dar4', 'Dar', 'order66', 'Chosen1', 'Ce1']
    for a_parol in parol_list:
        check_parol(a_parol)
    task_four(A_STRING)
    task_five()
    json_football_clubs(JSON_FILE)
    task_seven(YML_FILE)
