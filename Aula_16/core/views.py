from django.views.generic import FormView
from django.urls import reverse_lazy # Importa a função reverse_lazy para redirecionamento
from django.contrib import messages

from core.models import Servico, Equipe
from core.forms import ContatoForm

#15 Classe de gerenciamento da página inicial e formulário de contato (e-mail)
class IndexView(FormView):
    template_name = 'index.html' # Renderização da página inicial por meio do template HTML
    form_class = ContatoForm # Formulário de contato para envio de e-mail
    success_url = reverse_lazy('index') # URL de redirecionamento após o envio do formulário

    #15 Request: Adiciona os objetos de Servico e Equipe ao contexto
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) # Chama o contexto da superclasse
        context['servicos'] = Servico.objects.order_by('?').all() # Ordena os serviços aleatoriamente
        context['equipe'] = Equipe.objects.order_by('?').all() # Ordena os funcionários aleatoriamente
        return context

    #15 Formulário: Envia o e-mail com os dados do formulário
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs) # Redireciona para a URL de sucesso

    #15 Formulário: Exibe uma mensagem de erro do envio do e-mail
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs) # Redireciona para a URL de sucesso

'''
Class Based Views (CBVs) variáveis de uso automático no Django:
    Classes baseadas em views no Django (FormView, TemplateView, ListView etc.)

    "template_name =": define o caminho do template HTML que será renderizado quando a view for acessada.

    "form_class =": define qual classe de formulário (derivada de forms.Form ou forms.ModelForm) 
    será usada pela FormView. Você não precisa chamar ContatoForm() manualmente, pois o Django 
    faz isso por você.

    "success_url =": define para onde o usuário será redirecionado após o envio bem-sucedido do 
    formulário (isto é, quando form_valid() é chamado). A função reverse_lazy é usada no lugar 
    de reverse em arquivos onde o carregamento da URL precisa ser adiado até o momento da execução, 
    como em arquivos de configuração de views.

Vá até a "class IndexView(FormView):" e clique com Ctrl e 
botão direito do mouse e veja as opções disponíveis:
    Class Based Views já implementa métodos como "get_context_data", "form_valid" e 
    "form_invalid", que você pode sobrescrever para personalizar o comportamento da view.
    Essas classes são projetadas para serem fáceis de usar e personalizar, permitindo que 
    você se concentre na lógica de negócios em vez de na infraestrutura de views.
    Além disso, o Django fornece uma série de mixins que você pode usar para adicionar 
    funcionalidades adicionais às suas views, como autenticação, permissão, etc.    
'''