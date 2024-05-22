from django.shortcuts import render
from rest_framework.views import APIView

from shortner.serializer import UrlDBSerializer

# Create your views here.
class ShortenUrlView(APIView):
    def post(self, request):
        serializer = UrlDBSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
