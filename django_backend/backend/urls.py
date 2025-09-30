from django.urls import path
from .views import UserInputCreateView, UserInputListView

urlpatterns = [
    path('submit/', UserInputCreateView.as_view(), name='submit'),
    path('list/', UserInputListView.as_view(), name='list'),
]
