from django.shortcuts import render
from django.utils.translation import gettext as _
from django.conf import settings
from app.settings_db import get_setting
from django.utils import translation


# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'title':  _('Home'),
        'app_name': settings.APP_NAME,
        'app_home_head_html': get_setting('app_home_head_html', language=translation.get_language()),
        'app_home_body_html': get_setting('app_home_body_html', language=translation.get_language()),
    })
