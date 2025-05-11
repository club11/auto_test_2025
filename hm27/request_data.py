"""API request functions"""


import json
import requests
from hm28.API.conf_data import Conf, RequiredData


def get_booking_ids():
    """get booking ids"""
    endpoint = "/booking"
    try:
        response = requests.get(
            f"{Conf.URL}{endpoint}", timeout=5
        )
        return response
    except requests.exceptions.RequestException:
        return None


def get_booking_by_id(booking_id=1):
    """Get booking by id"""
    endpoint = f"/booking/{booking_id}"
    headers = {
        "Accept": "application/json",
    }
    try:
        response = requests.get(
            f"{Conf.URL}{endpoint}", headers=headers, timeout=5
        )
        return response
    except requests.exceptions.RequestException:
        return None


def create_booking(token):
    """Create booking for id"""
    endpoint = "/booking"
    payload = json.dumps(RequiredData.CreateBookingData)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.post(
            f"{Conf.URL}{endpoint}", data=payload, headers=headers,  timeout=5
        )
        return response
    except requests.exceptions.RequestException:
        return None


def update_booking(token, booking_id):
    """Update booking by id"""
    endpoint = f"/booking/{booking_id}"
    payload = json.dumps(RequiredData.UpdateBookingData)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}",
    }
    try:
        response = requests.put(
            f"{Conf.URL}{endpoint}", data=payload, headers=headers, timeout=5
        )
        return response
    except requests.exceptions.RequestException:
        return None


def partial_update_booking(token, booking_id):
    """Partial update of booking by id"""
    endpoint = f"/booking/{booking_id}"
    payload = json.dumps(RequiredData.UpdatePartialBookingData)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}",
    }
    try:
        response = requests.patch(
            f"{Conf.URL}{endpoint}", data=payload, headers=headers, timeout=5
        )
        return response
    except requests.exceptions.RequestException:
        return None
