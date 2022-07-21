from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PeriodHistory(models.Model):
    periodStartDay = models.DateField(null=True)
    periodEndDay = models.DateField(null=True)
    cycleEndDay = models.DateField(null=True)
    ovDate = models.DateField(null=True)
    periodLen = models.IntegerField(default=0, null=True)
    cycleLen = models.IntegerField(default=0, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
