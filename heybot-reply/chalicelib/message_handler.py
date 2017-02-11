import random
import re
import copy

from kik.messages import SuggestedResponseKeyboard, TextMessage, LinkMessage

from utils import select_random_srs
from const import ONE_ON_ONE_MSGS, GROUP_MSGS, NEWS, LUCKY

def dynamic_content_logic(message, body=None):

	index_to_return_in_replies = [1, 3, 4, 5]
	
	if len(set(message.participants)) > 2:
		KEYBOARD_CONTENT = GROUP_MSGS
	else:
		KEYBOARD_CONTENT = ONE_ON_ONE_MSGS

	if body is None:
		CLEANED_BODY_OPTIONS = [KEYBOARD_CONTENT[i] for i in index_to_return_in_replies]
		BODY = random.choice(random.choice(CLEANED_BODY_OPTIONS))
	else:
		BODY = body

	return BODY, KEYBOARD_CONTENT

def handle_start_chatting(message):
    return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body="'@hey' is a bot that doesn't interrupt you, it helps you start conversations."
    ),
        TextMessage(
            to=message.from_user,
            delay=500,
            chat_id=message.chat_id,
            body="Type '@hey' to get help starting conversations."
        )]

def basic_reply(message, body=None):

	BODY, KEYBOARD_CONTENT = dynamic_content_logic(message, body)

	return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body=BODY, 
        keyboards=[SuggestedResponseKeyboard(
            responses=select_random_srs(KEYBOARD_CONTENT)
        )]
    )]

def link_reply(message, NEWS_DICT):

	url   = NEWS_DICT[message.body]['url']
	title = NEWS_DICT[message.body]['title']

	BODY, KEYBOARD_CONTENT = dynamic_content_logic(message)

	return [LinkMessage(
	    to=message.from_user,
	    chat_id=message.chat_id,
	    url=url,
	    title=title,
	    keyboards=[SuggestedResponseKeyboard(
	        responses=select_random_srs(KEYBOARD_CONTENT)
	    )]
	)]

def handle_message(message):
	# Msgs other than text or welcome
	if message.type not in ('start-chatting', 'text'):
		return basic_reply(message, 'Thanks, but no thanks...')

	# Welcome Message
	if message.type == 'start-chatting':
		return handle_start_chatting(message)

	# Respond to empty request
	if message.body in LUCKY + ['']:
		return basic_reply(message)

    # Replies to News or SR's with Links
	if message.body in NEWS.keys():
		return link_reply(message, NEWS)
	
	# Don't reply if it's one of the baked in options
	if message.mention and message.body in [msg for sublist in GROUP_MSGS + ONE_ON_ONE_MSGS for msg in sublist]:
		return None

	# Fallback to help
	else:
		return basic_reply(message, "@hey doesn't reply, it just helps start conversations!")

