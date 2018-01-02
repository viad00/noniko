from django.core.exceptions import ObjectDoesNotExist
from app.models import Setting
from django.conf import settings


def get_setting(name, language=settings.LANGUAGE_CODE[:2]):
    try:
        return Setting.objects.filter(name=name, language=language)[0].get().string
    except IndexError:
        try:
            return Setting.objects.filter(name=name)[0].get().string
        except IndexError:
            return '<p class="error">Oops, setting {0} with language {1} not found!</p>'.format(name, language)
