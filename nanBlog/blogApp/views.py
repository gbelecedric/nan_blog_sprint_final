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