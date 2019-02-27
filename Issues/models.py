from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from Project.models import Project
from django.contrib.auth.models import User
from Issues.helper import *


class Sprint(models.Model):
    Name=models.CharField(max_length=50)
    Project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project_sprint',null=True)


    def __str__(self):
        return self.Name

class IssueManager(models.Manager):

    def get_all_issues_of_project(self,project_id):
        filtered_projects=Project.objects.get(pk=project_id)
        all_issues=Issues.objects.all().filter(project=filtered_projects)
        all_issues_decending_date=all_issues.order_by('create_date').reverse()
        return all_issues_decending_date

    def get_all_issues_of_project_without_ordering(self,project_id):
        filtered_projects=Project.objects.get(pk=project_id)
        all_issues=Issues.objects.all().filter(project=filtered_projects)
        return all_issues

    def assign_issue_to_user(self,issue_id,user_id):
        issues=Issues.objects.get(id=issue_id)
        active_user=issues.project.user.id
        if(user_id==active_user):
            user=User.objects.get(id=user_id)
            issues.assignee=user
            issues.save()
            return issues
        else:
            return None

    def update_issue_status(self,issue_id, updated_status):
        issue_object=Issues.objects.get(id=issue_id)
        status=issue_object.status
        if(status=='OP' and updated_status=='AG'):
            issue_object.status=updated_status
            issue_object.save()
            return issue_object

        elif(status=='AG' and updated_status=='IP'):
            issue_object.status=updated_status
            issue_object.save()
            return issue_object

        elif (status == 'IP' and updated_status == 'UR'):
            issue_object.status = updated_status
            issue_object.save()
            return issue_object

        elif (status == 'UR' and updated_status == 'DN'):
            issue_object.status = updated_status
            issue_object.save()
            return issue_object

        elif (status == 'DN' and updated_status == 'CL'):
            issue_object.status = updated_status
            issue_object.save()
            return issue_object

        else:
            raise ObjectDoesNotExist


    #
    # def get_issue_assigned_to_user(self,user_id):
    #     self.




    # def get_all_issues_of_project_pagination(self):

class Issues(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project',null=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField('update date',auto_now_add=True)
    issue_type = models.CharField(max_length=2,choices=ISSUE_TYPE_CHOICES,default=TASK)
    status=models.CharField(max_length=2,choices=STATUS_TYPE_CHOICE,default=OPEN)
    summary = models.CharField(max_length=30,null=True)
    priority = models.CharField(max_length=2,choices=PRIORITY_TYPE_CHOICES,default=MEDIUM,null=True)
    labels = models.CharField(max_length=30,null=True)
    assignee = models.ForeignKey(User,on_delete=models.CASCADE,related_name='User',null=True,default=User)
    sprint=models.ForeignKey(Sprint,on_delete=models.CASCADE,related_name='sprint',null=True)

    issue_manager=IssueManager()
    objects=models.Manager()


    def get_title(self):
        return self.title

    def get_name(self):
        return self.description


    def create_issue(self,title, description, project,issue_type, summary, priority,labels,assignee,sprint):
        assigned_user=User.objects.get(id=assignee)
        project_assigned=Project.objects.get(id=project)
        sprint_obj=Sprint.objects.get(id=sprint)
        issue_obj=Issues.objects.create(title=title, description=description, project=project_assigned,
                              issue_type=issue_type, summary=summary, priority=priority,
                              labels=labels,assignee=assigned_user,sprint=sprint_obj)
        issue_obj.save()
        return issue_obj



    # def is_upperclass(self):
    #     return self.year_in_school in (self.JUNIOR, self.SENIOR)


