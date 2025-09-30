from django.urls import path
from .views import UserInputCreateView

urlpatterns = [
    path('submit/', UserInputCreateView.as_view(), name='submit'),
]
