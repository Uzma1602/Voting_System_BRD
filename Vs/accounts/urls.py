from .views import RegisterAPI
from django.urls import path
# from .views import LoginAPI

urlpatterns = [
     path('api/register/',RegisterAPI.as_view(),name='register'),
   

]
