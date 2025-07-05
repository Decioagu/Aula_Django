from django.contrib import admin

from core.models import Cargo, Servico, Equipe
#14 Registrando o modelo Cargo no Django Admin
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

#14 Registrando o modelo Servico no Django Admin
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

#14 Registrando o modelo Equipe no Django Admin
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')
