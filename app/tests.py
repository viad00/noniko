from django.test import TestCase
from app.models import Setting, File
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

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
        self.assertContains(response, 'A<br>correct<br><h1>HTML<h1> string', 1, 200)

    def test_ru_header_load(self):
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='ru')
        self.assertContains(response, 'Строка русского текста', 1, 200)
        self.assertContains(response, '<html lang="ru">', 1, 200)
        self.assertContains(response, 'A<br>correct<br><h1>HTML<h1> string', 1, 200)


class FileTestCase(TestCase):
    """Uploaded files are correctly served"""
    def setUp(self):
        File.objects.create(name='sample_file', file=SimpleUploadedFile('sample.txt', b'This is sample file.'))

    def doCleanups(self):
        clean = File.objects.get(name='sample_file')
        clean.file.delete(save=False)
        clean.delete()

    def test_file_read(self):
        self.assertEqual(File.objects.get(name='sample_file').file.readline(), b'This is sample file.')

    def test_file_get_url(self):
        response = self.client.get('/get_file', {'name': 'sample_file'})
        self.assertEqual(response.url, '/media/sample.txt')
