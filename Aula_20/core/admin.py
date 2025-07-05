from django.contrib import admin

from .models import Chassi, Carro, Montadora

#20 Registrando os modelos no Django Admin
@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

#20 Registrando os modelos no Django Admin
@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)

#20 Registrando os modelos no Django Admin
@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')

    #20 Método para exibir os motoristas associados ao carro
    def get_motoristas(self, obj): 
        return ', '.join([m.username for m in obj.motoristas.all()]) # string separados por vírgula

    get_motoristas.short_description = 'Motoristas' #20 "short_description" descrição do campo no Django Admin
