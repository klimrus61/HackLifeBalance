from django.http import HttpRequest, HttpResponse
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..core import (
    google_auth_core,
    refresh_token_validation_core,
)
from ..serializers import (
    UserTokenRequestSerializer,
)
from ..services import GetLogoutHttpResponse, GetTokenHttpResponseService


@extend_schema(
    summary="WORKS: Google auth",
    description="NEED CHECKING: Take google token, create or authorize user, return 'access' and 'refresh' tokens in cookies",
    request=UserTokenRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully authenticated."),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "auth",
    ],
)
@api_view(["POST"])
def google_auth(request: HttpRequest) -> HttpResponse:
    user = google_auth_core(request=request)
    return GetTokenHttpResponseService(user)


@extend_schema(
    summary="WORKS: Refresh access token",
    description="Take user's 'refresh' token from cookies, update 'access' token",
    methods=["POST"],
    request=None,
    responses={
        200: OpenApiResponse(description="Successfully refreshed token."),
        401: OpenApiResponse(description="Error: Unauthorized"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "auth",
    ],
)
@api_view(["POST"])
def refresh_token(request: HttpRequest) -> HttpResponse:
    validated_data = refresh_token_validation_core(request=request)
    return GetTokenHttpResponseService(
        user=request.user, refresh_token=validated_data.data["refresh"]
    )

@extend_schema(
    summary="WORKS: Logout",
    description="Take authenticated user's refresh token, revoke it and blacklist it",
    methods=["POST"],
    request=None,
    responses={
        204: OpenApiResponse(description="Successfully logged out."),
        400: OpenApiResponse(description="Error: Refresh token is required."),
        401: OpenApiResponse(description="Error: Authentication credentials were not provided."),
        422: OpenApiResponse(description="Error: Token is invalid or expired"),
    },
    tags=[
        "auth",
    ],
)
@api_view(["POST"])
def logout(request: HttpRequest) -> HttpResponse:
    validated_data = refresh_token_validation_core(request=request)
    return GetLogoutHttpResponse(token=validated_data.data["refresh"])