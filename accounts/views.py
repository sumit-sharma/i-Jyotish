from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User
from .serializers import AstrologerSerializer, UserSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class UserViewSet(ListAPIView):
    """
    API endpoint that list users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# @swagger_auto_schema(manual_parameters=['offset'])
class AstrologerList(generics.ListAPIView):
    queryset = User.objects.filter(groups__name__in=["astrologer"])
    serializer_class = AstrologerSerializer


class AstrologerListDetail(generics.RetrieveAPIView):
    queryset = User.objects.filter(groups__name__in=["astrologer"])
    serializer_class = AstrologerSerializer
