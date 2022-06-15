from django.urls import path
from . import views

urlpatterns=[
    path('symptoms', views.getSymptoms),
    path('symptom/create/',  views.createSymtom),
    path('symptom/update/<str:pk>', views.updateSymptom),
    path('symptom/delete/<str:pk>', views.deleteSymptom),
    path('symptoms/date', views.getSymptomsbyDate),
]