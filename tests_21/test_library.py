"""Homework 21 Test case - Library with PYTEST"""

import logging
import pytest
from homework_12 import Book, Reader

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class TestLibrary:
    """
    TestLibrary class
    """
    book1_instance = Book(book_name="The Hobbit",
                          author="Books by J.R.R. Tolkien", num_pages=400, isbn="0000000001")

    book2_instance = Book(book_name="The 1984",
                          author="J.R.R.", num_pages=300, isbn="0000000002")

    reader1_instance = Reader("Vasya")
    reader2_instance = Reader("Petya")

    def test_reader_dicts_empty(self):
        """
        test_reader_dicts_empty fuc
        """
        assert not TestLibrary.reader1_instance.reservation_dict
        assert not TestLibrary.reader1_instance.taken_book_dict
        logger.info(f"checking empty dict for : reservation_dict:"
                    f"{TestLibrary.reader1_instance.reservation_dict} "
                    f"taken_book_dict: {TestLibrary.reader1_instance.taken_book_dict}")

    def test_reserve_book(self):
        """
        test_reserve_book fuc
        """
        TestLibrary.reader1_instance.reserve_book(TestLibrary.book1_instance)
        assert TestLibrary.book1_instance.book_is_reserved is True
        assert TestLibrary.book1_instance in TestLibrary.reader1_instance.reservation_dict
        assert TestLibrary.book2_instance not in TestLibrary.reader1_instance.reservation_dict
        logger.info(f"Attempted to reserve a book: {TestLibrary.reader1_instance.reader_name}"
                    f"book reservation status: {TestLibrary.reader1_instance.reservation_dict}")
        logger.info(f"Attempted to reserve a book: {TestLibrary.reader2_instance.reader_name} "
                    f"book reservation status: {TestLibrary.reader2_instance.reservation_dict}")
        # косяк приложения:
        assert TestLibrary.book1_instance in TestLibrary.reader2_instance.reservation_dict
        logger.info(f"check if book is reserved in {TestLibrary.reader2_instance.reader_name} "
                    f"reservation_dict:{TestLibrary.reader2_instance.reservation_dict}")
        TestLibrary.reader2_instance.reserve_book(TestLibrary.book1_instance)

    def test_cancel_reserve(self):
        """
        test_cancel_reserve fuc
        """
        TestLibrary.reader1_instance.cancel_reserve(TestLibrary.book1_instance)
        assert TestLibrary.book1_instance not in TestLibrary.reader1_instance.reservation_dict
        assert TestLibrary.book1_instance not in TestLibrary.reader2_instance.reservation_dict
        logger.info(f"cancel book's reserve: {TestLibrary.reader1_instance.reservation_dict}"
                    f"check book is not reserved in {TestLibrary.reader1_instance.reservation_dict}"
                    f"check book not reserved in {TestLibrary.reader2_instance.reservation_dict}")
        TestLibrary.reader2_instance.reserve_book(TestLibrary.book1_instance)
        TestLibrary.reader2_instance.reserve_book(TestLibrary.book2_instance)
        TestLibrary.reader1_instance.reserve_book(TestLibrary.book1_instance)
        TestLibrary.reader1_instance.cancel_reserve(TestLibrary.book2_instance)
        assert TestLibrary.book2_instance in TestLibrary.reader2_instance.reservation_dict
        logger.info(f"check if book {TestLibrary.book2_instance}"
                    f"is not reserved in {TestLibrary.reader2_instance.reservation_dict}")

    def test_get_book(self):
        """
        test_get_book fuc
        """
        # не консистентно, только для теста как работает:
        reader3_instance = Reader("Venja")
        reader4_instance = Reader("Solomon")
        book3_instance = Book(book_name="The 3",
                              author="Tolkien", num_pages=400, isbn="0000000001")
        book4_instance = Book(book_name="The 3",
                              author="Tolkien", num_pages=400, isbn="0000000001")
        reader3_instance.reserve_book(book3_instance)
        assert book3_instance.book_is_reserved is True
        logger.info(f"Attempted to reserve a book: {book3_instance} "
                    f"status: {book3_instance.book_is_reserved}")
        reader4_instance.get_book(book3_instance)
        assert book3_instance not in reader4_instance.taken_book_dict
        logger.info(f"Attempted to get a book: {book3_instance} "
                    f"status: {reader4_instance.taken_book_dict} "
                    f"for reader: {reader4_instance.reader_name}")
        reader3_instance.get_book(book3_instance)
        assert book3_instance in reader3_instance.taken_book_dict
        logger.info(f"Attempted to get a book: {book3_instance} "
                    f"status: {reader3_instance.taken_book_dict} "
                    f"for reader: {reader3_instance.reader_name}")
        reader3_instance.get_book(book4_instance)
        assert book4_instance in reader3_instance.taken_book_dict
        logger.info(f"Attempted to get a book: {book4_instance} "
                    f"status: {reader3_instance.taken_book_dict} "
                    f"for reader: {reader3_instance.reader_name}")

    def test_return_book(self):
        """
        test_return_book fuc
        """
        TestLibrary.book1_instance.book_is_reserved = False
        TestLibrary.reader1_instance.get_book(TestLibrary.book1_instance)
        TestLibrary.reader2_instance.return_book(TestLibrary.book1_instance)
        assert TestLibrary.book1_instance in TestLibrary.reader2_instance.taken_book_dict
        logger.info(f"Attempted to return a book: {TestLibrary.book1_instance.book_name}"
                    f"book status: {TestLibrary.reader2_instance.taken_book_dict}"
                    f"for books dict for reader: {TestLibrary.reader2_instance.reader_name}")
        TestLibrary.reader1_instance.return_book(TestLibrary.book1_instance)
        assert TestLibrary.book1_instance not in TestLibrary.reader1_instance.taken_book_dict
        logger.info(f"Attempted to return a book: {TestLibrary.book1_instance.book_name}"
                    f"book status: {TestLibrary.reader1_instance.taken_book_dict}"
                    f"book added to taken books dict"
                    f"for reader: {TestLibrary.reader1_instance.reader_name}")


