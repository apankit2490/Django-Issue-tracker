from django.contrib.auth.models import User
from django.test import TestCase

from Project.models import Project
from Constants import *
# Create your tests here.
from Issues.models import Issues


class TestIssues(TestCase):
    def setUp(self):
        project_object= Project.objects.create(name=TEST_PROJECT_NAME,description=TEST_PROJECT_DESCRIPTION)
        self.user = User.objects.create_user('ankit', 'lennon@thebeatles.com', 'johnpassword')
        Issues.objects.create(title=TEST_ISSUE_TITILE, description=TEST_ISSUE_DESC, project=project_object,
                              issue_type='BG', summary=TEST_ISSUE_SUMMARY, priority=TEST_ISSUE_PRIORITY,
                              labels=TEST_ISSUE_LABELS,assignee=self.user)

    def test_title_issue(self):
        issue_object=Issues.objects.get(title=TEST_ISSUE_TITILE)
        self.assertEqual(issue_object.title,TEST_ISSUE_TITILE)

    def test_description_issue(self):
        issue_object = Issues.objects.get(description=TEST_ISSUE_DESC)
        self.assertEqual(issue_object.description, TEST_ISSUE_DESC)

    def test_issue_type(self):
        issue_object = Issues.objects.get(issue_type=TEST_ISSUE_BUG)
        self.assertEqual(issue_object.issue_type,TEST_ISSUE_BUG)

    def test_issue_priority(self):
        issue_object = Issues.objects.get(priority=TEST_ISSUE_PRIORITY)
        self.assertTrue(issue_object.priority==TEST_ISSUE_PRIORITY)

    def test_issue_summary(self):
        issue_object = Issues.objects.get(summary=TEST_ISSUE_SUMMARY)
        self.assertTrue(issue_object.summary==TEST_ISSUE_SUMMARY)

    def test_issue_labels(self):
        issue_object = Issues.objects.get(labels=TEST_ISSUE_LABELS)
        self.assertTrue(issue_object.labels == TEST_ISSUE_LABELS)

    def test_issue_user(self):
        issue_object = Issues.objects.get(assignee=self.user)
        self.assertEqual(issue_object.assignee.get_username() ,'ankit')






