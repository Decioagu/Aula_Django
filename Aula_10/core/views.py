from django.shortcuts import render

#10 Conexão entre HTML e Banco de Dados
def index(request):
    context = {
    'texto': 'Aula 10 - Django',
    }
    return render(request, 'index.html', context=context)

#10 Conexão entre HTML e Banco de Dados
def contato(request):
    context = {
        'texto': 'Aula 10 - Django',
    }
    return render(request, 'contato.html', context=context)

#10 Conexão entre HTML e Banco de Dados
def produto(request):
    context = {
        'texto': 'Aula 10 - Django',
    }
    return render(request, 'produto.html', context=context)