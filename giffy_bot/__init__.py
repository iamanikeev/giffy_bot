# coding: utf-8
from __future__ import absolute_import, unicode_literals
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
import telepot
from django.conf import settings

from .celery import app as celery_app

# Load bot instance once during the app initialization
bot = telepot.Bot(settings.BOT_TOKEN)

__all__ = ['celery_app', 'bot']