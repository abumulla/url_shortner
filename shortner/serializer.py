from rest_framework import serializers

from shortner.models import Feedback, UrlDB

class UrlDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlDB
        fields = ['short_id', 'resource_url']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['name', 'email','feedback']