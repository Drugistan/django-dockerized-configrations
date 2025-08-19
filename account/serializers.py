from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)

        if user_type.lower() == 'admin':
            user.is_superuser = True
            user.is_staff = True
        elif user_type.lower() == 'staff':
            user.is_staff = True

        user.user_type = user_type
        user.save()
        return user



