from django.contrib import admin
from .models import Setting, File
from django.conf import settings

# Register your models here.


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'string_short')
    search_fields = ('name', )

    def string_short(self, obj):
        if len(obj.string) > 70:
            return obj.string[:70] + '...'
        else:
            return obj.string


class FileAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Setting, SettingAdmin)
admin.site.register(File, FileAdmin)
admin.site.site_header = settings.APP_NAME + ' administration'
