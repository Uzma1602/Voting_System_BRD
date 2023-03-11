from .views import *
from django.urls import path
# from .views import LoginAPI

urlpatterns = [
     path('signup',SignupAPI.as_view()),
     path('login',LoginAPI.as_view()),
     path('address',AddressView.as_view()),
     path('details',ProfileView.as_view()),

]
