from rest_framework import serializers

from Issues.models import Issues
from .models import *


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')