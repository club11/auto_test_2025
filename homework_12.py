"""Homework 12"""


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

    def open_deposit_account(self, client_id, start_balance, years):
        """
         open_deposit_account
        """
        if self.client_id == client_id:
            self.start_balance = start_balance
            self.years = years

    def calc_interest_rate(self, client_id):
        """
         calculate the interest rate
        """
        if self.client_id == client_id:
            capitalization_for_period = self.annual_interest_rate / self.capitalization_number
            money_to_return = self.start_balance
            for _ in range(self.capitalization_number):
                money_to_return += money_to_return * capitalization_for_period
                print('money_to_return', money_to_return)
            # More than one statement on a single line (multiple-statements):
            # for n in range(self.capitalization_number):money_to_return += \
            # Unused variable 'n' (unused-variable):
            # (Decimal(money_to_return) * Decimal(capitalization_for_period))
            answer_is = round(money_to_return, 2)  # до 2 знаков вместо формата + переменная!
            return answer_is
        return 'No money - no honey'

    def close_deposit(self, client_id):
        """
         close_deposit
        """
        if self.client_id == client_id:
            self.start_balance = 0


bank = Bank()
bank.register_client(client_id="0000001", name="Siarhei")
# print(bank.client_index, bank.name)
bank.open_deposit_account(client_id="0000001", start_balance=100000, years=1)
# print(bank.start_balance)
ass = bank.calc_interest_rate(client_id="0000001")
# print(ass, '===')
bank.close_deposit(client_id="0000001")


# 2. Библиотека aka library;
class Book:
    """
    class Book
    """
    # book_is_reserved = False
    # book_is_taken = False

    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.book_is_reserved = False
        self.book_is_taken = False


    def reserve(self):
        """
         to reserve a book
        """
        self.book_is_reserved = True

    def cancel_reserve(self):
        """
         cancel the reservation of a book
        """
        self.book_is_reserved = False

    def get_book(self):
        """
        get a book from the pool
        """
        self.book_is_taken = True

    def return_book(self):
        """
        return a book to the pool
        """
        self.book_is_taken = False


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
            Reader.reservation_dict[a_book] = self  # заменить на @classmethod
            print('book is reserved')
        else:
            print('cannot reserve - a book is reserved')

    def cancel_reserve(self, a_book):
        """
        decline a reservation book from the pool
        """
        if Reader.reservation_dict[a_book] == self:
            a_book.cancel_reserve()
            self.reservation_dict.pop(a_book)
        else:
            print('cannot cancel reserve - a book is not reserved by this User')

    def get_book(self, a_book):
        """
        return a book from the pool
        """
        if not a_book.book_is_reserved:
            a_book.get_book()
            Reader.taken_book_dict[a_book] = self
        elif Reader.reservation_dict[a_book] == self:
            a_book.get_book()
            self.cancel_reserve(a_book)
            Reader.taken_book_dict[a_book] = self
        else:
            print('cannot get a book  - is already taken by another User')

    def return_book(self, a_book):
        """
        return a book to the pool
        """
        if Reader.taken_book_dict[a_book] == self:
            a_book.return_book()
            Reader.taken_book_dict.pop(a_book)


book = Book(book_name="The Hobbit",
            author="Books by J.R.R. Tolkien", num_pages=400, isbn="0006754023")
book_2 = Book(book_name="The Lord Of The Rings",
            author="Books by J.R.R. Tolkien", num_pages=800, isbn="0006777023")

pool_of_books = [book, book_2]

vasya = Reader("Vasya")
petya = Reader("Petya")

for the_book in pool_of_books:
    vasya.reserve_book(the_book)
    petya.reserve_book(the_book)
    vasya.cancel_reserve(the_book)
    petya.reserve_book(the_book)

    vasya.get_book(the_book)
    petya.get_book(the_book)
    vasya.return_book(the_book)
    petya.return_book(the_book)
    vasya.get_book(the_book)
