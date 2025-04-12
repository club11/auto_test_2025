"""Homework 21 Test case - conf test"""

import sys
import pytest
from loguru import logger
from homework_12 import Bank, Reader, Book
# import logging


def pytest_addoption(parser):
    """"
     pytest_addoption func
    """
    parser.addoption(
        "--log_level", default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )


@pytest.fixture(scope="session", autouse=True)
def logging_status(request):
    """"
     логирование в консоль - но оно не срабатывает
    """
    loging_level = request.config.getoption("--log_level")
    logger.remove()
    logger.add(
        sys.stdout,
        level=loging_level,
        colorize=True,
        format="<magenta><u><i>{time:YYYY-MM-DD HH:mm:ss}</i></u>"
               "</magenta> <magenta><u><i>{message}</i></u></magenta>",
    )


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
