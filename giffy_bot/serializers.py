# coding: utf-8
import re

SUPPORTED_COMMANDS = ['help', 'pidoreg', 'pidorstats', 'pidor']


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
        try:
            return self.message['text']
        except KeyError:
            return None

    @property
    def from_id(self):
        return self.message['from']['id']

    @property
    def from_first_name(self):
        return self.message['from']['first_name']

    @property
    def command(self):
        text = self.text
        if text:
            expr = '/({})(?:^@pidor2bot$)?'.format('|'.join(SUPPORTED_COMMANDS))
            try:
                return re.match(expr, text).group(1)
            except IndexError:
                pass
        return None
