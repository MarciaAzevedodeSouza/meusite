from django.shortcuts import render

from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def login(request):
    if request.method == "GET":
        return render(request,'usuarios/login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user =authenticate(username = username,password = senha)

        if user:
            login_django(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('E-mail ou senha invalida')
        
def cadastro(resquest):
    if resquest.method == 'GET':
        return render(resquest,'usuarios/cadastro.html')
    else:
        username = resquest.POST.get('email')
        email =resquest.POST.get('email')
        password = resquest.POST.get('senha')
        first_name = resquest.POST.get('nome')

        user =User.objects.filter(username=username).first()

        if user:
         return HttpResponse("usuario ja existente")
        else:  
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()
            return HttpResponse("usuario cadastrado com sucesso")    

def home(request):
    return render(request, 'Usuarios/home.html')