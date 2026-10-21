from django.shortcuts import render

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
