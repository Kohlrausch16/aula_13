from django.contrib import admin

from meu_app.models import Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "quantidade", "ativo", "data_cadastro")
    list_filter = ("ativo",)
    search_fields = ("nome", "descricao")