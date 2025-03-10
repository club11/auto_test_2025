"""Homework 13"""


# 1. Колода карт "Without us, you don't have any cards". Some guy
import random
import requests
from homework_12 import Bank
# from typing import Dict
# from homework_13_1 import task_three_func
ALL_CURRENCIES_ENDPOINT = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'


class Card:
    """
    class Card
    """
    number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 'Jocker']
    mast_list = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    def __init__(self, number_list, mast_list):
        if number_list == 'Jocker':
            self.number_list = number_list
            self.mast_list = None
        else:
            self.number_list = number_list
            self.mast_list = mast_list

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


class CardsDeck:
    """
    class CardsDeck
    """
    # card_in_deck_dict = Dict[CardsDeck] - not work
    # card_in_deck_dict = Dict[dict] - same
    card_in_deck_dict = {'obj':'num'}

    def __init__(self):
        deck_lict = []
        for n_1 in Card.number_list[:-1]:
            for k in Card.mast_list:
                some_values = n_1, k
                deck_lict.append(some_values)
        deck_lict.append(('Jocker', None))
        deck_lict.append(('Jocker', None))
        deck_lict = dict(enumerate(deck_lict))

        for u_have_no_cards, we_do in deck_lict.items():
            if we_do[0] != 'Jocker':  # несколько коряво-нужно условие!!
                # print(we_do[0], we_do[1])
                some_card = Card(we_do[0], we_do[1])
                self.card_in_deck_dict[u_have_no_cards+1] = some_card
            else:
                # print(we_do[0])
                some_card = Card(we_do[0], None)
                self.card_in_deck_dict[u_have_no_cards+1] = some_card

    @staticmethod
    def shuffle():
        """
        get random card
        """
        random_card_num = random.choice(Card.number_list)
        random_card_suit = random.choice(Card.mast_list)
        return random_card_num, random_card_suit

    @staticmethod
    def get(card_number):
        """
        return a card by its number
        """
        users_card_number = CardsDeck.card_in_deck_dict[card_number]
        if not users_card_number.mast_list:
            return print(f'You card is: {users_card_number.number_list}')
        return print(f'You card is: 'f'{users_card_number.number_list}, '
                     f'{users_card_number.mast_list}')

def task_one_func():
    """
    getting a card by its number
    """
    deck = CardsDeck()
    deck.shuffle()
    card_number = None
    while card_number != 'n':
        card_number = int(input('Выберите карту из колоды в 54 карт:'))
        if card_number > 54:
            continue
        return deck.get(card_number)
    return 'card is not found'


# 2. Конвертер валют
class Person:
    """
    class Person
    """
    def __init__(self, curr, amount):
        self.curr = curr
        self.amount = amount

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


class CurrencyConverter(Bank):
    """
    class CurrencyConverter
    """
    currency_dict = {}
    currency_input = None
    amount_num = None
    exchange_output = None

    @staticmethod
    def currency():
        """
        return a card by its number
        """
        for valuta in requests.get(ALL_CURRENCIES_ENDPOINT, timeout=5).json():
            curr_value = valuta.get('Cur_OfficialRate')
            CurrencyConverter.currency_dict[valuta.get('Cur_Abbreviation')] = curr_value

    def exchange_currency(self, currency_input, amount_num, exchange_output=None):
        """
        calculate the exchange
        """
        self.currency_input = currency_input
        self.amount_num = amount_num
        self.exchange_output = exchange_output
        if not exchange_output and CurrencyConverter.currency_dict.get(currency_input):
            converted_val = amount_num * CurrencyConverter.currency_dict.get(currency_input)
            return print(converted_val, 'BYN')
        if exchange_output and CurrencyConverter.currency_dict.get(exchange_output):
            converted_val = (amount_num * CurrencyConverter.currency_dict.get(currency_input)
                             / CurrencyConverter.currency_dict.get(exchange_output))
            return print(converted_val, exchange_output)
        return print('invalid data')

# vasya = Person('USD', 10)
# petya = Person('EUR', 5)
# converter = CurrencyConverter()
# converter.currency()
# converter.exchange_currency(vasya.curr, vasya.amount)
# converter.exchange_currency(petya.curr, petya.amount, 'USD')


def task_two_func():
    """
    gimme_money - currency convertor!
    """
    skip_finally = False
    converter = CurrencyConverter()
    converter.currency()
    while skip_finally != 'n':
        print('варианты валют:', CurrencyConverter.currency_dict.keys())
        currency_input = input("введите валюту, WOULD YOU KINDLY!: ")
        amount = ''
        while not amount.isdigit():
            amount = input("введите денюжку, WOULD YOU KINDLY!: ")
        print('варианты валют:', CurrencyConverter.currency_dict.keys())
        currency_output = input("введите вожделенную валюту, WOULD YOU KINDLY!: ")
        users_values = Person(currency_input, int(amount))
        if not CurrencyConverter.currency_dict[currency_output]:
            converter.exchange_currency(users_values.curr, users_values.amount)
        else:
            converter.exchange_currency(users_values.curr, users_values.amount, currency_output)
        skip_finally = input("would u like to proceed, WOULD YOU KINDLY! (y/n): ")

# 3. Из молекулы в атомы *
# task3:
# first var. with MVP status
# overcomplicated and hard to resolve quickly


if __name__ == "__main__":
    task_one_func()
    task_two_func()
    # for n in ['K45[ON2]2N6', 'K45[ON(KSO3)2]2N6', 'K45[ON(KSO3)2]2(KSO3)2KSO3N6']:
    #     task_three_func(n)
