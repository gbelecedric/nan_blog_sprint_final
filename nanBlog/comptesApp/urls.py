from django.urls import path
from . import views

app_name = 'comptes'
urlpatterns = [
    path("register/", views.register, name="register"),
    path("loginvisit/", views.login_visiteur, name="login_visit"),
    path("logout/", views.logout_view, name="logout_you"),
    path('profile/', views.element, name='profil_util'),
    path('modif_profil/', views.modif_profil, name='modif_profil'),
    path("registerapi", views.registerApi, name="registerapi"),
    path("loginapi", views.loginsApi, name="loginapi"),
]
  