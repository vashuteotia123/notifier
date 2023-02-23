from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path("get_user_notifications/", GetUserNotifications.as_view()),
]