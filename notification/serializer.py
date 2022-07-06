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
        fields = ["user", "notification", "read", "id"]


class UserNotificationSerializer(ModelSerializer):
    read = serializers.SerializerMethodField('get_user_read')

    def get_user_read(self, obj):
        try:
            user_id = self.context.get("user")
            print(user_id)
            read = UserRead.objects.get(notification=obj.id, user=user_id).read
            print(read)
            return read
        except UserRead.DoesNotExist:
            return False

    class Meta:
        model = Notification
        fields = ["read", "title", "body", "updated_on", "expire_on", "id"]
