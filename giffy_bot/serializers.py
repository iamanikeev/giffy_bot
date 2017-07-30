# coding: utf-8

SUPPORTED_COMMANDS = ['help', 'register', 'save', 'post']


class MessageSerializer:
    """
    This class has nothing to do with Django serializer. It is just a helper to get Telegram message properties
    """
    def __init__(self, message_object):
        self.message = message_object['message']
        self.id = self.message['message_id']

    @property
    def chat_id(self):
        return self.message['chat']['id']

    @property
    def text(self):
        return self.message['text']

    @property
    def from_id(self):
        return self.message['from']['id']

    @property
    def from_first_name(self):
        return self.message['from']['first_name']

    @property
    def is_command(self):
        return self.text.startswith('/') and self.text.strip('/') in SUPPORTED_COMMANDS

    @property
    def command(self):
        return self.text.strip('/')
