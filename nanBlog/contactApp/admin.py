# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
        'email',
        'sujet',
        'message',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'email',
        'sujet',
        'nom',
        'message',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'email')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'email',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Message, MessageAdmin)
_register(models.Newsletter, NewsletterAdmin)
