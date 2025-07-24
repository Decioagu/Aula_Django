from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from core.forms import ProdutoForm  # Vamos criar o form abaixo

# Página inicial - listar produtos
def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

# Criar produto
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form})

# Editar produto
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})

# Deletar produto
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('index')
    return render(request, 'produto_del.html', {'produto': produto})
