from django import forms
from django.core.mail.message import EmailMessage


""" 
    ContatoForm: 
        Criação de formulários HTML com Django, para envio de e-mails 
        após cadastro de produtos, sem vinculo ao Banco de Dados.
        Resumo: Disparo automático de e-mails após cadastro de produtos.

    ProdutoModelForm: 
        Criação de formulários HTML com Django, para cadastro de produtos
        no Banco de Dados, utilizando o modelo Produto.
"""

#15 - Formulário SEM integração ao Banco de Dados (forms.Form = definição de modelo manual)
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    #15 Método para enviar o e-mail com os dados do formulário
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        '''self.cleaned_data[...] é um dicionário que o Django cria após validar os dados enviados no formulário'''

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        #15 Enviando o e-mail
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()
