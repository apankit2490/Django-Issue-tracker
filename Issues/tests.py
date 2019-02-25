from django.test import TestCase

# Create your tests here.
from Issues.models import Issues


class TestIssues(TestCase):
    @classmethod
    def setUp(self):
        Issues.objects.create(title='Test_issue',description='Test_description')

    def test_title_project(self):
        issue_object=Issues.objects.get(title='Test_issue')
        self.assertEqual(issue_object.title,'Test_issue')

    def test_description_project(self):
        issue_object = Issues.objects.get(description='Test_description')
        self.assertEqual(issue_object.description, 'Test_description')

