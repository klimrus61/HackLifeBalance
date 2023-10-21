from datetime import datetime, timezone

import requests
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core import cache
from django.db import models, transaction
from django.http import HttpRequest
# from redisq.tasks import MessageTasks
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from core.exceptions import (
    BadRequestException,
    GoogleTokenInvalidException,
    InvalidAuthTypeException,
)

from ..models import (
    UserAuthTypeModel,
    UserModel,
)
from ..serializers import (
    UserRefreshRequestSerializer,
)
from ..services import UserManagerService

@transaction.atomic
def google_auth_core(request: HttpRequest) -> UserModel:
    """This function validates the user's Google access token and returns a token if valid.

    Args:
    - request: Django's HttpRequest object that contains the user's access token.

    Returns:
    - GetTokenHttpResponseService: a Django HTTP response that returns a JSON web token.

    Raises:
    - GoogleTokenInvalidException: if the Google access token passed is invalid.
    - UserModel.DoesNotExist: if there isn't a user associated with that email.
    - InvalidAuthTypeException: if the user's account has a different authentication type.
    """

    data = {"access_token": request.data.get("token")}
    r = requests.get("https://www.googleapis.com/oauth2/v2/userinfo", params=data)
    data = json.loads(r.text)
    auth_type_google = UserAuthTypeModel.objects.get(name="google")

    if "error" in data:
        raise GoogleTokenInvalidException()

    try:
        user = UserModel.objects.get(email=data["email"])
    except UserModel.DoesNotExist:
        user = UserModel.objects.create_user(
            username=data["email"],
            password=make_password(UserManagerService().make_random_password()),
            email=data["email"],
            auth_type_id=auth_type_google,
        )

    if not user.auth_type_id == auth_type_google:
        raise InvalidAuthTypeException()

    return user

def refresh_token_validation_core(request: HttpRequest) -> str:
    """Validates the data in the request for refreshing an access token using the UserRefreshRequestSerializer. Raises
    an exception if validation fails.

    Args:
        request: The HTTP request containing the data to be validated.

    Returns:
        A validated instance of UserRefreshRequestSerializer.

    Raises:
        serializers.ValidationError: If validation fails.
    """
    data = {"refresh": request.COOKIES.get("refresh")}
    serialized_data = UserRefreshRequestSerializer(data=data)
    serialized_data.is_valid(raise_exception=True)
    return serialized_data