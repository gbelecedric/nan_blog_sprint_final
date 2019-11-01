from django.shortcuts import render

# Create your views here.
def contact(request):
     
    
    data={}

    return render(request, 'pages/contact/contact.html',data)