from django.db import models


# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30,null=True)



    def get_name(self):
        return str(Project().name)



