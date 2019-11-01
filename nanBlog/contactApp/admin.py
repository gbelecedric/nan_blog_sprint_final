from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'nom',
        'message',
    )
    list_filter = (
        'nom',
        'date_add',
        'date_update',
        'status',
        'nom',
        'message',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('date_add', 'date_update', 'status', 'email')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'email',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Message, MessageAdmin)
_register(models.Newsletter, NewsletterAdmin)
