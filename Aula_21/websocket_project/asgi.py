"""
ASGI config for websocket_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_project.settings')

application = ProtocolTypeRouter({ # Define o tipo de protocolo
    "http": get_asgi_application(), # para requisições HTTP normais
    "websocket": AuthMiddlewareStack( # para conexões WebSocket
        URLRouter(
            routing.websocket_urlpatterns # Define as rotas WebSocket para o Chat
        )
    ),
})

'''
ProtocolTypeRouter: define tipo de protocolo esta chegando (HTTP, WebSocket,  MQTT e  outros).
AuthMiddlewareStack: para autenticação do usuário no WebSocket.
URLRouter: para fazer o roteamento interno para os consumers.
'''