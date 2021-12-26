from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import User
from .serializers import AstrologerSerializer, UserSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
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

@api_view (["GET"])
def login_view(request):
    user = User.objects.get(email="josh@yopmail.com")
    token = Token.objects.get_or_create(user=user)
    # print(token[0])
    # data = {'token': token[0]}
    return Response(data, status=201)


def get_user_data(request):
    return HttpResponse()
