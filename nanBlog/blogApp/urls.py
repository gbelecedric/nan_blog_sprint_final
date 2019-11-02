from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:titre>', views.detail, name='detail'),
    path('category/<str:titre>', views.categorie, name='categorie'),

    path('dashbord', views.dashbord, name='dashbord'),
    path('dashpost', views.dashpost, name='dashpost'),
    path('dashdetail/', views.dashdetail, name='dashdetail'),
    path('error', views.error, name='error'),
    path('ajout', views.ajout, name='ajout'),

    path('postsAtt', views.postsAtt, name='postsAtt'),
    path('postsV', views.postsV, name='postsV'),

]
  