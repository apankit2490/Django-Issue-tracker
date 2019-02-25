import unittest

from django.test import TestCase

# Create your tests here.
from Project.models import Project


class TestProject(TestCase):
    @classmethod
    def setUp(self):
        Project.objects.create(name='First_project')

    def test_create_project(self):
        project_name=Project.objects.get(name='First_project')
        self.assertEqual(project_name.name , Project().get_name())

