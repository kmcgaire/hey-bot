import random
import re
import copy

from kik.messages import SuggestedResponseKeyboard, TextMessage, LinkMessage

from utils import conversation_type, build_keyboard
from const import HEY, CONTENT


# Hey Fork with categories instead of specifics

# @hey random
# @hey small talk
# @hey news
# @hey flirt
# @hey facts
# @hey games


def start_chatting_reply(message, body):
    return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body=body[0]
    ),
        TextMessage(
            to=message.from_user,
            delay=500,
            chat_id=message.chat_id,
            body=body[1],
            keyboards=[SuggestedResponseKeyboard(
                responses=build_keyboard(HEY)
            )]
        )]


def text_reply(message, body):
    return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body=body,
        keyboards=[SuggestedResponseKeyboard(
            responses=build_keyboard(HEY)
        )]
    )]


def link_reply(message, body):
    url = body['url']
    title = body['title']

    return [LinkMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        url=url,
        title=title,
        keyboards=[SuggestedResponseKeyboard(
            responses=build_keyboard(HEY)
        )]
    )]


def handle_message(message):
    convo_type = conversation_type(message)

    # Determine key needed for reply
    event = message.body

    if message.type not in ('start-chatting', 'text'):
        event = 'Unknown'

    if message.type == 'start-chatting':
        event = 'Subscribe'

    if message.body in HEY:
        event = 'Hey'

    try:
        body = random.choice(CONTENT[event][convo_type])
    except:
        event = 'Help'
        body = random.choice(CONTENT[event][convo_type])

    if event == "News":
        return link_reply(message, body), event
    if event == "Subscribe":
        return start_chatting_reply(message, body), event
    else:
        return text_reply(message, body), event
