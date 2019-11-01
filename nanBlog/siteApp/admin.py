from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class instagram_feedAdmin(admin.ModelAdmin):

    list_display = ('date_add', 'date_update', 'status', 'image')
    list_filter = (
        'date_add',
        'date_update',
        'status',
    )


class FooterAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'follow_us',
        'about_us',
        'newslleter',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'follow_us',
        'about_us',
        'newslleter',
    )


class BackgroundAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'home',
        'autres',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'home',
        'autres',
    )


class HomeAdmin(admin.ModelAdmin):

    list_display = ('date_add', 'date_update', 'status', 'text')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'text',
    )


class MembreAdmin(admin.ModelAdmin):

    list_display = ('date_add', 'date_update', 'status', 'text')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'text',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.instagram_feed, instagram_feedAdmin)
_register(models.Footer, FooterAdmin)
_register(models.Background, BackgroundAdmin)
_register(models.Home, HomeAdmin)
_register(models.Membre, MembreAdmin)
