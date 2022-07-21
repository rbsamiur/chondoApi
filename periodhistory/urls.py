from django.urls import path
from . import views

urlpatterns = [
    path('histories', views.get_history),
    path('history/create/', views.create_history),
    #
    # path('mood/delete/<str:pk>', views.deleteMood),
    # path('moods/date', views.getMoodsByDate),

]
