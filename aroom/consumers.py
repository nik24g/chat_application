import json
from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.consumer import AsyncConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

# additon add
# class EchoConsumer(AsyncConsumer):
#     channel_layer_alias = "echo_alias"
#
#     async def websocket_connect(self, event):
#         await self.send({
#             "type": "websocket.accept",
#         })
#
#     async def websocket_receive(self, event):
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })
#
# class MyConsumer(AsyncWebsocketConsumer):
#     groups = ["broadcast"]
#
#     async def connect(self):
#         # Called on connection.
#         # To accept the connection call:
#         await self.accept()
#         # Or accept the connection and specify a chosen subprotocol.
#         # A list of subprotocols specified by the connecting client
#         # will be available in self.scope['subprotocols']
#         await self.accept("subprotocol")
#         # To reject the connection, call:
#         await self.close()
#
#     async def receive(self, text_data=None, bytes_data=None):
#         # Called with either text_data or bytes_data for each frame
#         # You can call:
#         await self.send(text_data="Hello world!")
#         # Or, to send a binary frame:
#         await self.send(bytes_data="Hello world!")
#         # Want to force-close the connection? Call:
#         await self.close()
#         # Or add a custom WebSocket error code!
#         await self.close(code=4123)
#
#     async def disconnect(self, close_code):
#         # Called when the socket closes
#         pass

