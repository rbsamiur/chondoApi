from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Symptoms


class SymptomsSerializers(ModelSerializer):
    class Meta:
        model=Symptoms
        fields='__all__'

