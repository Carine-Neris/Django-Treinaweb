from django.shortcuts import render
from .models import Cliente, Produto


def home(request):
    return render(request, 'index.html')


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produto.html', {'produtos': produtos})

