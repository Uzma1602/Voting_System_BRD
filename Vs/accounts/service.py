from .models import CustomUser
from django.db.models import Q

def user_validation(phone,password):
    obj=CustomUser.objects.filter(Q(phone=phone) & Q(password=password))
    if obj is None:
        return False
    else:
        return True