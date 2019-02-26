from django.urls import path

from Project.views import *

urlpatterns = [
    path('projects/get-all-projects/',get,name='get'),
    path('projects/get-project/<int:p_id>/',get_project_by_id,name='get_project_by_id'),

]
