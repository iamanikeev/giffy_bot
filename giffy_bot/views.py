# coding: utf-8
import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import handle_message


class RouterView(APIView):
    """
    Accepts the incoming http requests, launches appropriate Celery task and replies to questioner server immediately
    """

    http_method_names = ['post']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logger = logging.getLogger(__name__)

    def post(self, request, *args, **kwargs):
        self.logger.info(request.data)
        handle_message.apply_async([request.data])
        return Response({'status': 'ok'})
