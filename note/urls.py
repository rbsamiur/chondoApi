from django.urls import path
from . import views

urlpatterns=[
    path('notes', views.getNotes),
    path('note/create/',  views.createNote),
    path('note/update/<str:pk>', views.updateNote),
    path('note/delete/<str:pk>', views.deleteNote),
]