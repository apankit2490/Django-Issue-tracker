from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.db.models import QuerySet
from django.test import TestCase, Client
from Constants import *
# Create your tests here.
from Issues.models import Issues
from Project.models import Project
from rest_framework.test import APIClient

class Testapi_issue(TestCase):

    def setUp(self):
        self.client = Client()
        self.base_url='/api/issues'
        self.project_object = Project.objects.create(name=TEST_PROJECT_NAME, description=TEST_PROJECT_DESCRIPTION)
        self.user = User.objects.create_user(TEST_ISSUE_NEW_USERNAME, TEST_ISSUE_NEW_EMAIL, TEST_ISSUE_NEW_PASSWORD)
        Issues.objects.create(title=TEST_ISSUE_TITILE, description=TEST_ISSUE_DESC, project=self.project_object,
                              issue_type=TEST_ISSUE_BUG, summary=TEST_ISSUE_SUMMARY, priority=TEST_ISSUE_PRIORITY,
                              labels=TEST_ISSUE_LABELS, assignee=self.user)
        self.issue_obj = Issues()

    def test_create_issue_api(self):
        url=self.base_url+'/create-issue/'
        payload=test_api_create_issue_payload
        response=self.client.post(url,data=payload)
        self.assertEqual(response.status_code,201)

