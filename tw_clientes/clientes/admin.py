from django.contrib import admin
from .models import Cliente, Produto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'sexo', 'profissao', 'email',)


admin.site.register(Produto)

