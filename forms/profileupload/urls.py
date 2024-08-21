from django.urls import path
from .views import CreateProfileView

urlpatterns = [
    path('upload/',CreateProfileView.as_view()),
]
