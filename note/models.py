from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=250)
    body=models.TextField()
    updated_on=models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
