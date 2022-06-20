from django.contrib import admin
from django.urls import path, include
from .views import EventAPIView, LocationAPIView, MapAPIView
app_name = 'mainapp-api'
urlpatterns = [
    path('', EventAPIView.as_view()),
    path('locs/', LocationAPIView.as_view()),
    path('maps/', MapAPIView.as_view()),
]
