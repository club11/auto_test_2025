"""Contest file"""

import json
import pytest
import requests
# from hm28.API.conf_data import Conf, RequiredData
from conf_data import Conf, RequiredData


@pytest.fixture
def get_token():
    """Receive a token."""
    endpoint = "/auth"
    payload = json.dumps(RequiredData.RegisterData)
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            f"{Conf.URL}{endpoint}", headers=headers, data=payload, timeout=5
        )
        return response.json()["token"]
    except requests.exceptions.RequestException:
        return None
