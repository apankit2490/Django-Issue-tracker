from django.db.models import QuerySet
from django.test import TestCase
from Constants import *
# Create your tests here.
from Project.models import Project


class TestProject(TestCase):

    def setUp(self):
        Project.objects.create(name=TEST_PROJECT_NAME,description=TEST_PROJECT_DESCRIPTION)

    def test_create_project_title(self):
        project_name=Project.objects.get(name=TEST_PROJECT_NAME)
        self.assertEqual(project_name.name , TEST_PROJECT_NAME)

    def test_create_project_description(self):
        project_name=Project.objects.get(description=TEST_PROJECT_DESCRIPTION)
        self.assertEqual(project_name.description , TEST_PROJECT_DESCRIPTION)

    def test_get_all_objects(self):
        all_projects=Project().get_all_project()
        self.assertTrue(type(all_projects) is QuerySet)
        self.assertEqual(all_projects[0].name,TEST_PROJECT_NAME)


