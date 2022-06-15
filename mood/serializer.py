from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Mood


class MoodSerializers(ModelSerializer):
    class Meta:
        model=Mood
        fields='__all__'

