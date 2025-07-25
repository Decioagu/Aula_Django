from django.views.generic import ListView

from core.models import Produto

#31 Classe de gerenciamento da página inicial
class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    paginate_by = 3 # Define a quantidade de itens por pagina
    ordering = 'id' # Define a ordem dos itens na paginação

