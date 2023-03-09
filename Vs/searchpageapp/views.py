from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
from homeapp.models import ElectionType,Candidate,ElectionList,UserVote
from rest_framework.views import APIView
from rest_framework.response import Response
from homeapp.serializers import ElectionListSerializer

class ElectionListaccloc(APIView):
    def get(self, request):
        selected_location = request.GET.get('location')
        selected_area = request.GET.get('area')
        required_election_list = ElectionList.objects.filter(state=selected_location, city=selected_area)
        serializer = ElectionListSerializer(required_election_list, many=True)
        return Response(serializer.data)
