from rest_framework.exceptions import APIException


class FieldDoesNotExist(APIException):
    """Custom exception class used to handle cases where an accessed model filed does not exist.

    Attributes:
        status_code (int): HTTP status code for the exception (set to 400).
        default_detail (str): Default message string for the exception (set to 'Provided attribute does not valid for instance).
        default_code (str): Default error code string for the exception (set to 'not_exist_attr_error').
    """

    status_code = 400
    default_detail = "Provided attribute does not valid for instance"
    default_code = "not_exist_attr_error"
