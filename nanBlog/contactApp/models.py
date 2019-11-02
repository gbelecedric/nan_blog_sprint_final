from django.db import models
from django.contrib.auth.models import User

class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True


class Message(Timemodels):
    
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    sujet = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.nom
    
    class Meta:
      

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Newsletter(Timemodels):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email