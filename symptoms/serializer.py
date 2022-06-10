from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Symptomps


class SymptompsSerializers(ModelSerializer):
    class Meta:
        model=Symptomps
        fields='__all__'

