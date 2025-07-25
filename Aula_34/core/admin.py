from django.contrib import admin

from core.models import AditivosNutritivos
from core.models import AditivosNutritivosPicole
from core.models import Conservantes
from core.models import ConservantesPicole
from core.models import Ingredientes
from core.models import IngredientesPicole
from core.models import Lotes
from core.models import LotesNotaFiscal
from core.models import NotasFiscais
from core.models import Picoles
from core.models import Revendedores
from core.models import Sabores
from core.models import TiposEmbalagem 
from core.models import TiposPicole 

# Register your models here.
admin.site.register(AditivosNutritivos)
admin.site.register(AditivosNutritivosPicole)
admin.site.register(Conservantes)
admin.site.register(ConservantesPicole) 
admin.site.register(Ingredientes)
admin.site.register(IngredientesPicole) 
admin.site.register(Lotes)
admin.site.register(LotesNotaFiscal)
admin.site.register(NotasFiscais)
admin.site.register(Picoles)
admin.site.register(Revendedores)
admin.site.register(Sabores)
admin.site.register(TiposEmbalagem)
admin.site.register(TiposPicole)    


