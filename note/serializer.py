from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Note


class NoteSerializers(ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'

