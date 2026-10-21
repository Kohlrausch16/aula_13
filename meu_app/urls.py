from django.urls import path
from meu_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
]
