from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#imports for the auth application
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from authenticate.models import Usersreg
from authenticate.serializers import AuthSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes

#Api token related imports
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

#view to register the user
@csrf_exempt
@api_view(['POST'])
def auth_register(request):
    reqdata = JSONParser().parse(request)
    serilizer= AuthSerializer(data=reqdata)
    if serilizer.is_valid():
        serilizer.save()
        user=User.objects.create_user(username=reqdata['User_name'],email=reqdata['user_email'],password=reqdata['passw'])
        user.save()

        return JsonResponse({'result':'user_registered'},status=201)
    return JsonResponse(serilizer.errors, status=400)

#view to generate the token if user is registred
@csrf_exempt
@api_view(['POST'])
def auth_login(request):
    user_data=JSONParser().parse(request)
    try:
        username=user_data['User_name']
        userpass=user_data['passw']
        user_instance=Usersreg.objects.get(User_name=username)
    except:
        return JsonResponse(user_data,status=500)
    if user_instance:
        if user_instance.passw == userpass:
            user_token= Token.objects.create(user=User.objects.get(username=username)).key
            return JsonResponse({'result':'Welcome','token':user_token},status=201)
        else:
            return JsonResponse({'result':'wrong credentials'},status=201)
    return JsonResponse({'result':'invalid request'},status=400)

#view that is used for fetching an existing token if it's present 
@csrf_exempt
@api_view(['POST'])
def gettoken(request):
    user_data=JSONParser().parse(request)

    try:
        user_instance=Token.objects.get(user=User.objects.get(username=user_data['User_name'])).key
        return JsonResponse({'result':'token found','token':user_instance},status=201)
        
    except:
        return JsonResponse({'result':'token dont exist1'},status=400)
    return JsonResponse({'result':'invalid request'},status=400)


#view that returns the full list of usernames of the existing users
@csrf_exempt
@api_view(['POST'])
def getallusers(request):
    
    try:

        data=get_user_model().objects.all()
        names=[]
        for i in data:
            names.append(i.get_username())


        return JsonResponse({'users':names},status=201)

    except:
        return JsonResponse({'result':'invalid request'},status=400)


#view to delete an user with verifiation of the credentials
@csrf_exempt
@api_view(['POST'])
def deletuser(request):
    user_data=JSONParser().parse(request)
    try:
        username=user_data['User_name']
        userpass=user_data['passw']
        user_instance=Usersreg.objects.get(User_name=username)
    except:
        return JsonResponse(user_data,status=500)
    if user_instance:
        if user_instance.passw == userpass:
            Token.objects.get(user=User.objects.get(username=username)).delete()
            return JsonResponse({'result':'Token removed'},status=201)
        else:
            return JsonResponse({'result':'wrong credentials'},status=201)
    return JsonResponse({'result':'invalid request'},status=400)
