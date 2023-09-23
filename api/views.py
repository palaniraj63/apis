from django.shortcuts import render
from api import models ,serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    DestroyAPIView
)

# Create your views here.

class StudentListView(ListAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer
