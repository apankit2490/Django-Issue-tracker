TEST_PROJECT_NAME='First_project_test'
TEST_PROJECT_NAME2='Second_project_test'
TEST_PROJECT_DESCRIPTION='Test Description'
TEST_PROJECT_DESCRIPTION2='Test Second Description'
TEST_ISSUE_TITILE='Test_issue'
TEST_ISSUE_DESC='Test_description'
TEST_ISSUE_SUMMARY='Test Summary'
TEST_ISSUE_LABELS= 'Test Labels'
TEST_ISSUE_BUG='BG'
TEST_ISSUE_PRIORITY='HG'
TEST_ISSUE_NEW_USERNAME='ankit'
TEST_ISSUE_NEW_USERNAME2='ankitkumar'
TEST_ISSUE_NEW_EMAIL='lennon@thebeatles.com'
TEST_ISSUE_NEW_PASSWORD='johnpassword'
test_api_create_issue_payload = {'title': 'test case title', 'description': 'test_case description', 'project_id': 1,
                                 'issue_type': 'EP', 'summary': 'teestcase summary', 'priority': 'LW',
                                 'assignee': 1,'sprint':1}

test_api_assign_issue_payoad={"issue_id":2,"user_id":2}
test_api_update_status_payload={"issue_id":1,"update_status":"AG"}
