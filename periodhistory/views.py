from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import *
from .serializer import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history(request):
    user = request.user
    mood_data = user.periodhistory_set.all()
    serializer = PeriodHistorySerializer(mood_data, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def getMoodsByDate(request):
#     user = request.user
#     date = request.data['date']
#     print(date)
#     mood_data = user.mood_set.filter(updated_on=date)
#     print(mood_data)
#     serializer = MoodSerializers(mood_data, many=True)
#     print (serializer)
#     return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_history(request):
    user = request.user
    print(request.data)
    serializer = PeriodHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def updateMood(request, pk):
#     mood_data = Mood.objects.get(id=pk)
#     serializer = MoodSerializers(instance=mood_data, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def deleteMood(request, pk):
#     mood_data = Mood.objects.get(id=pk)
#     mood_data.delete()
#     return Response("Item Deleted Successfully!")
