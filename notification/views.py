from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import Notification
from .serializer import NotificationSerializers
from authentication.decorator import permission_required


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotifications(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializers(notifications, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_required('add_notification')
@permission_classes([IsAuthenticated])
def createNotification(request):
    serializer = NotificationSerializers(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        print(serializer)
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_required('change_notification')
@permission_classes([IsAuthenticated])
def updateNotification(request, pk):
    notification = Notification.objects.get(id=pk)
    serializer = NotificationSerializers(instance=notification, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_required('delete_notification')
@permission_classes([IsAuthenticated])
def deleteNotification(request, pk):
    notification = Notification.objects.get(id=pk)
    notification.delete()
    return Response("Item Deleted Successfully!")
