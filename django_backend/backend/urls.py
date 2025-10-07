from django.urls import path
from .views import (
    UserInputCreateView, 
    UserInputListView, 
    UserInputDetailView,
    UserInputUpdateView,
    UserInputDeleteView
)

urlpatterns = [
    path('submit/', UserInputCreateView.as_view(), name='submit'),
    path('list/', UserInputListView.as_view(), name='list'),
    path('detail/<int:id>/', UserInputDetailView.as_view(), name='detail'),
    path('update/<int:id>/', UserInputUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', UserInputDeleteView.as_view(), name='delete'),
]
