from rest_framework import serializers

from blogApp.models import *
from comptesApp.models import *
from siteApp.models import *
from contactApp.models import *
from configurationApp.models import *
from statistiqueApp.models import *
from .models import *

from drf_dynamic_fields import DynamicFieldsMixin

#=============== App siteApp ==============#

class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = '__all__'

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'

class instagram_feedSerializer(serializers.ModelSerializer):
    class Meta:
        model = instagram_feed
        fields = '__all__'


#=============== App configurationApp ==============#

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


#=============== App compteApp ==============#

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


#=============== App ContactApp ==============#

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


#=============== App BlogApp ==============#

class VueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vue
        fields = '__all__'

class searchSerializer(serializers.ModelSerializer):
    class Meta:
        model = search
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    reponses = ReplySerializer(many=True, required=False)
    class Meta:
        model = Commentaire
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    commentaires = CommentaireSerializer(many=True, required=False)
    re_commentaires = ReplySerializer(many=True, required=False)
    likes = LikeSerializer(many=True, required=False)
    vues = VueSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    tag_article = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Tag
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Categorie
        fields = '__all__'


#=============== App StatistiqueApp ==============#

class Visitor_Infos_userSerializer(serializers.ModelSerializer):
    vues = VueSerializer(many=True, required=False)
    searchs = searchSerializer(many=True, required=False)
    articles = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Visitor_Infos_user
        fields = '__all__'

