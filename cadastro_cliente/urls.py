from django.contrib import admin
from django.urls import path
from app_cliente import views

urlpatterns = [
    path('', views.home, name="home"),
    path('clientes/', views.clientes, name="listagem_clientes"),
    path('lista/', views.lista, name="lista"),
    path('excluir/<int:id_cliente>', views.excluir, name="excluir"),
    path('atualizar/<int:id_cliente>', views.atualizar, name="atualizar"),
    path('atualizar/<int:id_cliente>', views.atualizar, name="atualizar"),
    path('pesquisar/', views.pesquisar, name="pesquisar"),
]
