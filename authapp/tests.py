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
        response = self.client.get("/auth/login/")
        self.assertEqual(response.status_code, 200)

        # response = self.client.get("/auth/profile/")
        # self.assertEqual(response.status_code, 200)

        response = self.client.get("/auth/register/")
        self.assertEqual(response.status_code, 200)

        # response = self.client.get("/auth/logout/")
        # self.assertEqual(response.status_code, 200)

        # response = self.client.get("/auth/update/")
        # self.assertEqual(response.status_code, 200)

        response = self.client.get("/auth/profile/1/")
        self.assertEqual(response.status_code, 200)

        # response = self.client.get("/auth/setting_user/1/")
        # self.assertEqual(response.status_code, 200)

        # response = self.client.get("/auth/up_setting_user_cont/1/")
        # self.assertEqual(response.status_code, 200)

        # response = self.client.get("/auth/change_password/")
        # self.assertEqual(response.status_code, 200)
