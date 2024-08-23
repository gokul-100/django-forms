from django.urls import path
from .views import CreateProfileView ,Profileview

urlpatterns = [
    path('upload/',CreateProfileView.as_view()),
    path('profileview/',Profileview.as_view()),
]
