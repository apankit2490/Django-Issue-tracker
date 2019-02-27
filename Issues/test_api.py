from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.db.models import QuerySet
from django.test import TestCase, Client
from Constants import *
# Create your tests here.
from Issues.models import Issues, Sprint
from Project.models import Project
from rest_framework.test import APIClient

class Testapi_issue(TestCase):

    def setUp(self):
        self.client = Client()
        self.base_url='/api/issues'
        self.project_object = Project.objects.create(name=TEST_PROJECT_NAME, description=TEST_PROJECT_DESCRIPTION)
        self.user = User.objects.create_user(TEST_ISSUE_NEW_USERNAME, TEST_ISSUE_NEW_EMAIL, TEST_ISSUE_NEW_PASSWORD)
        self.user2 = User.objects.create_user(TEST_ISSUE_NEW_USERNAME2, 'sss@gmail.com', TEST_ISSUE_NEW_PASSWORD)
        self.project_object2 = Project.objects.create(name=TEST_PROJECT_NAME, description=TEST_PROJECT_DESCRIPTION,
                                                      user=self.user2)
        Issues.objects.create(title=TEST_ISSUE_TITILE, description=TEST_ISSUE_DESC, project=self.project_object,
                              issue_type=TEST_ISSUE_BUG, summary=TEST_ISSUE_SUMMARY, priority=TEST_ISSUE_PRIORITY,
                              labels=TEST_ISSUE_LABELS, assignee=self.user)
        Issues.objects.create(title='', description=TEST_ISSUE_DESC, project=self.project_object2,
                              issue_type=TEST_ISSUE_BUG, summary=TEST_ISSUE_SUMMARY, priority=TEST_ISSUE_PRIORITY,
                              labels=TEST_ISSUE_LABELS, assignee=self.user)
        self.issue_obj = Issues()
        self.sprint = Sprint.objects.create(Name='Sprint 3', Project=self.project_object)

    def test_create_issue_api(self):
        url=self.base_url+'/create-issue/'
        payload=test_api_create_issue_payload
        response=self.client.post(url,data=payload)
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data.get('title'),'test case title')

    def test_get_all_issues_of_project_api(self):
        url=self.base_url+'/get-issues-project/'
        response=self.client.get(url+'1'+'/')
        self.assertEqual(response.status_code,201)
        self.assertTrue(response.data[0].get('project')==1)

    def test_get_all_issues_of_project_pagination_api(self):
        url=self.base_url+'/get-issues-project/pagination/'
        p_id='1'
        offset='1'
        limit='2'
        response=self.client.get(url+p_id+'/'+offset+'/'+limit+'/')
        self.assertEqual(response.status_code,201)
        self.assertEqual(len(response.data),1)

    def test_assign_issue_to_user_api(self):
        url=self.base_url+'/assign-issue/'
        payload=test_api_assign_issue_payoad
        response=self.client.post(url,data=payload)
        self.assertEqual(response.status_code,201)

    def test_update_issue_status_api(self):
        url=self.base_url+'/update-status/'
        payload=test_api_update_status_payload
        response=self.client.post(url,data=payload)
        self.assertEqual(response.status_code,201)






