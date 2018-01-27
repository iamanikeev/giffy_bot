# coding: utf-8
from random import randint

from giffy_bot import bot
import time


GAME_RESPONSE_SEQUENCES = (
    (
        'Запускаем военные дроны... ',
        'Проводим спектральный анализ... ',
        'Вот же он! Пидор дня! *@Илюша*'
    ),
    (
        'Производим взлом базы данных ГИБДД...',
        'Анализируем биометрические данные...',
        "Нихуясебе новость, достойно [НГСа](http://ngs.ru/). Нынче пидор дня *@Илюша*"
    ),
    (
        'ВЖУХ, и ты пидор!',
        "Пидор дня *@Илюша*"
    )
)


def help(message):
    text = "*Pidorbot 2.0* способен вычислить *пидора* в чате, при помощи новейших разработок КГБ" \
           " в области машинного обучения и анализа данных!"
    bot.sendMessage(message.chat_id, text, parse_mode='Markdown')


def pidoreg(message):
    text = "Сорян, регистрация пока что не работает. " \
           "Да и кому она нужна, и так понятно кто в этом чате пидор: *@Илюша*"
    bot.sendMessage(message.chat_id, text, parse_mode='Markdown')


def pidor(message):
    response_sequence = GAME_RESPONSE_SEQUENCES[randint(0, len(GAME_RESPONSE_SEQUENCES) - 1)]
    for response in response_sequence:
        bot.sendMessage(message.chat_id, response, parse_mode='Markdown')
        time.sleep(1)


def pidorstats(message):
    text = "По моим данным, в 100% случаев *пидором дня* оказывался: *@Илюша*"
    bot.sendMessage(message.chat_id, text, parse_mode='Markdown')
