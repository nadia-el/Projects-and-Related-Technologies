from channels.generic.websocket import JsonWebsocketConsumer
# from time import sleep
# from django.core.cache import cache
from asgiref.sync import async_to_sync


class DemoConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
    def receive_json(self, json_data):
        async_to_sync(self.channel_layer.send)(self.channel_name,
                                    # The channel name of
                                    # the channel who's method corresponding
                                    # to type will be invoked
                                    # the method will be named as
                                    # . replaced with _ in type argument
                                    {'type': 'somemethod',
                                    # all other keys and values will go as
                                    # keyword arguments
                                    'text':'this is my custom msg'})

    def disconnect(self, close_code):
        self.send_json({'message': "Goodbye!"})

    def somemethod(self, message):
        print(message)