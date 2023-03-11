from .models import CustomUser
from django.db.models import Q

def user_validation(phone,password):
    obj=CustomUser.objects.filter(Q(phone=phone) & Q(password=password)).values()
    print("------------ OBJ ",obj)
    if len(obj)==0:
        return False
    else:
        return True
    


def user_exist(email):
    email_c=CustomUser.objects.filter(Q(email=email) )
    print("email_c ",email_c)
    if len(email_c) == 0 :
        return False
    else:
        return True    