from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'nom')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
        'nom',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'nom',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
        'nom',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'temps_de_lecture',
        'titre',
        'titre_slug',
        'description',
        'categorie_id',
        'contenu',
        'photo',
        'auteur',
        'nb_com',
        'nb_like',
        'nb_re_commentaitre',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'categorie_id',
        'auteur',
        'date_add',
        'date_update',
        'status',
        'id',
        'temps_de_lecture',
        'titre',
        'titre_slug',
        'description',
        'categorie_id',
        'contenu',
        'photo',
        'auteur',
        'nb_com',
        'nb_like',
        'nb_re_commentaitre',
        'date_add',
        'date_update',
        'status',
    )
    raw_id_fields = ('tag_name',)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'contenu',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'id',
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'contenu',
    )


class ReplyAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'commentaire_id',
        'article_id',
        'username',
        'contenu',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'commentaire_id',
        'article_id',
        'username',
        'id',
        'date_add',
        'date_update',
        'status',
        'commentaire_id',
        'article_id',
        'username',
        'contenu',
    )


class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'person',
        'article',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'person',
        'article',
        'id',
        'date_add',
        'date_update',
        'status',
        'person',
        'article',
    )


class searchAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'query',
        'visiteur',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'visiteur',
        'id',
        'date_add',
        'date_update',
        'status',
        'query',
        'visiteur',
    )


class VueAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'article',
        'visiteur',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'article',
        'visiteur',
        'id',
        'date_add',
        'date_update',
        'status',
        'article',
        'visiteur',
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
