from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import status

  
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model=User
        fields=['id', 'email', 'password', 'password2', 'first_name', 'last_name', 'branch', 'country', 'state', 'phone_number']

    def validate(self, attrs):
        password= attrs.get('password', '')
        password2= attrs.get('password', '')
        if password != password2:
            raise serializers.ValidationError('password do not match')
        return super().validate(attrs)
    

    def create(self, validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            branch=validated_data['branch'],
            country=validated_data['country'],
            state=validated_data['state'],
            phone_number=validated_data['phone_number'],
        )
        return user


class GetUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id', 'email', 'first_name', 'last_name', 'branch', 'country', 'state', 'phone_number']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)
    id = serializers.CharField(max_length=15, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'access_token', 'refresh_token', 'id']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials. Please try again.")
        id = user.id
        email = user.email
        user_token=user.tokens()
        return {
            'email': email,
            'id': id,
            'access_token': str(user_token.get("access")),
            'refresh_token': str(user_token.get("refresh")),

        }
   

class LogoutUserSerializer(serializers.Serializer):
    refresh_token=serializers.CharField()

    default_error_message={
        'bad_token': ('Token is Invalid or has expired')
    }


    def validate(self, attrs):
        self.token=attrs.get('refresh_token')
        return attrs
    
    def save(self, **kwargs):
        try:
            token=RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return self.fail('bad_token')
        
