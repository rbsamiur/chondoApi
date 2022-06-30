from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class NotificationSerializers(ModelSerializer):
    class Meta:
        model = Notification
        fields = ["title", "body", "updated_on", "expire_on"]


class UserReadSerializers(ModelSerializer):
    class Meta:
        model = UserRead
        fields = ["user","notification","read","id"]


class UserNotificationSerializer(ModelSerializer):
    read = serializers.SerializerMethodField('get_user_read')

    def get_user_read(self, obj):
        try:
            read = UserRead.objects.get(notification=obj.id).read
            return read
        except UserRead.DoesNotExist:
            return False

    class Meta:
        model = Notification
        fields = ["read", "title", "body", "updated_on", "expire_on", "id"]
