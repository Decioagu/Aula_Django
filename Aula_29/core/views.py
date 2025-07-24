from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from core.models import Produto

#28 Classe de gerenciamento da página inicial
class IndexView(ListView):
    models = Produto # Nome do modelo
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos' # Nome da variável no template

#28 Classe de criação de produtos
class CreateProdutoView(CreateView):
    model = Produto # Nome do modelo
    template_name = 'produto_form.html' ### template
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index') # Redirecionamento para a página inicial

#28 Classe de edição de produtos
class UpdateProdutoView(UpdateView):
    model = Produto # Nome do modelo
    template_name = 'produto_form.html' ### template
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

#28 Classe de exclusão de produtos
class DeleteProdutoView(DeleteView):
    model = Produto # Nome do modelo
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
