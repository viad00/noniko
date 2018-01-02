from django.shortcuts import render
from django.utils.translation import gettext as _
from django.conf import settings
from app.settings_db import get_setting


# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'title':  _('Home'),
        'app_name': settings.APP_NAME,
        'app_description_text': get_setting('app_description_text'),
    })
