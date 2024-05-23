from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UrlDB
from .serializer import UrlDBSerializer
import uuid

class ShortenUrlView(APIView):
    def post(self, request):
        serializer = UrlDBSerializer(data=request.data)
        
        if serializer.is_valid():
            short_id = uuid.uuid4()
            serializer.save(short_id=short_id)
            return Response({"short_id": short_id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    