from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ElectionList, UserVote, Candidate
from .serializers import ElectionListSerializer, UserVoteSerializer

from django.utils import timezone
from datetime import date
class ElectionListView(APIView):
    serializer_class = ElectionListSerializer

    def get(self, request, format=None):
        election_list = ElectionList.objects.all()
        serializer = self.serializer_class(election_list, many=True)
        return Response(serializer.data)
#after voting api 
class UserVoteView(APIView):
    serializer_class = UserVoteSerializer

    def get(self, request, format=None):
        user_votes = UserVote.objects.all()
        serializer = self.serializer_class(user_votes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


#api for filterout the upcoming and past election
#for upcomg election
class UpcomingElectionsList(APIView):
    serializer_class = ElectionListSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        today = date.today()
        queryset = ElectionList.objects.filter(start_date__gte=today).order_by('start_date')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
#for past elction
class PastElectionsList(APIView):
    serializer_class = ElectionListSerializer

    def get(self, request, format=None):
        queryset = ElectionList.objects.filter(end_date__lt=timezone.now())
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

#to show candidates list and logo

#from .models import Candidate

# class CandidateListView(APIView):
#     def get(self, request):
#         candidates = Candidate.objects.all()
#         data = []
#         for candidate in candidates:
#             data.append({
#                 'id': candidate.can_id,
#                 'name': candidate.name,
#                 'des': candidate.des,
#                 'logo': request.build_absolute_uri(candidate.logo.url),
#             })
#         return Response(data)
