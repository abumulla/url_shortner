from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('<uuid:short_id>', views.redir)
]