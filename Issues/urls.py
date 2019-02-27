from django.urls import path

from Issues.views import *

urlpatterns = [
    path('issues/create-issue/',create_issue,name='create_issue'),
    path('issues/get-issues-project/<int:p_id>/',get_all_issues_of_project_api,name='get_issue_by_id'),
    path('issues/get-issues-project/pagination/<int:p_id>/<int:offset>/<int:limit>/',get_all_issues_of_project_pagination_api,name='get_issue_by_id_pagination'),
    # path('projects/get-project/<int:p_id>/',get_project_by_id,name='get_project_by_id'),

]