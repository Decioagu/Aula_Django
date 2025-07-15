from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.routing import websocket_urlpatterns

#21 Gerencia rotas para o WebSocket
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

'''
ProtocolTypeRouter: define tipo de protocolo esta chegando (HTTP, WebSocket,  MQTT e  outros).
AuthMiddlewareStack: para autenticação do usuário no WebSocket.
URLRouter: para fazer o roteamento interno para os consumers.
'''