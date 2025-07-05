from django.urls import re_path #21 expresão regular

from .consumers import ChatConsumer

#21 Define as rotas para o WebSocket
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer), #21 Define a rota com o nome da sala como parâmetro
]
