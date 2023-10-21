from rest_framework import serializers

from .models import Meeting

class MeetingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"

