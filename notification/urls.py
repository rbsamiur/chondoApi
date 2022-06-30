from django.urls import path
from . import views

urlpatterns = [
    path('notifications', views.getNotifications),
    path('user/notifications', views.getNotifications),
    path('user/notification/toggle/<str:pk>', views.notificationReadToggle),
    path('notification/create/', views.createNotification),
    path('notification/update/<str:pk>', views.updateNotification),
    path('notification/delete/<str:pk>', views.deleteNotification),
]
