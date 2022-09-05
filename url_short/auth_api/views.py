from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from auth_api.models import User

from auth_api.serializers import UserSerializer


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
        # 'data': data,
    })