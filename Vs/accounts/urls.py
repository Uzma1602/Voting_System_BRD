from .views import RegisterAPI
from django.urls import path
# from .views import LoginAPI

urlpatterns = [
     path('api/register/',RegisterAPI.as_view(),name='register'),
    #  path('api/login/',LoginAPI.as_view(),name='login'),
    #  path('api/logout/',RegisterAPI.as_view(),name='register'),

]
