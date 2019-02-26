from django.db import models


# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return str(Project().name)

    def get_all_project(self):
        return Project.objects.all()

    class Meta:
        db_table='Project'




