from django.shortcuts import get_object_or_404, redirect, render
from meu_app.forms import ProdutoForm
from meu_app.models import Produto


# Create your views here.


def index(request):

    return render(request, "index.html")

def cadastro_produto(request):
    formulario = ProdutoForm(request.POST or None)
    mensagem = None
    if request.method == "POST":
        if formulario.is_valid():
            Produto.objects.create(
                nome=formulario.cleaned_data["nome"].upper(),
                descricao=formulario.cleaned_data["descricao"],
                preco=formulario.cleaned_data["preco"],
                quantidade=formulario.cleaned_data["quantidade"],
            )
            mensagem = "Produto cadastrado com sucesso!"
            formulario = ProdutoForm()
        else:
            mensagem = "Erro ao cadastrar o produto. Verifique os dados e tente novamente."
    return render(request, "cadastro_produto.html", {"mensagem": mensagem, "formulario": formulario})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    formulario = ProdutoForm(request.POST or None, initial={
        "nome": produto.nome,
        "descricao": produto.descricao,
        "preco": produto.preco,
        "quantidade": produto.quantidade,
    })
    mensagem = None
    if request.method == "POST":
        if formulario.is_valid():
            produto.nome = formulario.cleaned_data["nome"].upper()
            produto.descricao = formulario.cleaned_data["descricao"]
            produto.preco = formulario.cleaned_data["preco"]
            produto.quantidade = formulario.cleaned_data["quantidade"]
            produto.save()
            return redirect('listar_produtos')

        else:
            mensagem = "Erro ao atualizar o produto. Verifique os dados e tente novamente."
    return render(request, "editar_produto.html", {"mensagem": mensagem, "formulario": formulario, "produto": produto})


def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    produto.ativo = False
    produto.save()

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
