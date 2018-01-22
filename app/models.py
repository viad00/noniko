from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Setting(models.Model):
    def __str__(self):
        return 'Setting {0} - {1} ({2})'.format(self.name, self.language, self.id)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=5)
    string = HTMLField()


class File(models.Model):
    def __str__(self):
        return 'File {0} ({1})'.format(self.name, self.id)
    name = models.CharField(max_length=100)
    file = models.FileField()
