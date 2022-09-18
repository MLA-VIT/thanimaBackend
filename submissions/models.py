from userauth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField 


# class Result(models.Model):
#   result_id = models.CharField(max_length = 5 ,primary_key= True)
#   position_1 = models.ForeignKey(Participant,on_delete=models.CASCADE)
#   position_2 = models.ForeignKey(Participant,on_delete=models.CASCADE)
#   position_3 = models.ForeignKey(Participant,on_delete=models.CASCADE) 

class Event(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    subname = models.CharField(max_length=100)
    description = models.TextField()
    rules = models.TextField()
    judging_criteria = models.TextField()
   # result = models.ForeignKey(Result, on_delete= models.CASCADE)     
    prize_1 = models.IntegerField()
    prize_2 = models.IntegerField()
    prize_3 = models.IntegerField()
    type = models.CharField(max_length = 11, choices=[("Individual", "Individual"), ("Team", "Team")])
    eligible_gender = ArrayField(
            models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")]),
            size=2
        )


class Participant(models.Model):
    participant_id = models.CharField(max_length= 5 ,primary_key=True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    events = models.ManyToManyField(Event)
    remarks = models.CharField(max_length= 200)
    prize_reveal = models.BooleanField(default=False)

class Teams(models.Model):
    team_id = models.CharField(max_length=5 ,primary_key=True)
    team_name = models.CharField(max_length=50)
    events = models.ManyToManyField(Event)
    members = models.ManyToManyField(Participant)