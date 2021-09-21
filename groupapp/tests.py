from django.test import TestCase
from django.test.client import Client


class TestAuthapp(TestCase):
    fixtures = [
        "mainapp/fixtures/001_category_task.json",
        "mainapp/fixtures/001_task.json",
        "authapp/fixtures/001_site_user.json",
        "authapp/fixtures/001_contact_user.json",
        "authapp/fixtures/001_professions.json",
        # "chatapp/fixtures/001_room_chat.json",
        # "chatapp/fixtures/001_message_chat.json",
        "groupapp/fixtures/001_group.json",
        "groupapp/fixtures/001_description_need_professions.json",
        "groupapp/fixtures/001_application_to_need_profession.json",
        "groupapp/fixtures/001_member_team.json",
        # "messageapp/fixtures/001_chat_manager.json",
        "messageapp/fixtures/001_dialog.json",
        "messageapp/fixtures/001_message.json",
    ]

    def setUp(self):
        self.client = Client()

    def test_authapp_urls(self):
        response = self.client.get("/group/groups/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/groups/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/create_group/")
        self.assertEqual(response.status_code, 302)

        # response = self.client.get("/group/group/1/")
        # self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/update_group/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/delete_group/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/setting/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/update_vacancy/1/")
        self.assertEqual(response.status_code, 200)

        # response = self.client.get("/group/user_groups/1/")
        # self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/need_profession_description/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/create_application_need_prof/1/")
        self.assertEqual(response.status_code, 302)

        response = self.client.get("/group/applications_to_team/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/api/update_applications_to_team/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/tasks_for_group/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/search_group_name/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/search_group_by_name/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/search_group_prof/")
        self.assertEqual(response.status_code, 200)

        # response = self.client.get("/group/search_group_by_prof/")
        # self.assertEqual(response.status_code, 200)

        response = self.client.get("/group/tasks_done_for_group/1/")
        self.assertEqual(response.status_code, 200)
