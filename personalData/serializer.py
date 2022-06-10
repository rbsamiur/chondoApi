from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import PersonalData


class PersonalDataSerializers(ModelSerializer):
    class Meta:
        model=PersonalData
        fields='__all__'
