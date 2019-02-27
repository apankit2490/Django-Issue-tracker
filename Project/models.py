from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User_project',null=True,default=User)

    def __str__(self):
        return self.name

    def get_name(self):
        return str(Project().name)

    def get_all_project(self):
        return Project.objects.all()

    def  get_project_details(self,project_id):
        return Project.objects.get(pk=project_id)




    class Meta:
        db_table='Project'




