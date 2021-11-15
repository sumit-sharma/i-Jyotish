from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView


# Create your views here.


class UserViewSet(ListAPIView):
    """
    API endpoint that list users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


