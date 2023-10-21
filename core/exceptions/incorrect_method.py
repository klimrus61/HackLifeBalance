from rest_framework.exceptions import APIException


class IncorrectMethod(APIException):
    """Custom exception for HTTP 418 when a user already exists in the current team.

    Attributes:
    -----------
    - status_code: int
        The HTTP status code, which is set to 418.
    - default_detail: str
        The default error detail message, which is 'User is already member of current team'.
    - default_code: str
        The default error code, which is 'I’m_a_teapot'.
    """

    status_code = 418
    default_detail = "Incorrect method"
    default_code = "I’m_a_teapot"
