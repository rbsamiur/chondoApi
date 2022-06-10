from django.db import models

# Create your models here.
class Notification(models.Model):
    title=models.CharField(max_length=250)
    body=models.TextField()
    updated_on=models.DateField(null=True)
    expire_on=models.DateField(null=True )
