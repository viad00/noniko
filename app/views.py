from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.conf import settings
from .settings_db import get_setting
from django.utils import translation
from .models import File
from django.http import HttpResponseBadRequest


# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'title':  _('Home'),
        'app_name': settings.APP_NAME,
        'app_home_head_html': get_setting('app_home_head_html', language=translation.get_language()),
        'app_home_body_html': get_setting('app_home_body_html', language=translation.get_language()),
    })


def get_file(request):
    if not request.GET:
        return HttpResponseBadRequest()
    try:
        return redirect(get_object_or_404(File, name=request.GET['name']).file.url)
    except KeyError:
        return HttpResponseBadRequest()
