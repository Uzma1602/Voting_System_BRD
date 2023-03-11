from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser,CustomUserManager


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields="__all__"

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['name','email','password','phone']  

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['password','phone']           

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['state', 'city','pin','area','nearby']          

class ProfileSerializer(serializers.ModelSerializer):
    address=LocationSerializer(many=True,read_only=True)
    class Meta:
        model = CustomUser
        fields =['name', 'phone', 'email', 'age','dob', 'gender', 'voter_Id','address','password']          

