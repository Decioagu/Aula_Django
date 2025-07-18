from django.urls import path

from chat.views import IndexView, SalaView

#21 Rotas das URLs das aplicações
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat/<str:nome_sala>/', SalaView.as_view(), name='sala'),
]
