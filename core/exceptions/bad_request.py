from rest_framework.exceptions import APIException


class BadRequest(APIException):
    """An exception class to represent HTTP 400 Bad Request errors.

    Attributes:
    - status_code (int): The HTTP status code for this error (400).
    - default_detail (str): A human-readable description of this error
      (i.e., 'Bad request').
    - default_code (str): A machine-readable identifier for this error
      (i.e., 'bad_request').
    """

    status_code = 400
    default_detail = "Bad request"
    default_code = "bad_request"
