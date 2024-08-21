from django.urls import path
from .import views

urlpatterns = [
    path('',views.feedbackform.as_view()),
    path('thankyou',views.thanku.as_view()),
    path('list',views.feedbacklistView.as_view()),
    
]
