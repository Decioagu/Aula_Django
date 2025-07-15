import json
from channels.generic.websocket import AsyncWebsocketConsumer

#22 Consumer para o Chat (navegador e aplicação)
class ChatConsumer(AsyncWebsocketConsumer):

    # Entrar na Sala
    async def connect(self):
        self.room_name = "sala"
        self.room_group_name = "chat_%s" % self.room_name

        # aguarda entrar na sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept() # aceita a conexão do WebSocket

    # Sair da Sala
    async def disconnect(self, close_code):
        # aguarda sair da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Enviara mensagem do WebSocket para a sala
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Enviar mensagem para o grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Recebe a mensagem do grupo da sala
    async def chat_message(self, event):
        message = event['message']

        # Enviar mensagem para WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
