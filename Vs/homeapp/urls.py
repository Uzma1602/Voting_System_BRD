from django.urls import path
from .views import ElectionListView, UserVoteView,UpcomingElectionsList,PastElectionsList
from . import views
urlpatterns = [
    path('elections/', ElectionListView.as_view(), name='election-list'),
    path('votes/', UserVoteView.as_view(), name='user-vote'),
    path('upcomingelection/', UpcomingElectionsList.as_view(), name='upcoming-election'),
    path('pastelection/', PastElectionsList.as_view(), name='past-election'),
   # path('votes', views.UserVote, name='user-vote'),
]
