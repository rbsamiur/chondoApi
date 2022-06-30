from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    updated_on = models.DateField(null=True)
    expire_on = models.DateField(null=True)


# Create your models here.
class UserRead(models.Model):
    read = models.BooleanField(max_length=250)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name='user', null=True, blank=True, on_delete=models.CASCADE)
