from django.urls import path

from Issues.views import *

urlpatterns = [
    path('issues/create-issue/',create_issue,name='create_issue'),
    # path('projects/get-project/<int:p_id>/',get_project_by_id,name='get_project_by_id'),

]