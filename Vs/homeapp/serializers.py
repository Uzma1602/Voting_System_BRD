from rest_framework import serializers
from .models import ElectionList, UserVote

class ElectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionList
        fields = ('id', 'type', 'start_date', 'end_date', 'region', 'district', 'city')

class UserVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVote
        fields = '__all__'
