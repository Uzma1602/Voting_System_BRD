from rest_framework import serializers
from .models import ElectionList, UserVote,ElectionType,Candidate

class ElectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionList
        fields = ('id', 'type', 'start_date', 'end_date', 'state', 'district', 'city')

class UserVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVote
        fields = '__all__'
