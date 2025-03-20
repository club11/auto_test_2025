"""Homework 15 - 10. Datetime """

import datetime


def task_ten(first_date_str, second_date_str):
    """
    two dates difference in days
    """
    while True:
        first_date_object = datetime.datetime.strptime(first_date_str, '%Y-%m-%d')
        second_date_object = datetime.datetime.strptime(second_date_str, '%Y-%m-%d')
        # something is not working as it was intended here:
        # time_diff = relativedelta(second_date_object, first_date_object).date
        # print("количество дней:", time_diff.days)
        # simple approach instead:
        print("количество дней:", (second_date_object - first_date_object).days)
        proceed = input('повторить операцию? (y/n)')
        if proceed == 'n':
            break


first_date = input('введите первую дату в формате "ГГГГ-ММ-ДД":')
second_date = input('введите вторую дату в формате "ГГГГ-ММ-ДД":')

if __name__ == "__main__":
    task_ten(first_date, second_date)
