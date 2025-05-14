"""API request functions"""


import json
import requests
from common_commands import make_request
from hm28.API.conf_data import Conf, RequiredData


def get_booking_ids():
    """get booking ids"""
    endpoint = "/booking"
    return make_request(requests.get, f"{Conf.URL}{endpoint}")


def get_booking_by_id(booking_id=1):
    """Get booking by id"""
    endpoint = f"/booking/{booking_id}"
    return make_request(requests.get, f"{Conf.URL}{endpoint}")


def create_booking(token):
    """Create booking for id"""
    endpoint = "/booking"
    payload = json.dumps(RequiredData.CreateBookingData)
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    return make_request(
        requests.post, f"{Conf.URL}{endpoint}", a_data=payload, a_header=headers
    )


def update_booking(token, booking_id):
    """Update booking by id"""
    endpoint = f"/booking/{booking_id}"
    payload = json.dumps(RequiredData.UpdateBookingData)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}",
    }
    return make_request(
        requests.put, f"{Conf.URL}{endpoint}", a_data=payload, a_header=headers
    )


def partial_update_booking(token, booking_id):
    """Partial update of booking by id"""
    endpoint = f"/booking/{booking_id}"
    payload = json.dumps(RequiredData.UpdatePartialBookingData)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}",
    }
    return make_request(
        requests.patch, f"{Conf.URL}{endpoint}", a_data=payload, a_header=headers
    )
