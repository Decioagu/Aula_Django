"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from core.views import index, contato, produto, error404, error500 #08 Importando as views do core (app)
from django.conf.urls import handler404, handler500 #08 Importando os manipuladores de erro

urlpatterns = [
    path('admin/', admin.site.urls), #07 Rota para o Django Admin
    path('', index, name='index'),  #07 Rota para a página inicial
    path('contato/', contato, name='contato'),  #07 Rota para a página de contato
    path('produto/<int:id>/', produto, name='produto'),  #07 Rota para a página de produto/id
]

    # path(url, view, views.py,  templates{% url 'NOME' %})

# Tratamento de erros personalizados somente com DEBUG=False em "sttings.py"
handler404 = error404 #08 Personalizados tratar erros por pagina própria
handler500 = error500 #08 Personalizados tratar erros por pagina própria