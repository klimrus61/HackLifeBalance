import datetime
import time

from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class UserTokenRequestSerializer(serializers.Serializer):
    token = serializers.CharField()


class UserRefreshRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, value):
        try:
            token = RefreshToken(value["refresh"])
            current_time = time.mktime(datetime.datetime.now().timetuple())
            if token["exp"] < int(current_time):
                raise serializers.ValidationError("Refresh token has expired")
        except TokenError:
            raise serializers.ValidationError("Invalid or expired refresh token")

        return value