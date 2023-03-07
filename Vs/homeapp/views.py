from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ElectionList, UserVote, Candidate, ElectionType
from .serializers import ElectionListSerializer, UserVoteSerializer, ElectionTypeSerializer,CandidateSerializer

from django.utils import timezone
from datetime import date

def addTypeToIncomingData(election_list_data):
        for each_ele in election_list_data:
            election_type = ElectionType.objects.get(pk=each_ele['election_type_fk'])
            ele_type_obj = ElectionTypeSerializer(election_type)
            each_ele['election_type']= ele_type_obj.data['type']

class ElectionListView(APIView):
    def get(self, request, format=None):
        election_list = ElectionList.objects.all()
        serializer = ElectionListSerializer(election_list, many=True)
        election_list_data = serializer.data
        
        addTypeToIncomingData(election_list_data)

        return Response(election_list_data)


    
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


class CandidateList(APIView):

    def get(self, request, election_type_id):
        print("ele type id ", election_type_id)
        queryset = Candidate.objects.filter(election_type_fk_id=election_type_id)
        serializer = CandidateSerializer(queryset, many=True)
        data = serializer.data
        addTypeToIncomingData(data)
        return Response(data)