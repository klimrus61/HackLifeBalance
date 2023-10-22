from rest_framework import serializers

from meetings.models import Meeting, MeetingQuestion

class MeetingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"


class MeetingQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingQuestion
        fields = "__all__"