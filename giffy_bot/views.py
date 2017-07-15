# coding: utf-8
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):

    def get(self, request, **kwargs):
        return Response({'res': 'hello world'})


class GiffyBot(APIView):

    def get(self, request, **kwargs):
        return ''
