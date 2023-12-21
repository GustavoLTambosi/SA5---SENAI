from django.shortcuts import render, redirect, get_object_or_404
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

def excluir(request, id_cliente):
    excluir_cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    excluir_cliente.delete()
    return redirect('lista')

def atualizar(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.POST:
        cliente.nome = request.POST.get("nome")
        cliente.email = request.POST.get("email")
        cliente.telefone = request.POST.get("telefone")
        cliente.save()
        return redirect('lista')
    return render(request, "app_cliente/atualizar.html", context={"cliente": cliente})

def pesquisar(request):
    nome = request.GET.get("nome")
    if nome:
        cliente = Cliente.objects.filter(nome__icontains=nome)
    else:
        cliente = Cliente.objects.all()

    return render(request, "app_cliente/pesquisar.html", context={"cliente": cliente})
