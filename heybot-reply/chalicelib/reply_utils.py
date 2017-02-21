import copy
import random
import re

from kik.messages import SuggestedResponseKeyboard, TextMessage, LinkMessage

from const import *


# Utils
def sub_in_users(message, body):
    n_subs = len(re.findall('{}', body))

    participants = copy.deepcopy(message.participants)
    # Don't do more work then you have to
    if n_subs == 0:
        return body

    users = ['@'+user for user in participants]

    if n_subs > len(users):
        users += ['@Roll', '@Kikteam']

    sub_users = random.sample(users, n_subs)

    return body.format(*sub_users)


def parse_event_name(message):
    if message.type not in ('start-chatting', 'text'):
        event_name = 'Unknown'

    elif message.type == 'start-chatting':
        event_name = 'Subscribe'

    elif message.body in hey_options + ['']:
        event_name = 'Hey'
    else:
        event_name = message.body

    return event_name


# Reply Handlers
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


class Reply:
    def __init__(self, replies, group_requirement, reply_handler):
        '''
        :param replies: list of possible responses to reply with
        :param group_requirement: how many users to consider what a group is
        :param reply_handler: type of reply handler from kik.py (text / link / etc.)
        '''
        self.replies = replies
        self.group_requirement = group_requirement
        self.reply_handler = reply_handler

    def choose_reply(self, message):

        if isinstance(self.replies, dict):
            if len(set(message.participants)) > self.group_requirement:
                convo_context = 'group'
            else:
                convo_context = '1v1'
            return random.choice(self.replies[convo_context])
        else:
            # If there is no dictionary then just grab from the list
            return random.choice(self.replies)

    def build_keyboard(self, message):
        hey_choice = [TextResponse(random.choice(hey_options))]  # hey_options from global

        responses = hey_choice + basic_keyboard

        if not message.mention:
            responses.append(TextResponse("Help"))

        return responses

    def reply(self, message):
        body = self.choose_reply(message)
        keyboard = self.build_keyboard(message)

        return self.reply_handler(message, body, keyboard)


CONTENT = {
    "Unknown": Reply(unknown_reply, None, text_reply),
    "Subscribe": Reply(subscribe_reply, None, start_chatting_reply),
    "Hey": Reply(hey_reply, 2, text_reply),
    "News": Reply(news_reply, 2, link_reply),
    "Small Talk": Reply(small_talk_reply, 2, text_reply),
    "Flirt": Reply(flirt_reply, 2, text_reply),
    "Questions": Reply(questions_reply, 2, text_reply),
    "Would you rather?": Reply(would_you_rather_reply, 2, text_reply),
    "Truth or Dare": Reply(truth_or_dare_reply, 10, text_reply),
    "Facts": Reply(facts_reply, 2, text_reply),
    "Help": Reply(help_reply, 1, text_reply)
}