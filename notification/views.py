from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import *
from .serializer import *
from authentication.decorator import permission_required


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotifications(request):
    notifications = Notification.objects.all()
    serializer = UserNotificationSerializer(notifications, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notificationReadToggle(request, pk):
    try:
        notification = UserRead.objects.get(notification=pk)

        notification.read = not notification.read

        notification.save()
        return Response(UserReadSerializers(notification, context={'request': request}).data)

    except UserRead.DoesNotExist:
        user_read_instance = {}
        user_read_instance["user"] = User.objects.get(username=request.user).id
        user_read_instance["notification"] = pk
        user_read_instance["read"] = True
        serializer = UserReadSerializers(data=user_read_instance)
        if serializer.is_valid():
            serializer.save()
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
