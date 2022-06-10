from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PersonalData(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    period_length=models.IntegerField()
    cycle_length=models.IntegerField()
    last_date_of_period=models.DateField(null=True)