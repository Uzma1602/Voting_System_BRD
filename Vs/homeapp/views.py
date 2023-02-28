from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ElectionList, UserVote
from .serializers import ElectionListSerializer, UserVoteSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import date

class ElectionListView(generics.ListCreateAPIView):
    queryset = ElectionList.objects.all()
    serializer_class = ElectionListSerializer

class UserVoteView(generics.ListCreateAPIView):
    queryset = UserVote.objects.all()
    serializer_class = UserVoteSerializer

#for filter out the upcoming and past elections

# Api for upcomg elections
class UpcomingElectionsList(generics.ListAPIView):
    serializer_class = ElectionListSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = date.today()
        queryset = ElectionList.objects.filter(start_date__gte=today).order_by('start_date')
        return queryset
    

#Api for past election
class PastElectionsList(generics.ListAPIView):
    serializer_class = ElectionListSerializer

    def get_queryset(self):
        queryset = ElectionList.objects.filter(end_date__lt=timezone.now())
        return queryset