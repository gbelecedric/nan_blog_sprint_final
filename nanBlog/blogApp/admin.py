<<<<<<< HEAD
=======
from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TagAdmin(admin.ModelAdmin):

    list_display = ('date_add', 'date_update', 'status', 'nom')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'nom',
    )
    


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'titre',
        'nom',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'titre',
        'nom',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'categorie_id',
        'photo',
        'auteur',
        'nb_like',
        'nb_re_commentaitre',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'titre',
        'description',
        'categorie_id',
        'auteur',
        'nb_like',
        'nb_re_commentaitre',
        'date_add',
        'date_update',
        'status',
    )
    raw_id_fields = ('tag_name',)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
    )
    list_filter = (
        'article_id',
        'username',
        'date_add',
        'date_update',
        'status',

    )


class ReplyAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'commentaire_id',
        #'article',
        'username',
    )
    list_filter = (
        'commentaire_id',
        #'article',
        'username',
        'date_add',
        'date_update',
        'status',
    )


class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'person',
        'article',
    )
    list_filter = (
        'person',
        'article',
        'date_add',
        'date_update',
        'status',
    )


class searchAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'query',
        'visiteur',
    )
    list_filter = (
        'visiteur',
        'date_add',
        'date_update',
        'status',
        'query',
    )


class VueAdmin(admin.ModelAdmin):

    list_display = (
        'date_add',
        'date_update',
        'status',
        'article',
        'visiteur',
    )
    list_filter = (
        'article',
        'visiteur',
        'date_add',
        'date_update',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Tag, TagAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Reply, ReplyAdmin)
_register(models.Like, LikeAdmin)
_register(models.search, searchAdmin)
_register(models.Vue, VueAdmin)
>>>>>>> c1d2415ac056d7d971c894ac0ee5bbf10739814c
