from django.contrib import admin
from Issues.models import Sprint
# Register your models here.
from Issues.models import Issues

admin.site.register(Issues)
admin.site.register(Sprint)
