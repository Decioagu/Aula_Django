from django.shortcuts import render
from django.shortcuts import get_object_or_404 #08
from django.http import HttpResponse #08
from django.template import loader #08

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
    # prod = Produto.objects.get(id=id) #07 Obtém o produto com o id fornecido
    prod = get_object_or_404(Produto, id=id) #08 Obtém o produto com o id fornecido ou retorna 404 se não encontrado

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, erro): #08 Função para tratar erros 404
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)


def error500(request): #08 Função para tratar erros 500
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


