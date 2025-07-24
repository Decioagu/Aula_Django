from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'), # http://localhost:8000
    path('criar/', CreateProdutoView.as_view(), name='criar_produto'), # http://localhost:8000/add
    path('<int:pk>/editar/', UpdateProdutoView.as_view(), name='editar_produto'), # http://localhost:8000/1/update
    path('<int:pk>/deletar/', DeleteProdutoView.as_view(), name='deletar_produto'), # http://localhost:8000/1/delete
]

'''
Com uso de Class Based Views em viwes.py, é necessário uso de "pk" na url ao inves de "id":
Devido ao uso da biblioteca "class-based-views": from django.views.generic.edit import CreateView, UpdateView, DeleteView
    Essas classes vêm prontas para:
     - Buscar um objeto usando a chave primária (primary key).
     - E por padrão, o Django espera encontrar um parâmetro chamado pk na URL.
        - Internamente a busca na classe é feita assim:
            - NOME_CLASS_MODELO.objects.get(pk=self.kwargs['pk'])

Para uso de id seria necessario mudar o parâmetro pk para id, devido ao uso de "id" em viwes.py :

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Produto.objects.get(id=self.kwargs['id'])

O uso de <int:pk> é exigido devido ao uso de Class Based Views (UpdateView, DeleteView)
que dependem de um parâmetro pk para funcionar automaticamente

'''