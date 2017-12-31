from django.core.exceptions import ObjectDoesNotExist
from app.models import Setting
from django.conf import settings


def get_setting(name, language=settings.LANGUAGE_CODE):
    # TODO: This function
    try:
        return Setting.objects.filter(name=name)[0].get().string
    except ObjectDoesNotExist:
        return 'Oops, setting {0} not found!'.format(name)
