from django.db import models
from Project.models import Project
from django.contrib.auth.models import User
from Issues.helper import *


class Issues(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project',null=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    issue_type = models.CharField(max_length=2,choices=ISSUE_TYPE_CHOICES,default=TASK)
    summary = models.CharField(max_length=30,null=True)
    priority = models.CharField(max_length=2,choices=PRIORITY_TYPE_CHOICES,default=MEDIUM,null=True)
    labels = models.CharField(max_length=30,null=True)
    assignee = models.ForeignKey(User,on_delete=models.CASCADE,related_name='User',null=True,default=User)

    def get_title(self):
        return self.title

    def get_name(self):
        return self.description



    # def is_upperclass(self):
    #     return self.year_in_school in (self.JUNIOR, self.SENIOR)



