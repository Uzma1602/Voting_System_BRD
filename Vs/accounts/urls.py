from .views import *
from django.urls import path
# from .views import LoginAPI

urlpatterns = [
     path('api/register/',RegisterAPI.as_view(),name='register'),
     path('signup/',SignupAPI.as_view()),
     path('login/',LoginAPI.as_view()),

]
