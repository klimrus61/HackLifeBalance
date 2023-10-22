from meetings.models import Meeting, MeetingQuestion, MeetingOffer
from rest_framework import serializers


class MeetingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"


class MeetingQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingQuestion
        fields = "__all__"


class MeetingOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingOffer
        fields = "__all__"