from django.contrib.auth.models import User
from django.test import TestCase

from Project.models import Project
from Constants import *

# Create your tests here.
from Issues.models import Issues, Sprint, Labels_issues


class TestIssues(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(TEST_ISSUE_NEW_USERNAME, TEST_ISSUE_NEW_EMAIL,TEST_ISSUE_NEW_PASSWORD)
        self.project_object = Project.objects.create(name=TEST_PROJECT_NAME, description=TEST_PROJECT_DESCRIPTION,
                                                     user=self.user)

        Issues.objects.create(title=TEST_ISSUE_TITILE, description=TEST_ISSUE_DESC, project=self.project_object,
                              issue_type=TEST_ISSUE_BUG, summary=TEST_ISSUE_SUMMARY, priority=TEST_ISSUE_PRIORITY,
                              assignee=self.user)

        self.issue_obj=Issues()
        self.sprint = Sprint.objects.create(Name='Sprint 3', Project=self.project_object)

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



    def test_issue_user(self):
        issue_object = Issues.objects.get(assignee=self.user)
        self.assertEqual(issue_object.assignee.get_username() ,TEST_ISSUE_NEW_USERNAME)

    def test_create_issue(self):
        test_issue_obj=self.issue_obj.create_issue(title='testcase titile',description='test_case description',
                                                   project=1,issue_type='EP',summary='teestcase summary',priority='LW',
                                                   assignee=1,sprint=1)
        self.assertEqual(test_issue_obj.title,'testcase titile')

    def test_get_all_issues_of_project(self):
        get_all_issues_of_project=Issues.issue_manager.get_all_issues_of_project(1)
        self.assertTrue(type(get_all_issues_of_project[0]) is Issues)

    def test_get_all_issues_of_project_pagination(self):
        p_id=1
        offset=1
        limit=2
        filtered_objs = Issues.issue_manager.get_all_issues_of_project_without_ordering(p_id)[offset - 1:limit]
        self.assertEqual(len(filtered_objs), 1)

    def test_assign_issue_to_user(self):
        fetchetd_issues=Issues.issue_manager.assign_issue_to_user(1,1)
        self.assertEqual(fetchetd_issues.assignee.id, 1)


    def test_update_issue_status(self):
        issue_id=1
        update='AG'
        update_status=Issues.issue_manager.update_issue_status(issue_id,update)
        self.assertEqual(update_status.status,'AG')
        issue_id = 1
        update = 'IP'
        update_status = Issues.issue_manager.update_issue_status(issue_id, update)
        self.assertEqual(update_status.status, 'IP')
        issue_id = 1
        update = 'UR'
        update_status = Issues.issue_manager.update_issue_status(issue_id, update)
        self.assertEqual(update_status.status, 'UR')
        issue_id = 1
        update = 'DN'
        update_status = Issues.issue_manager.update_issue_status(issue_id, update)
        self.assertEqual(update_status.status, 'DN')
        issue_id = 1
        update = 'CL'
        update_status = Issues.issue_manager.update_issue_status(issue_id, update)
        self.assertEqual(update_status.status, 'CL')

    def test_get_issue_assigned_to_user(self):
        uid=1
        issues=Issues.issue_manager.get_issue_assigned_to_user(uid)
        self.assertEqual(type(issues[0]),Issues)

    def test_add_label_to_issue(self):
        issue_id=1
        name='django'
        label_object=Issues.issue_manager.add_label_to_issue(issue_id,name)
        self.assertEqual(label_object.Name,name)






