"""Homework 14 - 1.Files"""

import random


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


def task_one():
    """
    task_one
    """
    create_student_groups(students_list)


    with open('students.txt', 'w+', encoding='utf-8', errors='replace') as file:
        for student in students_list:
            file.write(f'{student.student_name}, {student.grade}, {student.group}\n')
    amount_count = 0
    students_dict: dict = {}
    last_line = ''
    with open('students.txt', 'r+', encoding='utf-8', errors='replace') as file:
        for a_line in file:
            _, st_grade, st_group = a_line.replace('\n', '').split(',')
            amount_count += 1
            if not students_dict.get(st_group):
                stud_count = 1
                students_dict[st_group] = int(st_grade), stud_count
            else:
                prev_val, stud_count = students_dict[st_group]
                students_dict[st_group] = prev_val + int(st_grade), stud_count + 1

        for keys, values in students_dict.items():
            average_val = values[0] / values[1]
            last_line += (f' группа {keys}: количество студентов: {values[1]}, '
                          f'средняя оценка: {average_val}')
        file.write(last_line)
    return print(last_line)


if __name__ == "__main__":
    task_one()
