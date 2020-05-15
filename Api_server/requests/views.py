from django.shortcuts import render

#Api related imports
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from requests.models import ProjectCreateQ
from requests.serializers import RequestSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes

#Api token related imports
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Api conserned views.

@csrf_exempt
@api_view(['GET', 'POST'])
def requestQ(request):
    if request.method == 'POST':
        reqdata = JSONParser().parse(request)
        serilizer= RequestSerializer(data=reqdata)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data, status=201)
        return JsonResponse(serilizer.errors, status=400)



