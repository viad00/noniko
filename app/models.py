from django.db import models

# Create your models here.


class Setting(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=5)
    string = models.TextField()
