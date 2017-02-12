import random
import re
import copy

from kik.messages import SuggestedResponseKeyboard, TextMessage, LinkMessage

from utils import select_random_srs
from const import ONE_ON_ONE_MSGS, GROUP_MSGS, NEWS, LUCKY, HELP_1v1, HELP_GROUP

def dynamic_content_logic(message, body=None):

	index_to_return_in_replies = [1, 3, 4]
	
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
        body="I'm a bot that can help you start conversations."
    ),
        TextMessage(
            to=message.from_user,
            delay=500,
            chat_id=message.chat_id,
            body="Don't know what to say? Just type @hey!"
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
		reply = basic_reply(message, 'Thanks, but no thanks...')
		return reply, {"action_type": "body_is_not_text", 
						"reply_data":[("reply_body", reply[0].body), ("reply_type", reply[0].type)]}

	# Welcome Message
	if message.type == 'start-chatting':
		reply = handle_start_chatting(message)
		return reply, {"action_type": "start_chatting", 
						"reply_data":[("reply_body", '|'.join(r.body for r in reply)), ("reply_type", 'start-chatting')]}

	# Respond to empty request
	if message.body in LUCKY + ['']:
		reply = basic_reply(message)
		return reply, {"action_type": "feeling_lucky", 
						"reply_data":[("reply_body", reply[0].body), ("reply_type", reply[0].type)]}

    # Replies to News or SR's with Links
	if message.body in NEWS.keys():
		reply = link_reply(message, NEWS)
		return reply, {"action_type": "news", 
						"reply_data":[("reply_url", reply[0].url), ("reply_title", reply[0].title), ("reply_type", reply[0].type)]}
	
	# Respond to 1v1 help messages
	if not message.mention:
		reply = basic_reply(message, random.choice(HELP_1v1))
		return reply, {"action_type": "help", 
						"reply_data":[("reply_body", reply[0].body), ("reply_type", reply[0].type)]}

	# Don't reply if it's one of the baked in options
	if message.body in [msg for sublist in GROUP_MSGS + ONE_ON_ONE_MSGS for msg in sublist]:
			reply = None
			return reply, {"action_type": "no_reply", 
							"reply_data":[]}

	else:
		# Group help
		reply = basic_reply(message, random.choice(HELP_GROUP))
		return reply, {"action_type": "help", 
						"reply_data":[("reply_body", reply[0].body), ("reply_type", reply[0].type)]}

