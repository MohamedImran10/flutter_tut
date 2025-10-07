from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
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

@method_decorator(csrf_exempt, name='dispatch')
class UserInputDetailView(generics.RetrieveAPIView):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer
    lookup_field = 'id'

@method_decorator(csrf_exempt, name='dispatch')
class UserInputUpdateView(generics.UpdateAPIView):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer
    lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        print(f"Updating record {kwargs.get('id')} with data: {request.data}")
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(f"Data updated successfully: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(f"Validation errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class UserInputDeleteView(generics.DestroyAPIView):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        print(f"Deleting record {kwargs.get('id')}")
        instance = self.get_object()
        instance.delete()
        print(f"Record deleted successfully")
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
