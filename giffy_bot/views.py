# coding: utf-8
import logging
from contextlib import contextmanager

from rest_framework.response import Response
from rest_framework.views import APIView

from . import commands, bot
from giffy_bot.serializers import MessageSerializer


class RouterView(APIView):
    """
    Accepts the incoming http requests, handles message and returns ok response to Telegram server
    """

    http_method_names = ['post']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logger = logging.getLogger(__name__)

    def handle_failure(self, data, message, silent=False):
        text = '''
        I have no idea! I'm just a pidor bot! You can contact my <a href="tg://user?id=189581754">Creator</a> if you want
        '''
        self.logger.error('Bot could not handle this data: %s', data)
        if not silent:
            bot.sendMessage(message.chat_id, text, parse_mode='HTML')

    @contextmanager
    def handle_message(self, request):
        yield
        message = MessageSerializer(request.data)
        command = message.command
        if command:
            try:
                getattr(commands, command)(message)
            except AttributeError:
                self.handle_failure(request.data, message)
        else:
            self.handle_failure(request.data, message, silent=True)

    def post(self, request, *args, **kwargs):
        with self.handle_message(request):
            self.logger.info(request.data)
            return Response({'status': 'ok'})
