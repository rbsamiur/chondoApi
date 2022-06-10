from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import Symptomps
from .serializer import SymptompsSerializers

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSymptoms(request):
    user=request.user
    stored_data=user.symptomps_set.all()
    serializer= SymptompsSerializers(stored_data,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createSymtom(request):
    user = request.user
    serializer = SymptompsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateSymptom(request,pk):
    stored_data = Symptomps.objects.get(id=pk)
    serializer = SymptompsSerializers(instance=stored_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteSymptom(request,pk):
    stored_data = Symptomps.objects.get(id=pk)
    stored_data.delete()
    return Response("Item Deleted Successfully!")
