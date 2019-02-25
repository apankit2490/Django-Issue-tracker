from django.db import models


# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=30)

    def get_name(self):
        return str(Project().name)



