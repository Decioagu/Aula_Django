from django.contrib import admin

from core.models import Produto, Cliente

''' 
    Configurar a interface administrativa do Django Admin 
    Usar a interface administrativa do Django para manipulação do Banco de Dados
    Registrar os modelos Produto e Cliente para que possam ser gerenciados no Django Admin
'''

#07 Cabeçalho do Registro do modelo Produto no Django Admin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

#07 Cabeçalho do Registro do modelo Cliente no Django Admin
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin) #07 Registro do modelo Produto no Django Admin
admin.site.register(Cliente, ClienteAdmin) #07 Registro do modelo Cliente no Django Admin
