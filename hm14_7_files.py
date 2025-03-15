"""Homework 14 - 7. YAML
 7. YAML
 Создайте YAML файл, содержащий информацию о книгах
 (название, автор, год выпуска).
 Напишите программу, которая считывает данные
 из файла и позволяет пользователю добавлять новые книги в файл.
"""

import yaml

YML_FILE = "yml_data_file.yml"


def task_seven(some_yml):
    """
    task 7 yaml file
    """
    yml_data = {'book_1': ['Great_book', 'Great_author', 1999],
                'book_2': ['Great_book2', 'Great_author2', 2001]}
    with open('yml_data_file.yml', 'w', encoding='utf-8', errors='replace') as yaml_file:
        yaml.dump(yml_data, yaml_file, default_flow_style=False)

    def yml_file_red_write(some_yml_is):
        """
        work with yml file
        """
        to_yaml = {'book_3': ['Great_book3', 'Great_author3', 2025]}
        with open(some_yml_is, 'r+', encoding='utf-8', errors='replace') as stream:
            yaml.safe_load(stream)
            yaml.dump(to_yaml, stream, default_flow_style=False, allow_unicode=True)

    yml_file_red_write(some_yml)


if __name__ == "__main__":
    task_seven(YML_FILE)
