# coding: utf-8
from django.conf.urls import url

from giffy_bot.views import RouterView

app_name = 'router'
urlpatterns = [
    url(r'bot/', RouterView.as_view())
]
