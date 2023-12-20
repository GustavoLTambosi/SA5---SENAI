from django.contrib import admin
from django.urls import path
from app_cliente import views

urlpatterns = [
    path('', views.home, name="home"),
    path('clientes/', views.clientes, name="listagem_clientes"),
    path('lista/', views.lista, name="lista"),
]
