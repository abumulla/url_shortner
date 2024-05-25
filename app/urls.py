from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('feedback', views.feedback),
    path('<str:short_id>', views.redir)
]