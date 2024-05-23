from rest_framework import serializers

from shortner.models import UrlDB

class UrlDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlDB
        fields = ['short_id', 'resource_url']