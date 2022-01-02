from .models import User
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
        

class AstrologerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'email_verified_at', 'country_code', 'mobile_no', 'phone_verified_at')



class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    # def validate(self, attrs):
    #     username = attrs.get('username')
    #     password = attrs.get('password')

    #     if username and password:
    #         user = authenticate(request=self.context.get('request'),
    #                             username=username, password=password)

    #         # The authenticate call simply returns None for is_active=False
    #         # users. (Assuming the default ModelBackend authentication
    #         # backend.)
    #         if not user:
    #             msg = _('Unable to log in with provided credentials.')
    #             raise serializers.ValidationError(msg, code='authorization')
    #     else:
    #         msg = _('Must include "username" and "password".')
    #         raise serializers.ValidationError(msg, code='authorization')

    #     attrs['user'] = user
    #     return attrs
        
        