from django.shortcuts import render

# Create your views here.

def home(request):
     
    
    data={}

    return render(request, 'pages/blog/index.html',data)

def single(request):
     
    
    data={}

    return render(request, 'pages/blog/single.html',data)



def archive(request):
     
    
    data={}

    return render(request, 'pages/blog/archive.html',data)

def category(request):
     
    
    data={}

    return render(request, 'pages/blog/category.html',data)

def dashbord(request):
    # user = request.user
    # print(user.username)
    # print('***************')
    # userpost = Article.objects.filter(nom=user)
    # b = Article.objects.filter(nom=user, status=True)
    # c = Article.objects.filter(nom=user, status=False)
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
    return render(request, 'pages/dashbord/dashbord.html')

def dashpost(request):
    # user = request.user
    # print('+++++++++++++++',user,'+++++++++++++++++')
    # userarticle = User.objects.all()
    # #print(userarticle.ctegorieuser.articles.all)
    # userpost = Article.objects.filter(nom=user)
    

    # data={
    #     'userarticle': userarticle,
    #     'userpost': userpost,
       
    # }

    return render(request, 'pages/dashbord/posts.html')

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


