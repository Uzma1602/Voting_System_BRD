from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from rest_framework import status
from django.db import models
from .service import user_validation
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import CustomUserSerializer,SignupSerializer,ProfileSerializer,LocationSerializer,LoginSerializer
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .service import user_validation,user_exist


class SignupAPI(APIView):
    def post(self,request):
        body = request.data
        flag= user_exist(body['email'])
        if flag == True:
            return Response({"status":400,"message":"User already exist"})
        else:
            serializer = SignupSerializer(data=body)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":200,"message":"Data saved succesfully"})
            else: 
                 return Response({"status":400,"message":"Data Invalid"})
    
class LoginAPI(APIView):
    def post(self,request):
        phone=request.data.get('phone')
        password=request.data.get('password')
        flag=user_validation(phone,password)
        if flag==True:
            return Response(True)
        else:
            return Response(False)

class AddressView(APIView): 
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        body=request.data
        serializer = LocationSerializer(data=body)
        serializer.is_valid(raise_exception=True)   
        CustomUser.state = serializer.validated_data.get('state')
        CustomUser.city = serializer.validated_data.get('city')
        CustomUser.pin = serializer.validated_data.get('pincode')
        CustomUser.area = serializer.validated_data.get('area')
        CustomUser.nearby = serializer.validated_data.get('nearby')
        serializer.save()
        return Response({"success": True, "message": "Received location"}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self,request):
        body=request.data
        print(body)
        serializer =ProfileSerializer(data=body)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            #return Response({"success": True, "message": "Your account has been successfully activated!!"})

            user = CustomUser.objects.get(email=body['email'])
            print("user -> ", user)
           
            refresh = RefreshToken.for_user(user)
            print(refresh)

            return Response({"success": True, "message": "Your account has been successfully activated!!",
                                 'refresh': str(refresh),
                                 'access': str(refresh.access_token)},
                                status=status.HTTP_200_OK)
           
        else:
            return Response({"status":400,"message":"Data Invalid"})
    def get(self,request):
        address=CustomUser.objects.all()
        serializer=ProfileSerializer(address,many=True)
        return Response(serializer.data)