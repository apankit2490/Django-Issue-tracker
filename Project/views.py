from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Project.models import Project
from Project.serializers import ProjectSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# class IssueView(APIView):

@api_view(["GET"])
def get(requests):
    project_objs= Project.objects.all()
    serialiser= ProjectSerializer(project_objs,many=True)
    return Response(status=201,data=serialiser.data)
