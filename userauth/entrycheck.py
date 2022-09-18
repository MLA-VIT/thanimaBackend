from rest_framework import generics
from thanimaBackend.helpers import GenericResponse
from django.contrib.auth import get_user_model


class EntryCheckView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        reg_no = request.GET.get('reg_no', None)
        if reg_no is None:
            raise Exception(422,"Please provide Registration Number")
        try:
            user = get_user_model().objects.get(reg_no=reg_no)
            return GenericResponse("",{"entry": True})

        except Exception as e:
            return GenericResponse("",{"entry": False})
class HadFood(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        reg_no = request.GET.get('reg_no', None)
        if reg_no is None:
            raise Exception(422,"Please provide Registration Number")
        try:
            user = get_user_model().objects.get(reg_no=reg_no)
            if user.payment_done == True:
                if user.had_food == False:
                    user.had_food = True
                    user.save()
                    return GenericResponse("Entry Accepted",{"entry": True})
                else:
                    return GenericResponse("Had food",{"entry":False})
                
            else:
                return GenericResponse("Payment not done",{"entry": False})

        except Exception as e:
            return GenericResponse("Not registered in portal",{"entry": False})