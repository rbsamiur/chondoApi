from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import Note
from .serializer import NoteSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    note_data = user.note_set.all()
    serializer = NoteSerializers(note_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getNotesbyDate(request):
    user = request.user
    print(request.data['date'])
    date=request.data['date']
    note_data = user.note_set.filter(updated_on=date)
    serializer = NoteSerializers(note_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createNote(request):
    user = request.user
    serializer = NoteSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateNote(request, pk):
    note_data = Note.objects.get(id=pk)
    serializer = NoteSerializers(instance=note_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request, pk):
    note_data = Note.objects.get(id=pk)
    note_data.delete()
    return Response("Item Deleted Successfully!")
