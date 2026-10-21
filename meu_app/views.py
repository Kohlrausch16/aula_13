from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def sair(request):
    return redirect('login')

def cadastrar_usuario(request):
    
    formulario_de_usuario = UserCreationForm()

    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            #nome_usuario = formulario.cleaned_data['username']
            #mensagem = f'Usuário {nome_usuario} cadastrado com sucesso!'
            #messages.success(request, mensagem)

            return redirect('cadastrar_usuario')
    else: 
        formulario = UserCreationForm()


    dados = {
        'formulario': formulario_de_usuario
    }
       
    return render(request, 'cadastrar_usuario.html', dados)