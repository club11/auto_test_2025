"""Homework 21 Test case - Bank with PYTEST"""

import logging
import pytest
from homework_12 import Bank

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

# @pytest.fixture
# def initialize_bank():
#     bank_instance = Bank()
#     bank_instance.register_client(client_id="0000001", name="Siarhei")
#     logger.info(f"initialize a client: {bank_instance.client_id} {bank_instance.name}")
#     return bank_instance

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
    assert bank.client_id== "0000001"
    assert bank.name == "Siarhei"
    logger.info(f"initialize a client test_register_client: {bank.client_id} {bank.name}")

# С применением @pytest.fixture
def test_open_deposit_account(initialize_bank, request):
    """
    test_open_deposit_account fuc
    """
    # if request.config.getoption("--debug"):
    #     print('ERROR - вот здесь некоторый проблемный момент')
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    logging.info(f"Attempted to initialize depo account for client: {initialize_bank.client_id} "
                 f"start_balance: {initialize_bank.start_balance} years: {initialize_bank.years}.")
    assert initialize_bank.client_id == "0000001"
    assert initialize_bank.start_balance == 100000
    assert initialize_bank.years == 1
    logger.info(f"open_deposit_account: client_id: {initialize_bank.client_id} "
                f"start_balance: {initialize_bank.start_balance} years: {initialize_bank.years} ")

def test_close_deposit(initialize_bank):
    """
    test_close_deposit fuc
    """
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    initialize_bank.close_deposit(client_id="0000001")
    assert initialize_bank.start_balance == 0
    logger.info(f"close_deposit: client_id: {initialize_bank.client_id} "
                f"client balance: {initialize_bank.start_balance}")

def test_calc_interest_rate(initialize_bank):
    """
    test_calc_interest_rate fuc
    """
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    assert initialize_bank.calc_interest_rate(initialize_bank.client_id) == 112550.88
    logger.info(f"calc_interest_rate: client_id: {initialize_bank.client_id} "
                f"interest_rate: {initialize_bank.calc_interest_rate(initialize_bank.client_id)}")

def test_wrong_capitalization_number(initialize_bank):
    """
    test_wrong_capitalization_number fuc
    """
    initialize_bank.open_deposit_account("0000001", start_balance=100000, years=1)
    initialize_bank.capitalization_number = 0
    with pytest.raises(ZeroDivisionError):
        initialize_bank.calc_interest_rate(initialize_bank.client_id)
    logger.info(f"test wrong capitalization number (0): client_id: {initialize_bank.client_id} "
                f"start_balance: {initialize_bank.start_balance} "
                f"capitalization_number: {initialize_bank.capitalization_number}")
