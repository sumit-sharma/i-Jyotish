from django.shortcuts import render
from rest_framework import generics

from categories.models import Category
from .serializers import CategorySerializer


# Create your views here.

class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

