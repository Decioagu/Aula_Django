from django.urls import path

from .views import IndexView

#14 Definindo as URLs do app core
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

