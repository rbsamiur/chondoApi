from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import *


class PeriodHistorySerializer(ModelSerializer):
    class Meta:
        model = PeriodHistory
        fields = '__all__'
