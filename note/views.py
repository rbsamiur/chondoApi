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
    user=request.user
    stored_data=user.note_set.all()
    serializer= NoteSerializers(stored_data,many=True)
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
def updateNote(request,pk):
    stored_data = Note.objects.get(id=pk)
    serializer = NoteSerializers(instance=stored_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request,pk):
    stored_data = Note.objects.get(id=pk)
    stored_data.delete()
    return Response("Item Deleted Successfully!")
