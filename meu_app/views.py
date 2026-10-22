from django.shortcuts import render
from django.contrib import messages

from meu_app.forms import ProdutoForm
from django.shortcuts import get_object_or_404
from meu_app.models import Produto
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.



@login_required
def index(request):
    return render(request, 'index.html')

def cadastro_produto(request):
    formulario = ProdutoForm(request.POST or None)
    if request.method == "POST":
        if formulario.is_valid():
            Produto.objects.create(
                nome=formulario.cleaned_data["nome"].upper(),
                descricao=formulario.cleaned_data["descricao"],
                preco=formulario.cleaned_data["preco"],
                quantidade=formulario.cleaned_data["quantidade"],
            )
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect('listar_produtos')
        else:
            messages.error(request, "Erro ao cadastrar o produto. Verifique os dados e tente novamente.")
        return render(request, "cadastro_produto.html", {"formulario": formulario})
    return render(request, "cadastro_produto.html", {"formulario": formulario})

def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    formulario = ProdutoForm(request.POST or None, instance=produto)
    mensagem = None
    if request.method == "POST":
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect('listar_produtos')
        else:
            messages.error(request, "Erro ao atualizar o produto. Verifique os dados e tente novamente.")
    return render(request, "editar_produto.html", {"mensagem": mensagem, "formulario": formulario, "produto": produto})

def sair(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('index')

def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    produto.ativo = False
    produto.save()
      
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

    messages.success(request, "Produto removido com sucesso!")
    return redirect('listar_produtos')

def listar_produtos(request):
    produtos = Produto.objects.all()
    produtos = produtos.filter(ativo=True)
    search = request.GET.get("search", "")
    if search:
        produtos = produtos.filter(nome__icontains=search)

    if request.GET.get("ordem") == "crescente":
        produtos = produtos.order_by("nome")
    elif request.GET.get("ordem") == "decrescente":
        produtos = produtos.order_by("-nome")

    dados = {
        "produtos": produtos,}
    return render(request, "listar_produtos.html", {"dados": dados})
