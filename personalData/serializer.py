from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import *


class PersonalDataSerializers(ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'


class AbsoluteDataSerializers(ModelSerializer):
    class Meta:
        model = AbsolutePersonalData
        fields = '__all__'
