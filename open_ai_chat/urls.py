from django.urls import path

from . import views

urlpatterns = [
    path("", views.chatBot, name="index"),
]