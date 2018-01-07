from django.test import TestCase
from app.models import Setting
from django.conf import settings

# Create your tests here.


class HomeTestCase(TestCase):
    """Home page is loading and translates correctly"""
    def setUp(self):
        Setting.objects.create(name='app_home_head_html', language='en', string='A correct english string')
        Setting.objects.create(name='app_home_head_html', language='ru', string='Строка русского текста')
        Setting.objects.create(name='app_home_body_html', language='en', string='A<br>correct<br><h1>HTML<h1> string')

    def test_load(self):
        response = self.client.get('/')
        self.assertContains(response, 'A correct english string', 1, 200)
        self.assertContains(response, 'A<br>correct<br><h1>HTML<h1> string', 1, 200)
        self.assertContains(response, settings.APP_NAME)

    def test_ru_cookie_load(self):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'ru'})
        response = self.client.get('/')
        self.assertContains(response, 'Строка русского текста', 1, 200)
        self.assertContains(response, '<html lang="ru">', 1, 200)

    def test_ru_header_load(self):
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='ru')
        self.assertContains(response, 'Строка русского текста', 1, 200)
        self.assertContains(response, '<html lang="ru">', 1, 200)
