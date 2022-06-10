from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Notification


class NotificationSerializers(ModelSerializer):
    class Meta:
        model=Notification
        fields=["title","body","updated_on","expire_on"]
