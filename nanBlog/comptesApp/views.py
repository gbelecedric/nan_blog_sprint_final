import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import *



def register(request):
    return render(request, 'pages/comptes/register.html')


def registerApi(request):

    if request.method == 'POST' :
        
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        image = request.FILES['file']
        # image = request.FILES.get('file')
        print('vvgsgsgsggs',image)
        is_email=False       
        Min_Length = 8
        

        try:
            
            if firstname != None and lastname != None and username != None :

                try:
                    validate_email(email)
                    is_email=True
                except:
                    data = {
                        'success':False,
                        'message':'Email is not valide'
                    }

                if is_email :
                        
                    try:

                        user_dup = User.objects.filter(email=email)
                        
                        if user_dup.exists():
                            
                            data={
                                'success':False,
                                'message': 'Ce mail existe Deja dans la BD'
                            }

                        
                        elif image == None:
                            data = {
                                'success':False,
                                'message': 'Verifie votre champ Image'
                            }
                        
                        elif len(password) < Min_Length:
                            data = {
                                'success':False,
                                'message': 'Mot de passe doit etre au minimum 8 chiffres'
                            }

                        elif password == password2 and (password is not None and password2 is not None):
                            user = User(username = username, first_name = firstname, last_name = lastname, email = email)
                            user.save()
                            user.profile.imageprofile = image
                            print(user.profile.imageprofile)
                            user.save()
                            # print("UUUUUUU", user.save())
                            user.password = password
                            user.set_password(user.password)
                            user.save()

                            data={
                                'success':True,
                                'message': 'Enregistrement effectue avec succes'
                            }

                        else:
                            data={
                                'success':False,
                                'message':'Mot de passe ne sont pas meme'
                            }

                    except:
                        pass

                        # data={
                        #     'success':False,
                        #     'message':'Verifier les Champs'
                        # }

        except:
            data = {
                'success':False,
                'message':'Verifier les Champs SVP'
            }
            
    else:
        data={
            'success':False,
            'message':'Tous les Champs sont Vides'
        }
    
    return JsonResponse(data, safe=False)



def login_visiteur(request):
    return render(request, 'pages/comptes/login.html')


def loginsApi(request):

    postdata = json.loads(request.body.decode('utf-8'))
    username=postdata['username']
    password=postdata['password']
    print("###################user", username) 
    print("###################user", password) 
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        print("###################user is login")   
        login(request, user)

        data={
            'success':True,
            'message':'connecte'
        }

    else:

        data={
            'success':False,
            'message':'Erro Login...'
        }
    return JsonResponse(data, safe=False)


def logout_view(request):
    logout(request)
    return redirect('blog:home')


@login_required(login_url='comptes:login_visit')
def element(request):

    # u_form = UserUpdateForm(instance = request.user)
    # p_form = ProfileUpdateForm(instance = request.user.profile)


    # u_form = {
    #     # "fullname": request.user.fullname, 
    #     "username": request.user.username,
    #     "email": request.user.email,
    # }



    context = {
        # 'u_form' : u_form,
        # 'p_form' : p_form
    }
    
    return render(request, 'pages/profil/index.html',context)


def modif_profil(request):

    data={}
    return render(request, 'pages/comptes/modif_profil.html',data)


# def modifprofilapi(request):

#     if request.method == 'POST' :
#         u_form = UserUpdateForm(request.POST, instance = request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
            
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
           
#             data={
#                 'success':True,
#                 'message': 'Enregistrement effectue avec succes'
#             }


#     return JsonResponse(data, safe=False)












