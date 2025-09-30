from rest_framework import generics
from .models import UserInput
from .serializers import UserInputSerializer

class UserInputCreateView(generics.CreateAPIView):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer
