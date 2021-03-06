from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Mood(models.Model):
    moods = models.JSONField(default=dict, blank=True)
    updated_on = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
