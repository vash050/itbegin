import datetime

from django.test import TestCase
from django.test.client import Client

from authapp.forms import SiteUserRegisterForm, SiteUserUpdateForm, SiteUserUpdateContact
from authapp.models import SiteUser, Professions, ContactUser


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
        SiteUser.objects.create(
            username='TestUser',
            first_name='Ivan',
            last_name='Ivanov',
            email='Ivanov@test.com',
            is_staff=False,
            is_active=True,
            date_born='1977-12-11'.format(datetime.date),
            about_me='about user',
            link_to_portfolio='https://gb.ru/education',
            free=True
        )

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


class TestModelSiteUserAuthapp(TestCase):
    def setUp(self):
        SiteUser.objects.create(
            username='TestUser',
            first_name='Ivan',
            last_name='Ivanov',
            email='Ivanov@test.com',
            is_staff=False,
            is_active=True,
            date_born='1977-12-11'.format(datetime.date),
            about_me='about user',
            link_to_portfolio='https://gb.ru/education',
            free=True
        )

    def test_date_born_label(self):
        user = SiteUser.objects.get(id=1)
        field_label = user._meta.get_field('date_born').verbose_name
        self.assertEqual(field_label, 'день рождения')

    def test_about_me_label(self):
        user = SiteUser.objects.get(id=1)
        field_label = user._meta.get_field('about_me').verbose_name
        self.assertEqual(field_label, 'обо мне')

    def test_link_to_portfolio_label(self):
        user = SiteUser.objects.get(id=1)
        field_label = user._meta.get_field('link_to_portfolio').verbose_name
        self.assertEqual(field_label, 'ссылка на портфолио')

    def test_about_me_max_length(self):
        user = SiteUser.objects.get(id=1)
        max_length = user._meta.get_field('about_me').max_length
        self.assertEqual(max_length, 1000)

    def test_link_to_portfolio_max_length(self):
        user = SiteUser.objects.get(id=1)
        max_length = user._meta.get_field('link_to_portfolio').max_length
        self.assertEqual(max_length, 150)

    def test_user_name(self):
        user = SiteUser.objects.get(id=1)
        self.assertEqual(user.username, 'TestUser')

    def test_user_fist_name(self):
        user = SiteUser.objects.get(id=1)
        self.assertEqual(user.first_name, 'Ivan')


class TestModelProfessionsAuthapp(TestCase):
    def setUp(self):
        Professions.objects.create(profession_name='test profession')

    def test_professions_label(self):
        prof = Professions.objects.get(id=1)
        field_label = prof._meta.get_field('profession_name').verbose_name
        self.assertEqual(field_label, 'профессия')

    def test_professions_name(self):
        prof = Professions.objects.get(id=1)
        self.assertEqual(prof.profession_name, 'test profession')


