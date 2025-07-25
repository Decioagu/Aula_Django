from django.contrib import admin

from core.models import Filmes

#34 Registrando o modelo Produto no Django Admin
@admin.register(Filmes) # Decorador para registrar o modelo Produto
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'genero', 'ano') # lista de campos a serem exibidos na interface administrativa

# OU

#34 Registro do modelo Produto no Django Admin
# admin.site.register(Filmes) # Não exibe lista de campos