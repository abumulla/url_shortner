from django.urls import path

from shortner.views import FeedbackView, ShortenUrlView

urlpatterns = [
    path('shorten', ShortenUrlView.as_view()),
    path('feedback', FeedbackView.as_view())
]