# coding: utf-8
from giffy_bot import bot
from giffy_bot.celery import app
from giffy_bot.serializers import MessageSerializer


def display_help(message):
    # todo: prettify this shit
    text = """
    help - Display this help message.
    register - Make the bot remember your account so that it could save your gifs. Without this, it won't serve save and 
    post commands for you.
    save - Save last posted gif with given name.
    post - Post a gif by name.
    """
    bot.sendMessage(message.chat_id, text)


@app.task
def handle_message(request):
    message = MessageSerializer(request)
    if message.command == 'help':
        display_help(message)
