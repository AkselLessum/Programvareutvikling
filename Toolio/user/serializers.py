from rest_framework import serializers

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
  first_name = serializers.CharField(source="first_name")
  last_name = serializers.CharField(source="last_name")
  username = serializers.CharField(source="username")
  phone_number = serializers.IntegerField(source="phone_number")
  email = serializers.CharField(source="email")
  password = serializers.CharField(source="password")
  
  class Meta:
    model = CustomUser
    fields=['first_name', 'last_name', 'username', 'phone_number', 'email', 'password']