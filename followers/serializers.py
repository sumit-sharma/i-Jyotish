from rest_framework import serializers
from .models import UserFollowing

class FollowingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserFollowing
        fields = ("id", "user", "following_user", "created_at")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created_at")
        

        

