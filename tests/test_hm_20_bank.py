"""Homework 20 Test case - Bank"""

import unittest
from hm20.hm_20 import Bank


class TestBank(unittest.TestCase):
    """
    Test case for Bank module
    """
    @classmethod
    def setUpClass(cls):
        cls.client = Bank()

    def test_register_client(self):
        """
        Bank register_client func test
        """
        TestBank.client.register_client(client_id="0000001", name="test_client")
        self.assertIsNotNone(TestBank.client.client_id)
        self.assertIsNotNone(TestBank.client.name)
        self.assertIsInstance(TestBank.client.client_id, str)
        self.assertIsInstance(TestBank.client.name, str)

    def test_deposit_account(self):
        """
        deposit account exist
        """
        TestBank.client.register_client(client_id="0000001", name="test_client")
        TestBank.client.open_deposit_account(client_id="0000001", start_balance=100000, years=1)
        self.assertEqual(TestBank.client.client_id, "0000001")
        self.assertEqual(TestBank.client.start_balance, 100000)
        self.assertEqual(TestBank.client.years, 1)

    def test_calc_interest_rate(self):
        """
        Bank calc_interest_rate func test
        """
        TestBank.client.register_client(client_id="0000001", name="test_client")
        TestBank.client.open_deposit_account(client_id="0000001", start_balance=100000, years=1)
        self.assertIsNotNone(TestBank.client.calc_interest_rate(client_id="0000001"))

    def test_close_deposit(self):
        """
        Bank close_deposit func test
        """
        TestBank.client.register_client(client_id="0000001", name="test_client")
        TestBank.client.open_deposit_account(client_id="0000001", start_balance=100000, years=1)
        TestBank.client.close_deposit(client_id="0000001")
        self.assertEqual(TestBank.client.start_balance, 0)


if __name__ == '__main__':
    unittest.main()
