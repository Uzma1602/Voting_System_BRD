from django.urls import path
from .views import ElectionListView, UserVoteView,UpcomingElectionsList,PastElectionsList,CandidateList
#from .views import CandidateListView
from . import views
urlpatterns = [
    path('elections/', ElectionListView.as_view(), name='election-list'),
    path('votes/', UserVoteView.as_view(), name='user-vote'),
    path('upcomingelection/', UpcomingElectionsList.as_view(), name='upcoming-election'),
    path('pastelection/', PastElectionsList.as_view(), name='past-election'),
    path('candidates/<str:election_type_id>/', CandidateList.as_view(), name='CandidateList'),
]
