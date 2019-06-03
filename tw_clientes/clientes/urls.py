from django.urls import path
from .views import *

urlpatterns = [
    path('clientes', listar_clientes, name='listar_cliente'),
    path('clientes/cadastrar', inserir_cliente, name='cadastrar_cliente'),
]