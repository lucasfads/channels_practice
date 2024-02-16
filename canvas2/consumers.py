import json
import asyncio
import random


from channels.generic.websocket import AsyncWebsocketConsumer


from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Canvas2Consumer(AsyncWebsocketConsumer):
    ball_position = {'x': 250, 'y': 250}
    moving_up = True

    async def connect(self):
        await self.channel_layer.group_add("single_room", self.channel_name)
        await self.accept()
        self.ball_move_task = asyncio.create_task(self.move_ball_auto())

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("single_room", self.channel_name)
        self.ball_move_task.cancel()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']

        if command == 'move_left':
            self.ball_position['x'] -= 10
        elif command == 'move_right':
            self.ball_position['x'] += 10

        await self.update_ball_position()

    async def move_ball_auto(self):
        while True:
            if self.moving_up:
                self.ball_position['y'] -= 1
                if self.ball_position['y'] <= 0:
                    self.moving_up = False
            else:
                self.ball_position['y'] += 1
                if self.ball_position['y'] >= 500:
                    self.moving_up = True

            await self.update_ball_position()
            await asyncio.sleep(0.01)

    async def update_ball_position(self):
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
