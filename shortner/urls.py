from django.urls import path

from shortner.views import ShortenUrlView

urlpatterns = [
    path('shorten', ShortenUrlView.as_view()),
    # path('{url_code}',ShortenUrlView.as_view())
]