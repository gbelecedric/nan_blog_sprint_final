from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'contacts', 'image', 'birth_date')
    list_filter = (
        'user',
        'contacts',
        'birth_date',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
