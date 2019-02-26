from django.contrib.sites import requests
from django.db.models import QuerySet
from django.test import TestCase, Client
from Constants import *
# Create your tests here.
from Project.models import Project
from rest_framework.test import APIClient

class Testapi(TestCase):

    def setUp(self):
        self.client = Client()
        self.base_url='/api/projects'

    def test_get_all_projects_api(self):
        url=self.base_url+'/get-all-projects/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,201)

