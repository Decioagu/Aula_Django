from django.shortcuts import render

from core.models import Produto


def index(request):
    produtos = Produto.objects.all() #07 Obtém todos os produtos do banco de dados.

    # Renderiza a página inicial.
    context = {
        'curso': 'Programação Web com Django Framework', #07 Contexto para a página index.html
        'outro': 'Django é massa!', #07 Contexto para a página index.html
        'produtos': produtos #07 Contexto para a página index.html
    }
    return render(request, 'index.html', context)

def contato(request):
    # Renderiza a página de contato.
    return render(request, 'contato.html')

def produto(request, id): #07 Modifica a view produto para receber um parâmetro id
    # Renderiza a página de produto com o id fornecido.
    prod = Produto.objects.get(id=id) #07 Obtém o produto com o id fornecido

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)



