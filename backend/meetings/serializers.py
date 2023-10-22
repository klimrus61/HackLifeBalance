from rest_framework import serializers

from meetings.models import Meeting

class MeetingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"

