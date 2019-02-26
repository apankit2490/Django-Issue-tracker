from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Issues.models import Issues
from Issues.serializers import IssuesSerializer


@api_view(["POST"])
def create_issue(requests):
    title=requests.data.get('title')
    description=requests.data.get('description')
    p_id=requests.data.get('project_id')
    issue_type=requests.data.get('issue_type')
    summary=requests.data.get('summary')
    priority=requests.data.get('priority')
    labels=requests.data.get('labels')
    assignee=requests.data.get('assignee')
    issue_object = Issues().create_issue(title=title, description=description, project=p_id,
                                      issue_type=issue_type, summary=summary, priority=priority,
                                      labels=labels, assignee=assignee)
    serialiser=IssuesSerializer(issue_object)
    return Response(status=201,data=serialiser.data)


