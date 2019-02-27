from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Project import serializers
from Project.models import Project
from Project.serializers import ProjectSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# class IssueView(APIView):

@api_view(["GET"])
def get(requests):#to get all objects of project
    project_objs= Project.objects.all()
    serialiser= ProjectSerializer(project_objs,many=True)
    return Response(status=201,data=serialiser.data)

@api_view(["GET"])
def get_project_by_id(requests,p_id):
    # project_id=requests.GET.get('p_id')
    project_objects=Project().get_project_details(p_id)
    serializer=ProjectSerializer(project_objects)
    return Response(status=201,data=serializer.data)

