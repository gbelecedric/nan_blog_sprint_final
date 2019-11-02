from django.shortcuts import render
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
    
    nbr_vue = Visitor_Infos_user.objects.filter(page_visited="/details/{}".format(titre)).count()
    print(nbr_vue)
    # lien = Link.objects.filter(status=True).order_by('-date_add')
    # image = Background.objects.filter(status=True).order_by('-date_add')
    maxim = Article.objects.filter(status=True).order_by('-nb_like') 
 
    

    archive = Categorie.objects.filter(status=True).order_by('-date_add') 
    alltag = Tag.objects.filter(status=True)
    article = Article.objects.get(titre_slug=titre)
    categorie = Categorie.objects.filter(status=True).order_by('-date_add')
    tag = article.tag_name.all()
    comment = Commentaire.objects.filter(article_id = article).order_by('-date_add')
    comment7 = Commentaire.objects.filter(article_id = article).order_by('-date_add')[5::]
   

    data={
        "nbr_vue":nbr_vue,
    
        
    
        'verif':len(comment7),
        # 'lien':lien,
        # 'image':image,
        'alltag':alltag,
        'archive':archive,
        'tag':tag,
        'categorie':categorie,
        'comment':comment,
        'article':article,
        'maxim':maxim,
    }
    return render(request, 'pages/blog/blog-detail.html',data)

def categorie(request, titre):
    
    data={
        'titre': titre
    }
    return render(request, 'pages/blog/category.html',data)

def dashbord(request):
    user = request.user
    print(user.username)
    print('***************')
    # userpost = Article.objects.filter(auteur=user)
    # b = Article.objects.filter(auteur=user, status=True)
    # c = Article.objects.filter(auteur=user, status=False)
    # bb = b.count()
    # a = userpost.count()
    # cc = c.count()
    # print('++++++++++++++++++',a)
    # print('++++++++++++++++++',bb,cc)
    
    # data={
    #     'userpost': userpost,
    #     'a': a,
    #     'bb': bb,
    #     'cc': cc,
    # }
    return render(request, 'pages/dashbord/dashbord.html', data)

def dashpost(request):
    user = request.user
    print('+++++++++++++++',user,'+++++++++++++++++')
    userarticle = User.objects.all()
    #print(userarticle.ctegorieuser.articles.all)
    userpost = Article.objects.filter(auteur=user)
    

    data={
        'userarticle': userarticle,
        'userpost': userpost,
       
    }

    return render(request, 'pages/dashbord/posts.html', data)

def dashdetail(request):
    
        
    data = {
       
    }
    return render(request, 'pages/dashbord/dashdetail.html',data)

def error(request):
    
    data={}
    return render(request, 'pages/dashbord/page_404.html',data)

def ajout(request):
    
    data={}
    return render(request, 'pages/dashbord/ajout.html',data)


