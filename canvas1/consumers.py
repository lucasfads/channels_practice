import json

from channels.generic.websocket import AsyncWebsocketConsumer


class Canvas1Consumer(AsyncWebsocketConsumer):
    async def connect(self):
       	# Join room group
        await self.channel_layer.group_add("single_room", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard("single_room", self.channel_name)

    # # Receive message from WebSocket
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]

    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         "single_room", {"type": "canvas1.message", "message": message}
    #     )

    # # Receive message from room group
    # async def canvas1_message(self, event):
    #     message = event["message"]

    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({"message": message}))
