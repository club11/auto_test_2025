"""Homework 20 Test case - Bank"""

import unittest
from hm20.hm_20 import Bank


class TestBank(unittest.TestCase):
    """
    Test case for Bank module
    """
    @classmethod
    def setUpClass(cls):
        cls.bank = Bank()
        start_balance = 100000
        client_id = "0000001"
        client_name = 'test_client'
        years = 1
        TestBank.bank.register_client(client_id, client_name)
        TestBank.bank.open_deposit_account(client_id, start_balance, years)
        cls.money_to_return = TestBank.bank.calc_interest_rate(client_id)

    @classmethod
    def tearDownClass(cls):
        del TestBank.bank

    def test_register_client(self):
        """
        Bank register_client func test
        """
        self.assertIsNotNone(TestBank.bank.client_id)
        self.assertIsNotNone(TestBank.bank.name)
        self.assertIsInstance(TestBank.bank.client_id, str)
        self.assertIsInstance(TestBank.bank.name, str)

    def test_open_deposit_account(self):
        """
        Bank open_deposit_account func test
        """
        self.assertIsNotNone(TestBank.bank.start_balance)
        self.assertIsNotNone(TestBank.bank.years)
        self.assertIsInstance(TestBank.bank.start_balance, int)
        self.assertIsInstance(TestBank.bank.years, int)

    def test_calc_interest_rate(self):
        """
        Bank calc_interest_rate func test
        """
        self.assertIsNotNone(self.money_to_return)
        self.assertIsInstance(self.money_to_return, float)

    def test_close_deposit(self):
        """
        Bank close_deposit func test
        """
        self.assertIsNotNone(TestBank.bank.start_balance)
        self.assertEqual(TestBank.bank.start_balance, 0)

    @unittest.expectedFailure
    def test_close_deposit_not_success(self):
        """
        ожидаемая ошибка наличия денег на закрытом счете
        """
        self.assertIsNotNone(TestBank.bank.start_balance)
        self.assertNotEqual(TestBank.bank.start_balance, 0)

    @unittest.expectedFailure
    def test_client_is_not_deleted(self):
        """
        ожидаемая ошибка - тестовый клиент не удален
        """
        self.assertIsNone(TestBank.bank)


if __name__ == '__main__':
    unittest.main()
