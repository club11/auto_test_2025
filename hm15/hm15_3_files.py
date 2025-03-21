"""Homework 15 - 11. Datetime

 Создайте программу, которая будет принимать ввод от пользователя в формате "ГГГГ-ММ-ДД"
 и проверять, является ли введенная дата будущей или прошлой относительно текущей даты.
 Выведите соответствующее сообщение на экран.
"""

import datetime


def task_eleven(given_date_str):
    """
    define is date in the future or in the past
    """
    while True:
        today_date = datetime.datetime.now().date()
        given_date_object = datetime.datetime.strptime(given_date_str, '%Y-%m-%d').date()
        if given_date_object > today_date:
            print(f'сегодня {today_date} - '
                  f'введенная дата {given_date_object} позже сегодняшнего дня')
        elif given_date_object == today_date:
            print(f'сегодня {today_date} - '
                  f'введенная дата {given_date_object} равна сегодняшнему дню')
        else:
            print(f'сегодня {today_date} - '
                  f'введенная дата {given_date_object} ранее сегодняшнего дня')
        proceed = input('повторить операцию? (y/n)')
        if proceed == 'n':
            break


given_date = input('введите первую дату в формате "ГГГГ-ММ-ДД":')


if __name__ == "__main__":
    task_eleven(given_date)
