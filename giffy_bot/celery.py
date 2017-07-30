# coding: utf-8
from __future__ import absolute_import, unicode_literals
import os


# set the default Django settings module for the 'celery' program.
from celery import Celery

# Oddly, this doesn't work with settings.production. Maybe because of star import in it
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('giffy_bot')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
