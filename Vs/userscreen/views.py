from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
from homeapp.models import ElectionType,Candidate,ElectionList,UserVote
# Create your models here.
from rest_framework.views import APIView
from rest_framework.response import Response

#from .models import Candidate

class CandidateListView(APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        data = []
        for candidate in candidates:
            data.append({
                'id': candidate.can_id,
                'name': candidate.name,
                'des': candidate.des,
                'logo': request.build_absolute_uri(candidate.logo.url),
            })
        return Response(data)
