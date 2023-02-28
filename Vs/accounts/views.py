from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from rest_framework import status
from django.db import models
from .service import user_validation
from .serializers import CustomUserSerializer


# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer,CustomUserSerializer
from .models import CustomUser
from rest_framework.views import APIView

class SignupAPI(APIView):
    def post(self,request,*args,**kwargs):
        serializer=CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"message":"Data saved succesfully"})
    

class LoginAPI(APIView):
    def post(self,request):
        phone=request.data.get('phone')
        password=request.data.get('password')
        flag=user_validation(phone,password)
        if flag==True:
            return Response({"status":200,"error":False,"message":"logged in successfully"})
        else:
            return Response({"status":400,"error":False,"message":"Invalid credentials"})


        

       




