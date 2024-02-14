import json
import asyncio
import random


from channels.generic.websocket import AsyncWebsocketConsumer


from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Canvas1Consumer(AsyncWebsocketConsumer):
    ball_position = {'x': 250, 'y': 250}

    async def connect(self):
        await self.channel_layer.group_add("single_room", self.channel_name)
        await self.accept()

        await self.send(text_data=json.dumps({'type': 'ball_position', 'position': self.ball_position}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("single_room", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']

        if command == 'move_up':
            self.ball_position['y'] -= 10
        elif command == 'move_down':
            self.ball_position['y'] += 10
        elif command == 'move_left':
            self.ball_position['x'] -= 10
        elif command == 'move_right':
            self.ball_position['x'] += 10

        await self.channel_layer.group_send(
            "single_room",
            {
                'type': 'send_ball_position',
                'position': self.ball_position
            }
        )

    async def send_ball_position(self, event):
        position = event['position']
        
        await self.send(text_data=json.dumps({'type': 'ball_position', 'position': position}))
