"""Homework 14 - 4.
 4. В предложении допущены ошибки. Необходимо исправить каждый такой
 повтор (слово, один или несколько пробельных символов, и снова то же слово).
"""

import re

A_STRING = ("Довольно  распространённая ошибка  ошибка — это лишний повтор повтор слова слова. "
            "Смешно, не не правда ли? Не нужно портить хор хоровод")


def task_four(some_task):
    """
    replace text
    """
    pattern = re.compile(r'\s{2}')
    sentence = re.sub(pattern, ' ', some_task)
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


    return change_sentence(final_string_is, to_change_is)


if __name__ == "__main__":
    task_four(A_STRING)
