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
    path('check/username', CheckUserNameView),
    path('test', test_view),
    path('google/login', GoogleView),
    path('facebook/login', FacebookView),
    path('google/info/update', GoogleUserUpdateView),
    path('facebook/info/update', FacebookUpdateView),

]
