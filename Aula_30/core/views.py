from django.shortcuts import render
from django.core.paginator import Paginator
from core.models import Produto

def index_list_view(request):
    produtos = Produto.objects.all().order_by('id')  # Ordenação
    paginator = Paginator(produtos, 3)  # 3 produtos por página

    # Obtem o número da página
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)

    # Verifica se tem outras páginas
    is_paginated = page_obj.has_other_pages() 

    context = {
        'page_obj': page_obj, # Pagina atual
        'paginator': paginator, # Quantidade de items por página
        'is_paginated': is_paginated, # Verifica se tem outras páginas
    }

    return render(request, 'index.html', context)
