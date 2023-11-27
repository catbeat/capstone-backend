from django.shortcuts import render

# Create your views here.
import os
import django
import time
from .models import tb_user_chat
from django.http import HttpResponse
import json
import urllib.parse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView


@csrf_exempt
@api_view(['POST'])
@throttle_classes([UserRateThrottle])
def sql_insert(request):
    if request.method == 'POST':
        headers = request.headers
        print(headers)
        data = request.body.decode('utf-8')
        
        try:
            content_type = headers['Content-Type']
            if (content_type == 'application/x-www-form-urlencoded'):
                data = urllib.parse.parse_qs(data)
                print("data:")

                print(data)

                user_nickname = data['key_nickname'][0]

                chat_body = data['chat_body'][0]
                chat_body = json.loads(chat_body)
                chat_body_data = chat_body.get('data')
                chat_time = chat_body_data[0]['time']
                chat_body_content = chat_body_data[0]['content']

                user = tb_user_chat(user_nickname=user_nickname, chat_body=chat_body_content, chat_time=chat_time, db_time=int(time.time()), delete_status=0)
                user.save()
                #data = json.loads(data)

                returnContent = dict()
                returnContent["data"] = []
                returnContent["errno"] = 0
                returnContent["errmsg"] = "Success"
                return Response(returnContent)
            elif (content_type == 'application/json'):
                print("jsondata:")
                print(data)
                data = json.loads(data)
                user_nickname = data['key_nickname']
                chat_time = data['chat_body']['data'][0]['time']
                chat_body = data['chat_body']['data'][0]['content']
                print('decode json data:')
                print(user_nickname)
                print(chat_time)
                print(chat_body)
                user = tb_user_chat(user_nickname=user_nickname, chat_body=chat_body, chat_time=chat_time, db_time=int(time.time()), delete_status=0)
                user.save()

                returnContent = dict()
                returnContent["data"] = []
                returnContent["errno"] = 0
                returnContent["errmsg"] = "Success"
                return Response(returnContent)
            else:
                print("default:")
                print(data)

            #return Response("get")
        except Exception as e:
            print(e)
            returnContent = dict()
            returnContent["data"] = []
            returnContent["errno"] = 0
            returnContent["errmsg"] = "give me valid json pls"
            return Response(returnContent)
        '''
        content = data.get('data')
        chat_time = content[0]['time']
        user_nickname = content[0]['user_nickname']
        chat_body = content[0]['content']
        user = tb_user_chat(user_nickname=user_nickname, chat_body=chat_body, chat_time=chat_time, db_time=int(time.time()), delete_status=0)
        user.save()

        returnContent = dict()
        returnContent["data"] = []
        returnContent["errno"] = 0
        returnContent["errmsg"] = "Success"
        return Response(returnContent)
        '''
    else:
        return Response("give me post pls")

@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def sql_select(request):
    try: 
        key_nickname = request.GET.get("key_nickname")
        ctime = request.GET.get("time")
        print(key_nickname)
        print(ctime)
        rs = tb_user_chat.objects.filter(chat_time__gt = ctime, user_nickname = key_nickname)
        data = []
        for r in rs:
            d = dict()
            d["time"] = r.chat_time
            d["content"] = r.chat_body
            data.append(d)
			
        returnContent = dict()
        returnContent["data"] = data
        returnContent["errno"] = 0
        returnContent["errmsg"] = "Success"
        return Response(returnContent)
    except Exception as e:
        print(e)
        returnContent = dict()
        returnContent["data"] = []
        returnContent["errno"] = 0
        returnContent["errmsg"] = "give me valid request"
        return Response(returnContent)
