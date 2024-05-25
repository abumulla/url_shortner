from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UrlDB
from .serializer import FeedbackSerializer, UrlDBSerializer
import uuid
from django.core.mail import send_mail

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
            return Response({
                "short_id": short_id
                }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FeedbackView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            try:
                name = serializer.validated_data['name']
                email = serializer.validated_data['email'] 
                feedback = serializer.validated_data['feedback']
                send_mail(
                    "Feedback from Users: URL shortner",
                    f"Name: {name}\n\nEmail: {email}\n\n\nFeedback:\n {feedback}\n\n\nRegards,\n{name}",
                    "mulla.devops1@gmail.com",
                    ["mulla2000.abubakar@gmail.com"],
                    fail_silently=False
                )
                serializer.save()
                return Response({
                    "message": "Thank you for your feedback!"
                    }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "message": "Failed to submit feedback. Please try again."+str(e)
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print("invalid data")