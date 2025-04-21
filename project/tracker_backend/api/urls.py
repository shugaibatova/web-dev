from django.urls import path
from .views import MoodAPIView

urlpatterns = [
    path('moods/', MoodAPIView.as_view(), name='moods'),
]
