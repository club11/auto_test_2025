"""Homework 12"""

import logging

logging.basicConfig(level=logging.INFO, filename="py_21log.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


# 1. Банковский вклад
class Bank:
    """
    class Bank for all operations
    """
    client_index = 0
    client_id = None
    name = None
    start_balance = None
    years = None
    annual_interest_rate = 12 / 100
    capitalization_number = 4

    def register_client(self, client_id, name):
        """
         register_client
        """
        # Bank.client_index += 1
        self.name = name
        self.client_id = client_id
        logging.info(f"(register_client) Attempt to register a client"
                     f" for client_id: {self.client_id} for client name: {self.name}")

    def open_deposit_account(self, client_id, start_balance, years):
        """
         open_deposit_account
        """
        if self.client_id == client_id:
            self.start_balance = start_balance
            self.years = years
            logging.info(f"(open_deposit_account) Attempt open deposit account a client"
                         f" for client_id: {self.client_id}, "
                         f"start_balance: {self.start_balance}, years: {years}")

    def calc_interest_rate(self, client_id):
        """
         calculate the interest rate
        """
        if self.client_id == client_id:
            capitalization_for_period = self.annual_interest_rate / self.capitalization_number
            money_to_return = self.start_balance
            for _ in range(self.capitalization_number):
                money_to_return += money_to_return * capitalization_for_period
            answer_is = round(money_to_return, 2)  # до 2 знаков вместо формата + переменная!
            logging.info(f"(calc_interest_rate) Attempt to calculate clients interest rate"
                         f" for client_id: {self.client_id}, money to return: {answer_is}")
            return answer_is
        logging.info("(calc_interest_rate) no money to return")
        return 'No money - no honey'

    def close_deposit(self, client_id):
        """
         close_deposit
        """
        if self.client_id == client_id:
            self.start_balance = 0
            logging.info(f"(calc_interest_rate) Attempt to close clients deposit"
                         f" for client_id: {self.client_id}, balance is: {self.start_balance}."
                         f" Deposit os closed")


# 2. Библиотека aka library;
class Book:
    """
    class Book
    """

    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.book_is_reserved = False
        self.book_is_taken = False
        logging.info(f"(register_client): Attempt to initialize a book object"
                     f" book name: {self.book_name}, author: {self.author},"
                     f"num_pages: {self.num_pages}, isbn: {self.isbn},"
                     f"book reserve status: is reserved: {self.book_is_reserved},"
                     f"book taken status: is reserved: {self.book_is_taken}")

    def reserve(self):
        """
         to reserve a book
        """
        self.book_is_reserved = True
        logging.info("(reserve): book is reserved")
        return self.book_is_reserved

    def cancel_reserve(self):
        """
         cancel the reservation of a book
        """
        self.book_is_reserved = False
        logging.info(f"(cancel_reserve): cancel reserve of book {self.book_is_reserved}")
        return self.book_is_reserved

    def get_book(self):
        """
        get a book from the pool
        """
        self.book_is_taken = True
        logging.info(f"(get_book): get book, taken book status: {self.book_is_taken}")
        return self.book_is_taken

    def return_book(self):
        """
        return a book to the pool
        """
        self.book_is_taken = False
        logging.info("(return_book): return book, book status: is returned")
        return self.book_is_taken


class Reader:
    """
    class Reader
    """
    reservation_dict = {}  # type: dict
    taken_book_dict = {}  # type: dict

    def __init__(self, reader_name):
        self.reader_name = reader_name

    def reserve_book(self, a_book):
        """
        order a reservation of book from the pool
        """
        if not a_book.book_is_reserved:
            a_book.reserve()
            Reader.reservation_dict[a_book] = self
            logging.info("(reserve_book): book is reserved")
            return Reader.reservation_dict
        logging.error('(reserve_book): cannot reserve - a book is not reserved')
        return Reader.reservation_dict

    def cancel_reserve(self, a_book):
        """
        decline a reservation book from the pool
        """
        if Reader.reservation_dict[a_book] == self:
            a_book.cancel_reserve()
            self.reservation_dict.pop(a_book)
            logging.info('(cancel_reserve): book reservation is canceled')
            return self.reservation_dict
        logging.info('(cancel_reserve): cannot cancel reserve - '
                     'a book is not reserved by this reader')
        return self.reservation_dict

    def get_book(self, a_book):
        """
        return a book from the pool
        """
        if not a_book.book_is_reserved:
            a_book.get_book()
            Reader.taken_book_dict[a_book] = self
            logging.info(f'(get_book): book {a_book.book_name} '
                         f'is taken by reader: {Reader.__name__}')
        elif Reader.reservation_dict[a_book] == self:
            a_book.get_book()
            self.cancel_reserve(a_book)
            Reader.taken_book_dict[a_book] = self
            logging.info(f'(get_book): book {a_book.book_name} '
                         f'is taken by reader: {Reader.__name__}')
        else:
            logging.info('(get_book): cannot get a book - is already taken by another reader')

    def return_book(self, a_book):
        """
        return a book to the pool
        """
        if Reader.taken_book_dict[a_book] == self:
            a_book.return_book()
            Reader.taken_book_dict.pop(a_book)
            logging.error(f'(return_book): book {a_book.book_name} '
                          f'is returned by reader {Reader.__name__}')
            return Reader.taken_book_dict
        logging.error('(return_book): cannot return a book - '
                      'is already taken by another reader')
        return print('cannot return a book')


if __name__ == "__main__":
    bank = Bank()
    bank.register_client(client_id="0000001", name="Siarhei")
    bank.open_deposit_account(client_id="0000001", start_balance=100000, years=1)
    ass = bank.calc_interest_rate(client_id="0000001")
    bank.close_deposit(client_id="0000001")
    book_obj = Book(book_name="The Hobbit",
                    author="Books by J.R.R. Tolkien", num_pages=400, isbn="0000000001")
    reader1_instance = Reader("Vasya")
    reader2_instance = Reader("Petja")
    reader1_instance.reserve_book(book_obj)
    reader1_instance.get_book(book_obj)
    reader1_instance.return_book(book_obj)
