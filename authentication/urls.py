from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import tokenObtainPair
from .views import tokenVerify
from .views import tokenRefresh
from .views import registration_view
# from .views import GoogleView

urlpatterns=[
    path('register',registration_view, name="register"),

    path('token/', tokenObtainPair),
    path('token/refresh/', tokenRefresh),
    path('token/verify/', tokenVerify),
    # path('google/login',GoogleView),

]