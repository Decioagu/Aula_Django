from django.contrib import admin

from core.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor') # Exibe o título e a (Método auxiliar _autor) do post
    exclude = ['autor',] # Exclui o campo 'autor' do formulário de edição

    # Método auxiliar para exibir o nome completo do autor
    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}' 

    # Filtra os posts para exibir apenas os do usuário logado (autor ForeignKey do models.py)
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request) # Obtém o queryset padrão
        return qs.filter(autor=request.user) 
    
    # Define automaticamente o autor como usuário atual, garantindo que o campo autor não seja exposto
    def save_model(self, request, obj, form, change):
        obj.autor = request.user # Define o autor como o usuário logado (funciona em conjunto com exclude = ['autor'])
        super().save_model(request, obj, form, change) # Chama o método pai para salvar o objeto