# c использованием pytest:
# @pytest.fixture
# def reader_instance():
#     return Reader("Solomon")
#
# @pytest.fixture
# def reader2_instance():
#     return Reader("Solomon2")
#
# @pytest.fixture
# def book_instance():
#     return Book(book_name="The Hobbit",
#                 author="Books by J.R.R. Tolkien", num_pages=400, isbn="0006754023")
#
# @pytest.fixture
# def book2_instance():
#     return Book(book_name="Hobbit", author="by J.R.R.", num_pages=400, isbn="00067543")


def test_py_reserve_book(reader_instance, reader2_instance, book_instance, book2_instance):
    """
    test_py_reserve_book fuc
    """
    reader_instance.reserve_book(book_instance)
    assert book_instance.book_is_reserved is True
    assert book_instance in reader_instance.reservation_dict
    assert book2_instance not in reader_instance.reservation_dict
    logger.info(f"Attempted to reserve a book: {book_instance.book_name}"
                f"for reader: {reader_instance.reader_name}"
                f"book status: {book_instance.book_is_reserved}")
    # косяк приложения:
    assert book_instance in reader2_instance.reservation_dict
    logger.info(f"ERROR: Book: {book_instance.book_name}"
                f" added by default for reader: {reader2_instance.reader_name}"
                f"book status: {book_instance.book_is_reserved}")


def test_py_cancel_reserve(reader_instance, reader2_instance, book_instance, book2_instance):
    """
    test_py_cancel_reserve fuc
    """
    reader_instance.reserve_book(book_instance)
    assert book_instance in reader_instance.reservation_dict
    logger.info(f"Attempted to reserve a book: {book_instance.book_name} "
                f"book added to {reader_instance.reservation_dict}")
    # косяк:
    with pytest.raises(AssertionError):
        assert book_instance not in reader2_instance.reservation_dict
        logger.info(f"ERROR: book: {book_instance.book_name} "
                    f"book added to {reader2_instance.reservation_dict}")
    reader2_instance.reserve_book(book_instance)
    reader2_instance.reserve_book(book2_instance)
    reader_instance.cancel_reserve(book2_instance)
    assert book2_instance in reader_instance.reservation_dict
    logger.info(f"Attempted to cancel reserve for a book: {book_instance.book_name} "
                f"book added to {reader_instance.reservation_dict}")


def test_py_test_get_book(reader_instance, reader2_instance, book_instance, book2_instance):
    """
    test_py_test_get_book fuc
    """
    reader_instance.reserve_book(book_instance)
    assert book_instance.book_is_reserved is True
    logger.info(f"Attempted to reserve book: {book_instance.book_name} "
                f"status is reserved: {book_instance.book_is_reserved}")
    reader2_instance.get_book(book_instance)
    assert book_instance not in reader2_instance.taken_book_dict
    logger.info(f"Attempted to get book: {book_instance.book_name}"
                f"for reader: {reader2_instance.reader_name}"
                f"is added to: {reader2_instance.taken_book_dict}")
    reader_instance.get_book(book_instance)
    assert book_instance in reader_instance.taken_book_dict
    logger.info(f"Attempted to get book: {book_instance.book_name}"
                f"for reader: {reader_instance.reader_name}"
                f"is added to: {reader_instance.taken_book_dict}")
    reader_instance.get_book(book2_instance)
    assert book2_instance in reader_instance.taken_book_dict
    logger.info(f"Attempted to get book: {book2_instance.book_name}"
                f"for reader: {reader_instance.reader_name}"
                f"is added to: {reader_instance.taken_book_dict}")


def test_py_return_book(reader_instance, reader2_instance, book_instance):
    """
    test_py_return_book fuc
    """
    reader_instance.get_book(book_instance)
    reader2_instance.return_book(book_instance)
    assert book_instance in reader2_instance.taken_book_dict
    logger.info(f"Attempted to return book: {book_instance.book_name}"
                f"by reader: {reader2_instance.reader_name}"
                f"is added to: {reader2_instance.taken_book_dict}")
    reader_instance.return_book(book_instance)
    assert book_instance not in reader_instance.taken_book_dict
    logger.info(f"Attempted to return book: {book_instance.book_name}"
                f"by reader: {reader_instance.reader_name}"
                f"is added to: {reader_instance.taken_book_dict}")

# Некоторые примечания по итогу:
# 1. без использования класса тест потребовал бы фикстуры, и
# 2. при этом каждая функция работает как отдельный тест, что не требует отслеживания состояния
# instance на каждом из этапов/тестов
# 3. но с классом можно просто в каждой функции инициировать объект класса Reader, Book
# 4. + возможность накинуть фиктстуру на класс в дальнейшем, обойдясь без makrs для фикстур
