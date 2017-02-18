import random

from kik.messages import SuggestedResponseKeyboard, TextMessage, LinkMessage

from utils import conversation_type, build_keyboard, sub_in_users
from const import HEY, CONTENT


def start_chatting_reply(message, body, response_list):
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
                responses=response_list
            )]
        )]


def text_reply(message, body, response_list):

    body = sub_in_users(message, body)

    return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body=body,
        keyboards=[SuggestedResponseKeyboard(
            responses=response_list
        )]
    )]


def link_reply(message, body, response_list):
    url = body['url']
    title = body['title']

    return [LinkMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        url=url,
        title=title,
        keyboards=[SuggestedResponseKeyboard(
            responses=response_list
        )]
    )]


def handle_message(message):
    convo_type = conversation_type(message)

    # Decide which SR's to Show
    if convo_type == 'group':
        response_list = build_keyboard(HEY)
    else:
        response_list = build_keyboard(HEY, ['Help'])

    # Determine Event Type
    if message.type not in ('start-chatting', 'text'):
        event = 'Unknown'

    elif message.type == 'start-chatting':
        event = 'Subscribe'

    elif message.body in HEY + ['']:
        event = 'Hey'
    else:
        event = message.body

    # Select Response
    try:
        body = random.choice(CONTENT[event][convo_type])
    except Exception as e:
        event = 'Help'
        # Help Messaging for 1v1 with another user should be of `group` type
        if message.mention:
            convo_type = 'group'
        body = random.choice(CONTENT[event][convo_type])

    # Select Reply Type
    if event == "News":
        return link_reply(message, body, response_list), event
    if event == "Subscribe":
        return start_chatting_reply(message, body, response_list), event
    else:
        return text_reply(message, body, response_list), event
