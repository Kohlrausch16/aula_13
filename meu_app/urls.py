from django.urls import path
from meu_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('remover_produto/<int:produto_id>/', views.remover_produto, name='remover_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
]
