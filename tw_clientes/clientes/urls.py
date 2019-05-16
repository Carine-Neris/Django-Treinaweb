from django.urls import path
from .views import listar_clientes, listar_produtos,home

urlpatterns = [
    path('', home, name='home'),
    path('clientes', listar_clientes, name='listar_cliente'),
    path('produtos', listar_produtos, name='listar_produto'),
]