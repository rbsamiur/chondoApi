from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, UntypedToken
from rest_framework import status
import datetime
from django.contrib.auth.hashers import check_password
from .serializer import RegistrationSerializers
from .serializer import LoginSerializer
from .serializer import AccountSerializer
from .serializer import UserInfoSerializer
from .serializer import GoogleUserUpdateSerializers
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from .models import *
import requests as httpRequest


@api_view(['POST'])
def GoogleView(request):
    payload = {'access_token': request.data.get("token")}  # validate the token
    r = httpRequest.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
    data = json.loads(r.text)

    if 'error' in data:
        content = {'message': 'wrong google token / this google token is already expired.'}
        return Response(content)

    # create user if not exist
    response = {}
    try:
        user = User.objects.get(email=data['email'])
        response['username'] = user.username
        response['last_login'] = user.last_login
        response['new_user'] = False
        response['name'] = data['name']
    except User.DoesNotExist:

        user = User()
        user.email = data['email']
        # provider random default password
        user.password = make_password(BaseUserManager().make_random_password())
        user.save()
        response['last_login'] = user.last_login
        response['name'] = data['name']
        response['username'] = user.username
        response['new_user'] = True

    token = RefreshToken.for_user(user)  # generate token without username & password

    response['email'] = user.email
    response['access_token'] = str(token.access_token)
    response['refresh_token'] = str(token)
    return Response(response)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GoogleUserUpdateView(request):
    if request.method == 'POST':
        user = request.user

        serializer = GoogleUserUpdateSerializers(data=request.data)

        account_data = {
            'gender': request.data['gender'],
            'phone_no': request.data['phone_no']
        }

        serializer2 = AccountSerializer(data=account_data)

        if serializer.is_valid() and serializer2.is_valid():
            user_instance = serializer.update(user, serializer.validated_data)
            account = serializer2.save(user=user)
            return Response({
                'response': "User Info Updated",
                'email': user_instance.email,
                'username': user_instance.username,
                'gender': account.gender,
                'phone_no': account.phone_no
            })
        else:
            return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserInfoView(request):
    user_instance = User.objects.get(username=request.user)
    serializer = UserInfoSerializer(user_instance)
    account_data = Account.objects.get(user=user_instance)
    serializer2 = AccountSerializer(account_data)
    print(serializer2.data)
    return Response({
        "user_info": serializer.data,
        "account_info": serializer2.data
    })


@api_view(['POST'])
def CheckUserNameView(request):
    response = {}
    print(request)
    try:
        user = User.objects.get(username=request.data[
            "username"
        ])
        response["msg"] = "Username not available"
    except User.DoesNotExist:
        response["msg"] = "Username Valid"

    return Response(response)
@api_view(['POST'])
@permission_classes([])
def tokenObtainPair(request):
    try:

        login_serializer = LoginSerializer(data=request.data)

        if login_serializer.is_valid():
            email = login_serializer.validated_data.get('email')
            password = login_serializer.validated_data.get('password')
            if "@" in email:
                user_instance = User.objects.get(email=email)
            else:
                user_instance = User.objects.get(username=email)
            if check_password(password, user_instance.password):
                refresh = RefreshToken.for_user(user_instance)

                # return Response({
                #
                #     'access_token': str(refresh.access_token),
                #     'refresh_token': str(refresh),
                #     'token_type': str(refresh.payload['token_type']),
                #     'expiry': refresh.payload['exp'],
                #     'user_id': refresh.payload['user_id'],
                #     'user_object': UserInfoSerializer(user_instance).data,
                #
                #

                return Response({

                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                    'token_type': str(refresh.payload['token_type']),
                    'expiry': refresh.payload['exp'],
                    'user_id': refresh.payload['user_id'],
                    'user_object': UserInfoSerializer(user_instance).data,

                })
            else:
                return Response({
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "message": "No active account found with the given credentials",
                    "status_code": 401,
                    "errors": [
                        {
                            "status_code": 401,
                            "message": "No active account found with the given credentials"
                        }
                    ]
                })
        else:
            return Response({
                "code": status.HTTP_401_UNAUTHORIZED,
                "message": "No active account found with the given credentials",
                "status_code": 401,
                "errors": [
                    {
                        "status_code": 401,
                        "message": "Either Email or Password or both not given"
                    }
                ]})
    except Exception as e:
        return Response({
            "code": status.HTTP_401_UNAUTHORIZED,
            "message": str(e),
            "status_code": 401,
            "errors": [
                {
                    "status_code": 401,
                    "message": str(e)
                }
            ]
        })


@api_view(['POST'])
def tokenRefresh(request):
    try:

        refresh = RefreshToken(token=request.data.get('refresh_token'), verify=True)

        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'token_type': str(refresh.payload['token_type']),
            'expiry': refresh.payload['exp'],
            'user_id': refresh.payload['user_id'],
            'user_object': UserInfoSerializer(User.objects.get(id=refresh.payload['user_id'])).data,

        })
    except Exception as e:
        return Response({
            "code": status.HTTP_401_UNAUTHORIZED,
            "message": str(e),
            "status_code": 401,
            "errors": [
                {
                    "status_code": 401,
                    "message": str(e)
                }
            ]
        })


@api_view(['POST'])
def tokenVerify(request):
    try:

        verify = UntypedToken(token=request.data.get('access_token'))

        return Response({
            'access_token': str(verify.token),
            'token_type': str(verify.payload['token_type']),
            'expiry': verify.payload['exp'],
            'user_id': verify.payload['user_id'],
        })
    except Exception as e:
        return Response({
            "code": status.HTTP_401_UNAUTHORIZED,
            "message": str(e),
            "status_code": 401,
            "errors": [
                {
                    "status_code": 401,
                    "message": str(e)
                }
            ]
        })


@api_view(['POST'])
def test_view(request):
    return Response({
        "hello": 'hello'
    }, 200)


# Create your views here.
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        print(request.data['gender'])
        serializer = RegistrationSerializers(data=request.data)

        account_data = {
            'gender': request.data['gender'],
            'phone_no': request.data['phone_no']
        }

        serializer2 = AccountSerializer(data=account_data)

        if serializer.is_valid() and serializer2.is_valid():

            user = serializer.save()
            account = serializer2.save(user=user)
            return Response({
                'response': "successfully registered user",
                'email': user.email,
                'username': user.username,
                'gender': account.gender,
                'phone_no': account.phone_no
            })
        else:
            return Response(serializer.errors)
