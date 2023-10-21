from rest_framework.exceptions import APIException


class InvalidPassword(APIException):
    """Exception raised when an API request fails due to an invalid password.

    Attributes:
        status_code (int): The HTTP status code to be returned to the client.
        default_detail (str): A human-readable message describing the error.
        default_code (str): A short error code that can be used programmatically.
    """

    status_code = 400
    default_detail = "Invalid password"
    default_code = "bad_request"
