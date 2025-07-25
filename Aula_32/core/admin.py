from django.contrib import admin

from core.models import Produto

#31 Registrando o modelo Produto no Django Admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

