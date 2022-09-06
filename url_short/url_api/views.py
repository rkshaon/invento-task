from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import pyshorteners as sh


@api_view(['POST'])
def create_short_url(request):
    if 'url' not in request.data:
        return Response({
            'status': False,
            'message': 'URL required to create short URL!'
        }, status=status.HTTP_400_BAD_REQUEST)

    s = sh.Shortener()
    short_url = s.tinyurl.short(request.data['url'])

    data = {
        'short_url': short_url,
        'url': request.data['url']
    }

    return Response({
        'status': True,
        'data': data,
    })