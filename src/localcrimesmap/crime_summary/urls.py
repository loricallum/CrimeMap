from django.urls import path, include
from crime_summary.crimesummaryview import CrimeSummaryView

urlpatterns = [
    path('',  CrimeSummaryView.as_view(), name='crimesummary'),
]