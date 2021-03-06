from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Issues.models import Issues
from Issues.serializers import IssuesSerializer, LabelSerializer


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
    sprint=requests.data.get('sprint')
    issue_object = Issues().create_issue(title=title, description=description, project=p_id,
                                      issue_type=issue_type, summary=summary, priority=priority,
                                       assignee=assignee,sprint=sprint)
    serialiser=IssuesSerializer(issue_object)
    return Response(status=201,data=serialiser.data)

@api_view(["GET"])
def get_all_issues_of_project_api(requests,p_id):
    filtered_issues_objs=Issues.issue_manager.get_all_issues_of_project(p_id)
    serializer=IssuesSerializer(filtered_issues_objs,many=True)
    return Response(status=201,data=serializer.data)

@api_view(["GET"])
def get_all_issues_of_project_pagination_api(requests,p_id, offset, limit):
    filtered_objs=Issues.issue_manager.get_all_issues_of_project_without_ordering(p_id)[offset-1:limit]
    serialiser=IssuesSerializer(filtered_objs,many=True)
    return Response(status=201,data=serialiser.data)

@api_view(["POST"])
def assign_issue_to_user_api(requests):
    issue_id=requests.data.get('issue_id')
    user_id=requests.data.get('user_id')
    # try:
    issues_updated=Issues.issue_manager.assign_issue_to_user(issue_id,user_id)
    serialiser=IssuesSerializer(issues_updated)
    return Response(status=201,data=serialiser.data)
    # except ObjectDoesNotExist:
    #     return Response("requested user is not in the active project",status=202)

@api_view(["POST"])
def update_issue_status_api(requests):
    issue_id=requests.data.get('issue_id')
    update_status=requests.data.get('update_status')
    status_updated_issues=Issues.issue_manager.update_issue_status(issue_id,update_status)
    serialiser = IssuesSerializer(status_updated_issues)
    return Response(status=201,data=serialiser.data)

@api_view(["GET"])
def get_issue_assigned_to_user_api(requests):
    current_user = requests.user
    try:
        uid=current_user.id
    except:
        uid=1
    result=Issues.issue_manager.get_issue_assigned_to_user(uid)
    serialiser = IssuesSerializer(result,many=True)
    return Response(status=201,data=serialiser.data)

@api_view(["POST"])
def add_label_to_issue_api(requests):
    issue_id=requests.data.get('issue_id')
    label=requests.data.get('label')
    label_object=Issues.issue_manager.add_label_to_issue(issue_id,label)
    serialiser = LabelSerializer(label_object)
    return Response(status=201, data=serialiser.data)







