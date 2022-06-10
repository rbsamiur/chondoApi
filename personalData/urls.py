from django.urls import path
from . import views

urlpatterns=[
    path('personaldata', views.getPersonalData),
    path('personaldata/create',  views.createPersonalData),
    path('personaldata/update', views.updatePersonalData),
    path('personaldata/delete', views.deletePersonalData),
]