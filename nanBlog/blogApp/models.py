 #--------------------import--blog-----------#
import uuid
from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.utils.text import slugify
from datetime import datetime
from statistiqueApp.models import Visitor_Infos_user

from comptesApp.models import *
# Create your models here.
#------------------------ blog_app_model --------------#
class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)

    class Meta:
        abstract=True


class Tag(Timemodels):
    nom = models.CharField(max_length=225)

    def __str__(self):
        return self.nom

class Categorie(Timemodels):
    titre =  models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorie',)
    nom =  models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='ctegorieuser')

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorie'

    
    def __str__(self):
        return self.titre

class Article(models.Model):
    temps_de_lecture = models.CharField(max_length=255, null=True)
    titre =  models.CharField(max_length=255)
    titre_slug = models.SlugField(max_length=255,editable=False,default=uuid.uuid4, null=True)
    description = models.TextField()
    categorie_id =  models.ForeignKey(Categorie,on_delete=models.CASCADE, related_name="articles")
    contenu =  HTMLField('article_description', null=True)
    photo = models.ImageField(upload_to ='article')
    tag_name = models.ManyToManyField(Tag, related_name="tag_article")
    auteur =  models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    nb_com = models.PositiveIntegerField(editable=False,)
    nb_like = models.PositiveIntegerField(editable=False,)
    nb_re_commentaitre = models.PositiveIntegerField(editable=False,)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=False)
  
    @property
    def nbr_like(self):
        n = self.likes.all().count()
        return n

    @property
    def nbr_comment(self):
        n = self.commentaires.all().count()
   
        return n
    
    @property
    def nb_reply(self):
        n = self.re_commentaires.all().count()
        return n

    @property
    def nb_vues(self):
        n = self.vues.all().count()
        return n


    def save(self, *args, **kwargs):
        u3 = uuid.uuid3(uuid.NAMESPACE_DNS,  str(self.pk))
        self.titre_slug ='@'+ slugify(self.titre + str(u3) + str(self.pk)  + self.auteur.Profilename )
        self.nb_com = self.nbr_comment
        self.nb_like=self.nbr_like
        self.nb_re_commentaitre=self.nb_reply

        super(Article, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Article'
   
    def __str__(self):
        return self.titre
    
    
class Commentaire(Timemodels):
    article_id =  models.ForeignKey(Article,on_delete=models.CASCADE, related_name="commentaires")
    username =  models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="re_Profile")
    contenu =  models.TextField(null=True)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaire des postes'
    

    
class Reply(Timemodels):
    commentaire_id =  models.ForeignKey(Commentaire,on_delete=models.CASCADE, related_name="reponses")
    article_id =  models.ForeignKey(Article,on_delete=models.CASCADE, related_name="re_commentaires")
    username =  models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="userreply")
    contenu =  models.TextField(null=True)

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'reponse aux commentaires'


class Like(Timemodels):
    person =  models.ForeignKey(User,on_delete=models.CASCADE, related_name="likes_visiteur")
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name="likes")

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return self.person
    
class search (Timemodels):
    query= models.CharField(max_length=250)
    visiteur = models.ForeignKey(Visitor_Infos_user, on_delete=models.CASCADE, related_name='searchs')

    class Meta:
        verbose_name = 'serarch'
        verbose_name_plural = 'les recherches des utilisateurs'

class Vue(Timemodels): # Pour faciliter les requêtes on va directement lié Visitor_Infos_user de statistique et article
    """Model definition for Vue."""

    # TODO: Define fields here
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name="vues_articles")
    visiteur = models.ForeignKey(Visitor_Infos_user, on_delete=models.CASCADE, related_name='vues')


    class Meta:
        """Meta definition for Vue."""

        verbose_name = 'Vue'
        verbose_name_plural = 'Vues'

    def __str__(self):
        """Unicode representation of Vue."""
        return "{}".format(visiteur.ip)
