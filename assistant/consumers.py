import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .utils import run_assistant

class AssistantConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message == "start":
            # Run the voice assistant logic
            response = run_assistant()
            await self.send(text_data=json.dumps({
                'message': response
            }))
        else:
            await self.send(text_data=json.dumps({
                'message': "Unknown command."
            }))