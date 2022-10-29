from django.urls import path, include
from .views import get_all_crimes_api, get_crimes_within_area_api

urlpatterns = [
    path('getallcrimes', get_all_crimes_api, name='getallcrimes'),
    path('allcrimesinarea', get_crimes_within_area_api, name='getallcrimesinarea'),
]