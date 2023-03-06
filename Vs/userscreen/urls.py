from django.urls import path
#from .views import CandidateList
from .import views
from django.urls import path
from .views import CandidateListView

urlpatterns = [
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
]