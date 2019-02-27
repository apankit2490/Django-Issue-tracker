from rest_framework import serializers

from Issues.models import Issues
from .models import *


class IssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Labels_issues
        fields = '__all__'