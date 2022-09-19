from dataclasses import field
from .models import Event
from .models import Submission
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name","subname","rules","judging_criteria","prize_1","prize_2","prize_3","eligible_gender","deadline"]

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["file","event"]