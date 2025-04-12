"""Homework 21 Test case - Bank with PYTEST"""

import logging
import pytest
from homework_12 import Bank

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# С применением @pytest.mark.parametrize
@pytest.mark.parametrize(
    'bank, a, b', [
        (Bank(), "0000001", "Siarhei")
    ]
)
def test_register_client(bank, a, b):
    """
    test_register_client fuc
    """
    bank.register_client(a, b)
    assert bank.client_id == "0000001"
    assert bank.name == "Siarhei"


# С применением @pytest.fixture
def test_open_deposit_account(initialize_bank):
    """
    test_open_deposit_account fuc
    """
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    assert initialize_bank.client_id == "0000001"
    assert initialize_bank.start_balance == 100000
    assert initialize_bank.years == 1


def test_close_deposit(initialize_bank):
    """
    test_close_deposit fuc
    """
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    initialize_bank.close_deposit(client_id="0000001")
    assert initialize_bank.start_balance == 0


def test_calc_interest_rate(initialize_bank):
    """
    test_calc_interest_rate fuc
    """
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    assert initialize_bank.calc_interest_rate(initialize_bank.client_id) == 112550.88


def test_wrong_capitalization_number(initialize_bank):
    """
    test_wrong_capitalization_number fuc
    """
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    initialize_bank.capitalization_number = 0
    with pytest.raises(ZeroDivisionError):
        initialize_bank.calc_interest_rate(initialize_bank.client_id)
