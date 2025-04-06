"""Homework 20 Test case - Book, Reader"""

import unittest
from hm20.hm_20 import Book, Reader


class TestBook(unittest.TestCase):
    """
    Test case for Book module
    """
    @classmethod
    def setUpClass(cls):
        cls.book = Book(book_name="TheTEST",
            author="The test author", num_pages=400, isbn="0006754023")

    @classmethod
    def tearDownClass(cls):
        del TestBook.book

    def test_book_exist(self):
        """
        Book is created test
        """
        self.assertIsInstance(TestBook.book.book_name, str)
        self.assertIsInstance(TestBook.book.author, str)
        self.assertIsInstance(TestBook.book.num_pages, int)
        self.assertIsInstance(TestBook.book.isbn, str)

    def test_reserve(self):
        """
        Book test_reserve func test
        """
        TestBook.book.reserve()
        self.assertTrue(TestBook.book.book_is_reserved)

    def test_cancel_reserve(self):
        """
        Book cancel_reserve func test
        """
        if not TestBook.book.book_is_reserved:
            TestBook.book.cancel_reserve()
            self.assertFalse(TestBook.book.book_is_reserved)

    def test_get_book(self):
        """
        Book get_book func test
        """
        TestBook.book.get_book()
        self.assertTrue(TestBook.book.book_is_taken)

    def test_return_book(self):
        """
        Book return_book func test
        """
        if not TestBook.book.book_is_taken:
            TestBook.book.return_book()
            self.assertFalse(TestBook.book.book_is_taken)

class TestReader(unittest.TestCase):
    """
    Test case for Book-Reader module
    """
    @classmethod
    def setUpClass(cls):
        cls.reader = Reader("Vasya")
        cls.book = Book(book_name="TheTEST",
             author="The test author", num_pages=400, isbn="0006754023")

    @classmethod
    def tearDownClass(cls):
        del TestReader.reader
        del TestReader.book

    def test_reader_exist(self):
        """
        Book is created test
        """
        self.assertIsInstance(TestReader.reader.reader_name, str)

    def test_reserve_book(self):
        """
        Reader reserve_book func test
        """
        TestReader.reader.reserve_book(TestReader.book)
        if TestReader.book.book_is_reserved:
            self.assertIsNotNone(TestReader.reader.reservation_dict[TestReader.book])
        else:
            self.assertIsNone(TestReader.reader.reservation_dict[TestReader.book])

    def test_cancel_reserve(self):
        """
        Reader cancel_reserve func test
        """
        self.assertNotIn(TestReader.book, TestReader.reader.reservation_dict)

    def test_get_book(self):
        """
        Reader get_book func test
        """
        if not TestReader.book.book_is_reserved:
            TestReader.reader.get_book(TestReader.book)
            self.assertIn(TestReader.book, TestReader.reader.taken_book_dict)

    def test_return_book(self):
        """
        Reader return_book func test
        """
        TestReader.reader.return_book(TestReader.book)
        self.assertNotIn(TestReader.book, TestReader.reader.taken_book_dict)


if __name__ == '__main__':
    unittest.main()
