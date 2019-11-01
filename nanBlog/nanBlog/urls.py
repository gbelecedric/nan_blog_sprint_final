"""nanBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings

from django.conf.urls.static import static
from filebrowser.sites import site
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True , schema=schema)),
    path('', include('blogApp.urls')),
    path('comptes/', include('comptesApp.urls')),
    path('configuration/', include('configurationApp.urls')),
    path('contact/', include('contactApp.urls')),
    path('site/', include('siteApp.urls')),
    path('statistique/', include('statistiqueApp.urls')),
    path('apirest/', include('api_rest.urls')),
    # Tinymce
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
    # url(r'^accounts/', include('allauth.urls')),
    # path('api/', include('api.urls')),
    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
