from django.urls import path
from . import views

urlpatterns=[
    path('notifications', views.getNotifications),
    path('notification/create/',  views.createNotification),
    path('notification/update/<str:pk>', views.updateNotification),
    path('notification/delete/<str:pk>', views.deleteNotification),
]