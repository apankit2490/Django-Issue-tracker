from django.contrib import admin
from Issues.models import Sprint
# Register your models here.
from Issues.models import *

admin.site.register(Issues)
admin.site.register(Sprint)
admin.site.register(Labels_issues)