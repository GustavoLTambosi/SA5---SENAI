from django.shortcuts import render, redirect
from app_cliente.models import Cliente

def home(request):
    return render(request, 'app_cliente/home.html')

def clientes(request):
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.email = request.POST.get('email')
    novo_cliente.telefone = request.POST.get('telefone')
    novo_cliente.save()
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'app_cliente/clientes.html', clientes)

def lista(request):
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'app_cliente/clientes.html', clientes)
