from django.urls import path
from meu_app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),    
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.sair, name='logout')
]