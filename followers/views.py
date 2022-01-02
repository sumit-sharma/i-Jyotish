from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import UserFollowing
from .serializers import FollowingSerializer, FollowersSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
# Create your views here.


@swagger_auto_schema()
@api_view(["POST"])
def create_follower(request):
    user = request.data.get('user_id')
    usr = UserFollowing.objects.create(user_id=user, following_user_id=request.user.id)
    data =  FollowingSerializer(usr).data
    return Response(data, status=status.HTTP_200_OK)


# class CategoryDetail(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer