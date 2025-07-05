"""djangoum2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#17 Gerecia as URLs das aplicações
urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Geek University'
admin.site.site_title = 'Evolua seu lado geek!'
admin.site.index_title = 'Sistema de Gerenciamento de Posts'

'''
- admin.site.site_header: Define o título principal exibido no cabeçalho da interface do Django Admin.
    Exemplo de uso acima:
    Exibirá "Geek University" no topo da tela do admin, substituindo o padrão.

- admin.site.site_title: Define o título da aba do navegador (HTML <title>) quando a interface do admin está aberta.
    Exemplo de uso acima:
    Mostrará "Evolua seu lado geek!" na aba do navegador.

- admin.site.index_title: Define o título da página de índice (a tela principal do admin que aparece após o login).
    Exemplo de uso acima:
    Mostrará "Sistema de Gerenciamento de Posts" como o título da página inicial do admin.
'''