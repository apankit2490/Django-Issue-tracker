from django.urls import path

from Project.views import get

urlpatterns = [
    path('get/',get,name='get'),
]
