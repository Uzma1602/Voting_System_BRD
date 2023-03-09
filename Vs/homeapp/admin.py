from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ElectionType)
admin.site.register(Candidate)
admin.site.register(ElectionList)
admin.site.register(UserVote)