class TestModelContactUserAuthapp(TestCase):
    def setUp(self):
        SiteUser.objects.create(
            username='TestUser',
            first_name='Ivan',
            last_name='Ivanov',
            email='Ivanov@test.com',
            is_staff=False,
            is_active=True,
            date_born='1977-12-11'.format(datetime.date),
            about_me='about user',
            link_to_portfolio='https://gb.ru/education',
            free=True
        )

        ContactUser.objects.update(
            user=SiteUser.objects.get(id=1),
            user_phone='+79114035689',
            user_email='Ivanov@test.com',
            user_instagram='https://www.instagram.com/',
            user_vk='https://vk.com/feed',
            user_telegram='https://telegram.org/'
        )

    def test_user_phone_label(self):
        cont = ContactUser.objects.get(user_id=1)
        field_label = cont._meta.get_field('user_phone').verbose_name
        self.assertEqual(field_label, 'телефон')

    def test_user_email_label(self):
        cont = ContactUser.objects.get(user_id=1)
        field_label = cont._meta.get_field('user_email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_user_instagram_label(self):
        cont = ContactUser.objects.get(user_id=1)
        field_label = cont._meta.get_field('user_instagram').verbose_name
        self.assertEqual(field_label, 'инстаграмм')

    def test_user_vk_label(self):
        cont = ContactUser.objects.get(user_id=1)
        field_label = cont._meta.get_field('user_vk').verbose_name
        self.assertEqual(field_label, 'вконтакте')

    def test_user_telegram_label(self):
        cont = ContactUser.objects.get(user_id=1)
        field_label = cont._meta.get_field('user_telegram').verbose_name
        self.assertEqual(field_label, 'телеграмм')

    def test_user_phone(self):
        cont = ContactUser.objects.get(user_id=1)
        self.assertEqual(cont.user_phone, '+79114035689')

    def test_user_email(self):
        cont = ContactUser.objects.get(user_id=1)
        self.assertEqual(cont.user_email, 'Ivanov@test.com')

    def test_user_instagram(self):
        cont = ContactUser.objects.get(user_id=1)
        self.assertEqual(cont.user_instagram, 'https://www.instagram.com/')

    def test_user_vk(self):
        cont = ContactUser.objects.get(user_id=1)
        self.assertEqual(cont.user_vk, 'https://vk.com/feed')

    def test_user_telegram(self):
        cont = ContactUser.objects.get(user_id=1)
        self.assertEqual(cont.user_telegram, 'https://telegram.org/')

    def test_get_absolute_url(self):
        cont = ContactUser.objects.get(user_id=1)
        self.assertEqual(cont.get_absolute_url(), '/auth/profile/')


class TestSiteUserRegisterForm(TestCase):
    def test_first_name_field_label(self):
        form = SiteUserRegisterForm()
        self.assertEqual(form.fields['first_name'].label, 'Имя')

    def test_last_name_field_label(self):
        form = SiteUserRegisterForm()
        self.assertEqual(form.fields['last_name'].label, 'Фамилия')

    def test_date_born_field_label(self):
        form = SiteUserRegisterForm()
        self.assertEqual(form.fields['date_born'].label, 'День рождения')

    def test_username_field_label(self):
        form = SiteUserRegisterForm()
        self.assertEqual(form.fields['username'].label, 'Имя пользователя')

    def test_email_field_label(self):
        form = SiteUserRegisterForm()
        self.assertEqual(form.fields['email'].label, 'Адрес электронной почты')

    def test_password1_field_label(self):
        form = SiteUserRegisterForm()
        self.assertEqual(form.fields['password1'].label, 'Пароль')

    def test_password2_field_label(self):
        form = SiteUserRegisterForm()
        self.assertEqual(form.fields['password2'].label, 'Подтверждение пароля')


class TestSiteUserUpdateForm(TestCase):
    def test_first_name_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['first_name'].label, 'Имя')

    def test_last_name_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['last_name'].label, 'Фамилия')

    def test_date_born_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['date_born'].label, 'День рождения')

    def test_username_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['username'].label, 'Имя пользователя')

    def test_avatar_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['avatar'].label, 'Аватар пользователя')

    def test_profession_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['profession'].label, 'Профессии')

    def test_about_me_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['about_me'].label, 'Обо мне')

    def test_link_to_portfolio_field_label(self):
        form = SiteUserUpdateForm()
        self.assertEqual(form.fields['link_to_portfolio'].label, 'Ссылка на портфолио')


class TestSiteUserUpdateContact(TestCase):
    def test_user_phone_field_label(self):
        form = SiteUserUpdateContact()
        self.assertEqual(form.fields['user_phone'].label, 'Телефон')

    def test_user_instagram_field_label(self):
        form = SiteUserUpdateContact()
        self.assertEqual(form.fields['user_instagram'].label, 'Инстаграмм')

    def test_user_vk_field_label(self):
        form = SiteUserUpdateContact()
        self.assertEqual(form.fields['user_vk'].label, 'Вконтакте')

    def test_user_telegram_field_label(self):
        form = SiteUserUpdateContact()
        self.assertEqual(form.fields['user_telegram'].label, 'Телеграмм')
