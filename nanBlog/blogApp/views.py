from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
import json
# Create your views here.

def home(request):
     
    
    data={}

    return render(request, 'pages/blog/index.html',data)

def detail(request , titre):

    data = {
        "titre": titre
    }
    
    return render(request, 'pages/blog/single.html',data)

def categorie(request, titre):
    
    data={
        'titre': titre
    }
    return render(request, 'pages/blog/category.html',data)

def dashbord(request):
    user = request.user
    print(user.username)
    print('***************')
    userpost = Article.objects.filter(auteur=user)
    b = Article.objects.filter(auteur=user, status=True)
    c = Article.objects.filter(auteur=user, status=False)
    bb = b.count()
    a = userpost.count()
    cc = c.count()
    print('++++++++++++++++++',a)
    print('++++++++++++++++++',bb,cc)
    
    data={
        'userpost': userpost,
        'a': a,
        'bb': bb,
        'cc': cc,
    }
    return render(request, 'pages/dashbord/dashbord.html', data)

def dashpost(request):
    user = request.user
    print('+++++++++++++++',user,'+++++++++++++++++')
    userarticle = User.objects.all()
    #print(userarticle.ctegorieuser.articles.all)
    userpost = Article.objects.filter(auteur=user)
    #article = get_object_or_404(Article, categorie=cat, id=id)
    

    data={
        'userarticle': userarticle,
        'userpost': userpost,
       
    }

    return render(request, 'pages/dashbord/posts.html', data)

def dashdetail(request):
    #article = get_object_or_404(Article, pk=id)
    # article = Article.objects.filter(auteur=autor)[:1].get()

    # data = {
    #     'article': article,
    # }
    return render(request, 'pages/dashbord/dashdetail.html')

def error(request):
    
    data={}
    return render(request, 'pages/dashbord/page_404.html',data)

def ajout(request):
    
    data={}
    return render(request, 'pages/dashbord/ajout.html',data)

def postsAtt(request):
    user = request.user
    userpost = Article.objects.filter(auteur=user)
    c = Article.objects.filter(auteur=user, status=False)
    a = userpost.count()
    cc = c.count()
    print('++++++++++++++++++',a)
    
    data={
        'userpost': userpost,
        'a': a,
        'cc': cc,
        'c': c,
    }
    return render(request, 'pages/dashbord/postsAtt.html',data)

def postsV(request):
    user = request.user
    userpost = Article.objects.filter(auteur=user)
    b = Article.objects.filter(auteur=user, status=True)
    bb = b.count()
    a = userpost.count()
    print('++++++++++++++++++',a)
    
    data={
        'userpost': userpost,
        'a': a,
        'bb': bb,
        'b': b,
    }
    
    return render(request, 'pages/dashbord/postsV.html',data)


