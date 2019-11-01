from django.db import models

# Create your models here.
class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True

    
class instagram_feed(Timemodels):
    image = models.ImageField(upload_to="image")
    
class Footer(Timemodels):
    follow_us =  models.CharField(max_length=250 ,verbose_name="text de follow_us")
    about_us =  models.CharField(max_length=250 ,verbose_name="text de about")
    newslleter =  models.CharField(max_length=250 ,verbose_name="text de newslleter")
    
    
    
    
class Background(Timemodels):
    home = models.ImageField(upload_to='home', )
    autres  = models.ImageField(upload_to='autres',)


class Home(Timemodels):
    text = models.CharField(max_length=250 ,verbose_name="text de contact")
    
class Membre(Timemodels):
    text = models.CharField(max_length=250 ,verbose_name="text du background")
