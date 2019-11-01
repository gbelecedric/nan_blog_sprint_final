from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Visitor_Infos_user(models.Model): # On va utiliser cette table pour faire les statistiques des utilisateurs
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_stat", null=True)
    page_visited = models.TextField()
    event_date =  models.DateTimeField(auto_now=True)
    pays = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    page_visited = models.TextField()
    reseau_mobile = models.CharField(max_length=50)
    status =  models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Visitor_Infos_user'
        verbose_name_plural = 'Visitor_Infos_users'
   
    def __str__(self):
        return self.ip