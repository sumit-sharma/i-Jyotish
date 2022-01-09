from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import Serializer
from .models import User
from .serializers import (
    AstrologerSerializer,
    UserSerializer,
    TokenSerializer,
    RegisterUserSerializer,
)
from rest_framework import generics, status
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


@swagger_auto_schema(manual_parameters=["offset"])
class AstrologerList(generics.ListAPIView):
    queryset = User.objects.filter(groups__name__in=["astrologer"])
    serializer_class = AstrologerSerializer
    permission_classes = [permissions.IsAuthenticated]


@swagger_auto_schema()
class AstrologerListDetail(generics.RetrieveAPIView):
    queryset = User.objects.filter(groups__name__in=["astrologer"])
    serializer_class = AstrologerSerializer
    permission_classes = [permissions.IsAuthenticated]


@swagger_auto_schema(method="POST")
@api_view(["POST"])
def login_view(request):
    if request.method == "POST":
        try:
            country = request.data.get("country_code")
            mobile = request.data.get("mobile_no")
            # return Response({country_code}, status=status.HTTP_200_OK)

            user = User.objects.get(country_code=country, mobile_no=mobile)
            if user:
                if user.is_active == 1:
                    token, created = Token.objects.get_or_create(user=user)
                    data = {"token": token.key, "user_id": user.id, "created": created}
                    stat = status.HTTP_200_OK
                else:
                    data = {"msg": "user has been blocked by admin", "data": {}}
                    stat = status.HTTP_422_UNPROCESSABLE_ENTITY
        except User.DoesNotExist:
            data = {"msg": "user not found", "data": {}}
            stat = status.HTTP_422_UNPROCESSABLE_ENTITY

        return Response(data, stat)


@swagger_auto_schema(
    method="POST", request_body=RegisterUserSerializer, responses={201: UserSerializer}
)
@api_view(["POST"])
def register_view(request):
    try:
        user_name = request.data.get("country_code") + request.data.get("mobile_no")
        request.data["username"] = user_name
        userData = request.data
        serializer = UserSerializer(data=userData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # TODO: send otp
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        raise e


@api_view(["POST"])
def verify_otp(request):
    if request.method == "POST":
        type = request.data.get("type")
        otp = request.data.get("otp")
        user_identifier = request.data.get("user_identifier")
        # if(type == 'mobile'):
        # filterData =

        user = User.objects.all()


@api_view(["GET"])
def get_user_data(request):
    user = request.user
    return Response(
        {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    )
