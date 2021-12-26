from django.shortcuts import render
from rest_framework import generics

from .models import UserFollowing
from .serializers import FollowingSerializer, FollowersSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

# @swagger_auto_schema(manual_parameters=['offset'])
class CreateFollower(generics.CreateAPIView):
    # UserFollowing.objects.create(user_id=user.id, following_user_id=follow.id)
    serializer_class = FollowingSerializer
    queryset = UserFollowing.objects.all()


# class CategoryDetail(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer