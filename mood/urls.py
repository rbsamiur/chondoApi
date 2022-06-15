from django.urls import path
from . import views

urlpatterns=[
    path('moods', views.getMoods),
    path('mood/create/',  views.createMood),
    path('mood/update/<str:pk>', views.updateMood),
    path('mood/delete/<str:pk>', views.deleteMood),
    path('moods/date', views.getMoodsByDate),

]