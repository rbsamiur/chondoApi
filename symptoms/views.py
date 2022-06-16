from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import Symptoms
from .serializer import SymptomsSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSymptoms(request):
    user = request.user
    symptom_data = user.symptoms_set.all()
    serializer = SymptomsSerializers(symptom_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getSymptomsbyDate(request):
    user = request.user
    print(request.data['date'])
    date = request.data['date']
    symptom_data = user.symptoms_set.filter(updated_on=date)
    serializer = SymptomsSerializers(symptom_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createSymtom(request):
    user = request.user
    serializer = SymptomsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateSymptom(request, pk):
    symptom_data = Symptoms.objects.get(id=pk)
    serializer = SymptomsSerializers(instance=symptom_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteSymptom(request, pk):
    symptom_data = Symptoms.objects.get(id=pk)
    symptom_data.delete()
    return Response("Item Deleted Successfully!")
