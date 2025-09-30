from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import UserInput
from .serializers import UserInputSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UserInputCreateView(generics.CreateAPIView):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer
    
    def create(self, request, *args, **kwargs):
        print(f"Received data: {request.data}")  # Debug print
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f"Data saved successfully: {serializer.data}")  # Debug print
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(f"Validation errors: {serializer.errors}")  # Debug print
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class UserInputListView(generics.ListAPIView):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer
