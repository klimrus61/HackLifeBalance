from rest_framework.exceptions import APIException


class GoogleTokenInvalid(APIException):
    """An exception class to represent HTTP 400 invalid token errors for Google authentication.

    Attributes:
    - status_code (int): The HTTP status code for this error (400).
    - default_detail (str): A human-readable description of this error
      (i.e., 'Google token invalid or has expired').
    - default_code (str): A machine-readable identifier for this error
      (i.e., 'bad_request').

    Usage:
    When the Google token is invalid or has expired during authentication, an instance of
    InvalidToken class is raised along with a message "Google token invalid or has expired".
    """

    status_code = 400
    default_detail = "Google token invalid or has expired"
    default_code = "bad_request"
