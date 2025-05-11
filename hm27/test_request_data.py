"""Tests API"""

#from Tests.config.config_log import logger
from hm28.API.request_data import (
    get_booking_ids,
    get_booking_by_id,
    create_booking,
    update_booking,
    partial_update_booking,
)


def test_get_booking_ids():
    """
    test get booking ids
    """
    res = get_booking_ids()
    assert res.status_code == 200, f"Expected 200, but got {res.status_code}"


def test_get_booking_by_id(get_token):
    """
    test get token
    """
    booking_created = create_booking(get_token)
    res = get_booking_by_id(booking_id=booking_created.json()['bookingid'])
    assert res.status_code == 200, f"Expected 200, but got {res.status_code}"
    assert res.json()['firstname'] == 'Jim'


def test_create_booking(get_token):
    """
    test create booking
    """
    res = create_booking(get_token)
    assert res.status_code == 200, f"Expected 200, but got {res.status_code}"
    assert res.json()['booking']['firstname'] == 'Jim'


def test_update_booking(get_token):
    """
    test update booking
    """
    booking_created = create_booking(get_token)
    res = update_booking(token=get_token, booking_id=booking_created.json()['bookingid'])
    assert res.status_code == 200, f"Expected 200, but got {res.status_code}"


def test_partial_update_booking(get_token):
    """
    test partial update booking
    """
    booking_created = create_booking(get_token)
    res = partial_update_booking(token=get_token, booking_id=booking_created.json()['bookingid'])
    assert res.status_code == 200, f"Expected 200, but got {res.status_code}"
