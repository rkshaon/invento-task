from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import datetime
import pyshorteners as sh


# more about pyshorteners 1.0.1
# https://pyshorteners.readthedocs.io/en/latest/


@api_view(['POST'])
def create_short_url(request):
    if 'url' not in request.data:
        return Response({
            'status': False,
            'message': 'URL required to create short URL!'
        }, status=status.HTTP_400_BAD_REQUEST)

    epoch_time = datetime.datetime(1900, 1, 1)
    current_time = datetime.datetime.now()
    execution_time = (current_time - epoch_time).total_seconds()

    if 'expiry' in request.data:
        duration = int(request.data['expiry'])
    else:
        duration = 3600
    # print(type(execution_time))
    # duration = 3600

    url = request.data['url']
    url = url + '?exe=' + str(duration) + '&exp=' + str(execution_time)
    s = sh.Shortener()
    short_url = s.tinyurl.short(url)

    data = {
        'short_url': short_url,
        'url': url,
    }

    return Response({
        'status': True,
        'data': data,
    })


@api_view(['POST'])
def retrive_short_url(request):
    if 'short_url' not in request.data:
        return Response({
            'status': False,
            'message': 'Short URL is require to retrive URL!'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    

    # print('execution-time: ', execution_time)

    s = sh.Shortener()
    url = s.tinyurl.expand(request.data['short_url'])
    
    epoch_time = datetime.datetime(1900, 1, 1)
    current_time = datetime.datetime.now()
    execution_time = (current_time - epoch_time).total_seconds()

    url_split = url.split('?')[1].split('&')
    # print('url-split: ', url_split)
    # url_exeution_tim
    # url_execution_time = url_split['exp']
    url_execution_time = None
    url_duration = None

    for u in url_split:
        # print(u)
        if 'exp' in u:
            # print(u)
            url_execution_time = float(u.split('=')[1])
        
        if 'exe' in u:
            url_duration = float(u.split('=')[1])
    
    # print(url_execution_time)
    # print(url_duration)
    actual_duration = execution_time - url_execution_time
    print(actual_duration)
    # epoch_time = datetime.datetime(1900, 1, 1)
    # current_time = datetime.datetime.now()
    # if execution_time -

    if actual_duration > url_duration:
        return Response({
            'status': True,
            'message': 'Link expired!'
        }, status=status.HTTP_410_GONE)
    
    data = {
        'url': url,
        'short_url': request.data['short_url'],
    }

    return Response({
        'status': True,
        'data': data,
    })