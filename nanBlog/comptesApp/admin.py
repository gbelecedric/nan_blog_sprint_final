from django.contrib import admin
from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'imageprofile')
    list_filter = ('id', 'user', 'imageprofile')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)