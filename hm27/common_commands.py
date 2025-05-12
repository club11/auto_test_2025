"""A helper file with common func"""

import requests
from hm28.API.conf_data import Conf, RequiredData


def make_request(request_method, an_url, a_data=None, a_header=None, a_timeout=5):
    """
    common request func
    """
    try:
        response = request_method(
                f"{an_url}", data=a_data, headers=a_header, timeout=a_timeout
        )
        return response
    except requests.exceptions.RequestException:
        return None
