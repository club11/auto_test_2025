"""Homework 14 - 6 JSON.
 Создайте JSON файл, содержащий информацию о футбольных клубах
 (название, страна, количество побед).
 Напишите программу, которая считывает данные из файла и выводит
 на экран информацию о клубе с наибольшим количеством побед.
"""

import json

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


if __name__ == "__main__":
    json_football_clubs(JSON_FILE)
