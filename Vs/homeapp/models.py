from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

class ElectionType(models.Model):
    ele_id = models.AutoField(primary_key=True)
    TYPE_CHOICES = [
        ('Loksabha', 'Loksabha'),
        ('Assembly', 'Assembly'),
        ('Panchayat', 'Panchayat'),
    ]
    type = models.CharField(choices=TYPE_CHOICES, max_length=255)

class Candidate(models.Model):
    can_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    des = models.TextField()
    logo = models.ImageField(upload_to='candidate_logos/')
    election_type_fk = models.ForeignKey(ElectionType, on_delete=models.CASCADE, default=2)

#create the election list of election type
class ElectionList(models.Model):
    start_date = models.DateField()
    state = models.CharField(max_length=255,  default="Karnataka")
    end_date = models.DateField()
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #election_pic = models.ImageField(upload_to='election_image/')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_id',  default=1)
    election_type_fk = models.ForeignKey(ElectionType, on_delete=models.CASCADE, default=2)


class UserVote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    election = models.ForeignKey(ElectionList, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
   # custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='voter')

    def __str__(self):
        return f"{self.user} voted for {self.candidate} in the {self.election} election"


    def __str__(self):
        return f"{self.type} election in {self.state}"


    def __str__(self):
        return self.name


    def __str__(self):
        return self.type
