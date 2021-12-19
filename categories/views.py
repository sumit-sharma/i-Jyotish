from django.shortcuts import render
from rest_framework import generics

from categories.models import Category
from .serializers import CategorySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

@swagger_auto_schema(manual_parameters=['offset'])
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer