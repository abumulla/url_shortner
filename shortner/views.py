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
            flag = True
            short_id = ""
            while flag:
                short = uuid.uuid4()
                short_id = str(short).replace('-','')[:6]
                print(short_id)
                try:
                    UrlDB.objects.get(short_id = short_id)
                except:
                    flag = False
            # print(short_id)
            serializer.save(short_id=short_id)
            return Response({"short_id": short_id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    