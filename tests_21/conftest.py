"""Homework 21 Test case - conf test"""

import pytest
from homework_12 import Bank, Reader, Book

# def pytest_addoption(parser):
#     """"
#      pytest_addoption func
#     """
#     parser.addoption(
#         "--debug", action="store_true", help="Enable debugging output"
#     )


@pytest.fixture
def initialize_bank():
    """"
    initialize_bank fixture
    """
    bank_instance = Bank()
    bank_instance.register_client(client_id="0000001", name="Siarhei")
    return bank_instance


@pytest.fixture
def reader_instance():
    """"
    reader_instance fixture
    """
    return Reader("Solomon")


@pytest.fixture
def reader2_instance():
    """"
    reader2_instance fixture
    """
    return Reader("Solomon2")


@pytest.fixture
def book_instance():
    """"
    book_instance fixture
    """
    return Book(book_name="The Hobbit",
                author="Books by J.R.R. Tolkien", num_pages=400, isbn="0006754023")


@pytest.fixture
def book2_instance():
    """"
    book2_instance fixture
    """
    return Book(book_name="Hobbit", author="by J.R.R.", num_pages=400, isbn="00067543")
