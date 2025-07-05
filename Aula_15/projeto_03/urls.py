"""
URL configuration for projeto_03 project.

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
from django.urls import path, include #14 Importando o módulo path e include do Django

from django.conf.urls.static import static #14
from django.conf import settings #14

#14 Gerecia as URLs das aplicações
urlpatterns = [
    path('admin/', admin.site.urls), #14 Rota para o Django Admin
    path('', include('core.core_urls')), #14 Incluindo as URLs do app core (aplicação)
]
#14 Verifica se o modo DEBUG está ativado
if settings.DEBUG:  
    #14 Adiciona as URLs de mídia ao urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
