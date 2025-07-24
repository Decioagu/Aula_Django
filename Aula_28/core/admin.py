from django.contrib import admin

from .models import Produto

#28 Registrando o modelo Produto no Django Admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
