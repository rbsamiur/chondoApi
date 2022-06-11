from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import PersonalData
from .serializer import PersonalDataSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPersonalData(request):
    user = request.user
    stored_data = user.personaldata_set.all()
    serializer = PersonalDataSerializers(stored_data, many=True)
    return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPersonalData(request):
    user = request.user
    if PersonalData.objects.filter(user=user).exists():
        return Response("Personal Date already entered. Please use update for change")
    else:
        serializer = PersonalDataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updatePersonalData(request):
    user = request.user
    stored_data = PersonalData.objects.get(user=user)
    print(stored_data)
    serializer = PersonalDataSerializers(instance=stored_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePersonalData(request):
    user = request.user
    stored_data = PersonalData.objects.get(user=user)
    stored_data.delete()
    return Response("Item Deleted Successfully!")
