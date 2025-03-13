"""Homework 14"""

import random
import re
import xml.etree.ElementTree as Et
import json
import yaml


# 1.Files
class Student:
    """
    just in case, instead dict use
    """
    def __init__(self, student_name=None, grade=None, group=None):
        self.student_name = student_name
        self.grade = grade
        self.group = group

    @staticmethod
    def print_data():
        """
        # to avoid "Too few public methods" pylint Error
        """
        return print("what i supposed to do here?")

    @staticmethod
    def doings_something():
        """
        # to avoid "Too few public methods" pylint Error
        """
        return print("pylint makes me do that!")

students_list: list = []


def create_student_groups(some_students_list):
    """
    to keep data in objects
    """
    group_num = 0
    for lazy_name in range(10):
        group_num += 1
        a_student = Student(f'student_name_{lazy_name}', random.randrange(2, 10), group=group_num)
        some_students_list.append(a_student)
        if group_num == 4:
            group_num = 0


create_student_groups(students_list)


with open('students.txt', 'w+', encoding='utf-8', errors='replace') as file:
    for student in students_list:
        file.write(f'{student.student_name}, {student.grade}, {student.group}\n')


AMOUNT_COUNT = 0
students_dict: dict = {}
with open('students.txt', 'r+', encoding='utf-8', errors='replace') as file:
    for a_line in file:
        # print(a_line)
        st_name, st_grade, st_group = a_line.replace('\n', '').split(',')
        AMOUNT_COUNT += 1
        if not students_dict.get(st_group):
            STUD_COUNT = 1
            students_dict[st_group] = int(st_grade), STUD_COUNT
        else:
            prev_val, STUD_COUNT = students_dict[st_group]
            students_dict[st_group] = prev_val + int(st_grade), STUD_COUNT + 1
    LAST_LINE = ''
    for keys, values in students_dict.items():
        average_val = values[0] / values[1]
        LAST_LINE += (f' группа {keys}: количество студентов: {values[1]}, '
                      f'средняя оценка: {average_val}')
    file.write(LAST_LINE)


# 2. Re:  "dd.mm.yyyy"
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


FILE_NAME = 'hm_14_re.txt'
find_data_re(FILE_NAME)


# 3. Проверка паролей
def check_parol(some_parol):
    """
    to check_parol
    """
    # result = re.match('/^[0-9a-zA-Z]{4,}$', some_parol) # д.б. поверить
    if len(some_parol) < 4:
        return print('something went wrong!!!!!')
    success_check = True
    validators_lat = ('[0-9]', '[A-Z]', '[a-z]')
    validators_kir = ('[0-9]', '[А-Я]', '[а-я]')
    for valid in validators_lat:
        if not re.search(valid, some_parol):
            success_check = False
            break
    if success_check:
        return print('success!')
    for valid in validators_kir:
        if not re.search(valid, some_parol):
            success_check = False
            break
    if not success_check:
        return print('something went wrong!')
    return print('success!')


# 4. В предложении допущены ошибки. Необходимо исправить каждый такой
# повтор (слово, один или несколько пробельных символов, и снова то же слово).
A_STRING = ("Довольно  распространённая ошибка  ошибка — это лишний повтор повтор слова слова. "
            "Смешно, не не правда ли? Не нужно портить хор хоровод")
pattern = re.compile(r'\s{2}')
sentence = re.sub(pattern, ' ', A_STRING)
PATTERN = r"\s{2+}"
re_result = re.split(PATTERN, sentence)
to_change_is = {'ошибка ошибка': 'ошибка', 'повтор повтор': 'повтор повтор',
                'слова слова': 'слова', 'не не': 'не', 'хор хоровод': 'хоровод'}
final_string_is = sentence


def change_sentence(final_string, to_change):
    """
    to change_sentence, duplicates exclude
    """
    for ex_change, ex in to_change.items():
        new_string = re.sub(ex_change, ex, final_string)
        final_string = new_string
    return print(final_string)


# 5. XML
root = Et.Element("data")
doc = Et.SubElement(root, "product")
Et.SubElement(doc, "description", name="description").text = "cellphone"
Et.SubElement(doc, "price", name="price").text = "100"
Et.SubElement(doc, "currency", name="price").text = "USD"
doc = Et.SubElement(root, "product")
Et.SubElement(doc, "description", name="description").text = "cellphone2"
Et.SubElement(doc, "price", name="price").text = "200"
Et.SubElement(doc, "currency", name="price").text = "USD"
tree = Et.ElementTree(root)
tree.write("not_best_choice.xml")


def parse_xml(xml_str):
    """
    work with xml file
    """
    tree_is = Et.parse(xml_str)
    root_is = tree_is.getroot()
    total_cost = 0
    for child in root_is.findall('product'):
        # product = child.find('description').text
        price = child.find('price').text
        # currency = child.find('currency').text
        total_cost += (int(price))
    return print('total_cost =', total_cost)


# 6. JSON
# Создайте JSON файл, содержащий информацию о футбольных клубах
# (название, страна, количество побед).
# Напишите программу, которая считывает данные из файла и выводит
# на экран информацию о клубе с наибольшим количеством побед.


JSON_FILE = 'champions_league.json'


def json_football_clubs(some_json):
    """
    work with json file
    """
    with open(some_json, encoding='utf-8', errors='replace') as a_file_is:
        json_data = json.load(a_file_is)
        win = 0
        max_wins = 0
        club_win_max = ''
        for club in json_data.items():
            _, wins = club[1].values()
            if wins > win:
                club_win_max = club[0]
                max_wins = wins
                win = wins
    return print(club_win_max, max_wins)


# 7. YAML
# Создайте YAML файл, содержащий информацию о книгах
# (название, автор, год выпуска).
# Напишите программу, которая считывает данные
# из файла и позволяет пользователю добавлять новые книги в файл.

yml_data = {'book_1': ['Great_book', 'Great_author', 1999],
            'book_2': ['Great_book2', 'Great_author2', 2001]}
with open('yml_data_file.yml', 'w', encoding='utf-8', errors='replace') as yaml_file:
    yaml.dump(yml_data, yaml_file, default_flow_style=False)

to_yaml = {'book_3': ['Great_book3', 'Great_author3', 2025]}
YML_FILE = "yml_data_file.yml"


def yml_file_red_write(some_yml):
    """
    work with yml file
    """
    with open(some_yml, 'r+', encoding='utf-8', errors='replace') as stream:
        yaml.safe_load(stream)
        yaml.dump(to_yaml, stream, default_flow_style=False, allow_unicode=True)

yml_file_red_write(YML_FILE)


if __name__ == "__main__":
    find_data_re(FILE_NAME)
    parol_list = ['Dar4', 'Dar', 'order66', 'Chosen1', 'Ce1']
    for a_parol in parol_list:
        check_parol(a_parol)
    change_sentence(final_string_is, to_change_is)
    parse_xml("not_best_choice.xml")
    json_football_clubs(JSON_FILE)
    yml_file_red_write(YML_FILE)
