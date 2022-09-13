from userauth.models import User
from django.db import models


# class Result(models.Model):
#   result_id = models.CharField(max_length = 5 ,primary_key= True)
#   position_1 = models.ForeignKey(Participant,on_delete=models.CASCADE)
#   position_2 = models.ForeignKey(Participant,on_delete=models.CASCADE)
#   position_3 = models.ForeignKey(Participant,on_delete=models.CASCADE) 

class Event(models.Model):
    event_id = models.CharField(max_length = 5 ,primary_key= True)
    event_name = models.CharField(max_length= 50)
    event_description = models.TextField(max_length= 500)
   # result = models.ForeignKey(Result, on_delete= models.CASCADE)     
    prize_1 = models.IntegerField
    prize_2 = models.IntegerField
    prize_3 = models.IntegerField
    event_Type = models.CharField(max_length = 11, choices=[("Individual", "Individual"), ("Team", "Team")])   
    eligible_gender = models.ArrayField(
            models.CharField(max_length=10, blank=True),
            size=2,
        )


class Participant(models.Model):
    participant_id = models.CharField(max_length= 5 ,primary_key=True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    events = models.ManyToManyField(Event)
    remaks = models.CharField(max_length= 200)
    prize_reveal = models.BooleanField(default=False)


class Teams(models.Model):
    team_name = models.CharField(max_length=50)
    team_id = models.IntegerField(max_length= 20)
    events = models.ManyToManyField(Event)
    members = models.ManyToManyField(Participant)


