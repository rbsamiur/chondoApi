from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import *

# from .views import GoogleView

urlpatterns = [
    path('register', registration_view, name="register"),

    path('token/', tokenObtainPair),
    path('token/refresh/', tokenRefresh),
    path('token/verify/', tokenVerify),
    path('user/info', UserInfoView),
    path('test', test_view),
    path('google/login',GoogleView),
    path('google/info/update',GoogleUserUpdateView),

]
