from rest_framework import serializers
from .models import ElectionList, UserVote,ElectionType,Candidate

#election list serializer
class ElectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionList
        fields = '__all__'

#user vote serializer
class UserVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVote
        fields = '__all__'
 
#candidate serializer
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
   
class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionType
        fields = '__all__'