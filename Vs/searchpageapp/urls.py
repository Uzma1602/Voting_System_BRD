from django.urls import path
from .views import ElectionListaccloc
from . import views

urlpatterns = [
    path('electionListAccloc/', ElectionListaccloc.as_view(), name='electionlist-accloc'),
    
]
