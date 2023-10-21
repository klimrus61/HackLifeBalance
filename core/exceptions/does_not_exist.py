from rest_framework.exceptions import APIException


class DoesNotExist(APIException):
    """Custom exception class used to handle cases where an API object does not exist.

    Attributes:
        status_code (int): HTTP status code for the exception (set to 404).
        default_detail (str): Default message string for the exception (set to 'Does not exists').
        default_code (str): Default error code string for the exception (set to 'not_found').
    """

    status_code = 400
    default_detail = "Does not exist"
    default_code = "not_found"
