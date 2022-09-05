from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import datetime
import jwt

from url_short.utility import auth_user

from auth_api.models import User

from auth_api.serializers import UserSerializer
from auth_api.serializers import UserProfileSerializer


@api_view(['POST'])
def user_registration(request):
    data = request.data

    if 'username' not in data or data['username'] == '' or 'password' not in data or data['password'] == '':
        return Response({
            'status': False,
            'message': 'username and password are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user_serializer = UserSerializer(data=data)

    if user_serializer.is_valid():
        user_serializer.save()
    else:
        return Response({
            'status': False,
            'message': str(user_serializer.errors),
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    return Response({
        'status': True,
        'data': data,
    })


@api_view(['POST'])
def user_login(request):
    data = request.data
    
    if 'credential' not in data or data['credential'] == '' or 'password' not in data or data['password'] == '':
        return Response({
            'status': False,
            'message': 'credential and password are required'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        try:
            user = User.objects.get(username=data['credential'])
        except Exception as e:
            print(e)
            user = User.objects.get(email=data['credential'])
    except User.DoesNotExist:
        return Response({
            'status': False,
            'message': 'user does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(data['password']):
        return Response({
            'status': False,
            'message': 'incorrect password'
        }, status=status.HTTP_401_UNAUTHORIZED)

    payload = {
        'id': user.id,
        'iat': datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response()

    response.set_cookie(key='token', value=token, httponly=True)
    response.data = {
        'status': True,
        'data': {
            'token': token,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'id': user.id,
        },
    }

    return response


@api_view(['POST'])
def user_logout(request):
    response = Response()

    response.delete_cookie('token')

    response.data = {
        'status': True,
        'message': 'logout success'
    }

    return response


@api_view(['GET'])
def user_profile(request):
    user = auth_user(request)

    user_serializer = UserProfileSerializer(user)
    data = user_serializer.data

    return Response({
        'status': True,
        'data': data,
    })