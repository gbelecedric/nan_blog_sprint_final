from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('archive', views.archive, name='archive'),
    path('single', views.single, name='single'),
    path('category', views.category, name='category'),

    path('dashbord', views.dashbord, name='dashbord'),
    path('dashpost', views.dashpost, name='dashpost'),
    path('dashdetail', views.dashdetail, name='dashdetail'),
    path('error', views.error, name='error'),
    path('ajout', views.ajout, name='ajout'),

]
  