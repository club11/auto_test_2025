"""Test data for API testing"""


class Conf:
    """
    URL
    """
    URL = "https://restful-booker.herokuapp.com"

    def get_url(self):
        """
        get URL
        """
        Conf.URL = input()
        return self.URL

    def show_url(self):
        """
        show url
        """
        return print(self.URL)


class RequiredData:
    """
    Test required data
    """
    RegisterData = {
        "username": "admin",
        "password": "password123"
    }
    CreateBookingData = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    UpdateBookingData = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    UpdatePartialBookingData = {
        "firstname": "James",
        "lastname": "Brown"
    }

    @staticmethod
    def class_name():
        """
        show class name
        """
        class_name = 'RequiredData'
        return print(class_name)

    def show_data_fields(self):
        """
        show class fields
        """
        return print(
            self.RegisterData,
            self.CreateBookingData,
            self.UpdateBookingData,
            self.UpdatePartialBookingData,
        )
