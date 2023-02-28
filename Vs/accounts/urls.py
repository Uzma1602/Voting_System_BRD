from .views import SignupAPI,LoginAPI
from django.urls import path
# from .views import LoginAPI

urlpatterns = [
     path('signup/',SignupAPI.as_view()),
     path('login/',LoginAPI.as_view()),
   

]
