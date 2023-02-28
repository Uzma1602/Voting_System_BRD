from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from rest_framework import status


# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer,CustomUserSerializer
from .models import CustomUser

class RegisterAPI(generics.GenericAPIView):
    serializer_class=CustomUserSerializer

    print(serializer_class)
    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #return Response(serializer.data)
        refresh = RefreshToken.for_user(serializer)
        return Response({"success": True, "message": "Your account has been successfully activated!!",
                             'refresh': str(refresh),
                             'access': str(refresh.access_token)},
                            status=status.HTTP_200_OK)
        

       




