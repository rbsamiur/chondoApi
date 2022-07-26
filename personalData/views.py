from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import *
from .serializer import *
import datetime


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPersonalData(request):
    user = request.user
    stored_data = user.personaldata_set.all()
    serializer = PersonalDataSerializers(stored_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getPersonalDatabyDate(request):
    user = request.user
    print(request.data['date'])
    date = request.data['date']
    stored_data = user.personaldata_set.filter(updated_on=date)
    serializer = PersonalDataSerializers(stored_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPersonalData(request):
    user = request.user
    if PersonalData.objects.filter(user=user).exists():
        return Response({'msg': "Personal Data already entered. Please use update for change"})
    else:
        serializer = PersonalDataSerializers(data=request.data)
        user_instance = User.objects.get(id=user.id)
        user_instance.last_login = datetime.datetime.now()
        user_instance.save()
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
    return Response({'msg': "Item Deleted Successfully!"})


@permission_classes([IsAuthenticated])
def getAbsoulteData(request):
    user = request.user
    stored_data = user.absolutepersonaldata_set.all()
    serializer = AbsoluteDataSerializers(stored_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAbsoluteData(request):
    user = request.user
    if AbsolutePersonalData.objects.filter(user=user).exists():
        return Response({'msg': "Absolute Personal Data already entered. Please use update for change"})
    else:
        serializer = AbsoluteDataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateAbsoluteData(request):
    user = request.user
    stored_data = AbsolutePersonalData.objects.get(user=user)
    print(stored_data)
    serializer = AbsolutePersonalData(instance=stored_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
