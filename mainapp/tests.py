from django.test import TestCase
from django.test.client import Client


class TestMainapp(TestCase):
    fixtures = [
        "mainapp/fixtures/001_category_task.json",
        "mainapp/fixtures/001_task.json",
        "authapp/fixtures/001_site_user.json",
        "authapp/fixtures/001_contact_user.json",
        "authapp/fixtures/001_professions.json",
        "chatapp/fixtures/001_room_chat.json",
        "chatapp/fixtures/001_message_chat.json",
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

    def test_mainapp_urls(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/task/1/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/create_task/")
        self.assertEqual(response.status_code, 200)

        # response.status_code == 302?
        # response = self.client.get(f"/get_task/1/")
        # self.assertEqual(response.status_code, 200)
