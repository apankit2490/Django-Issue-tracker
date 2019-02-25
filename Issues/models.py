from django.db import models

# Create your models here.
class Issues(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

    def get_title(self):
        return self.title

    def get_name(self):
        return self.description



