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

def start_chatting_reply(message, BODY):

    return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body=BODY[0]
    ),
        TextMessage(
            to=message.from_user,
            delay=500,
            chat_id=message.chat_id,
            body=BODY[1],
            keyboards=[SuggestedResponseKeyboard(
            	responses=build_keyboard()
        )]
        )]

def text_reply(message, BODY):

	return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body=BODY, 
        keyboards=[SuggestedResponseKeyboard(
            responses=build_keyboard()
        )]
    )]

def link_reply(message, BODY):

	url   = BODY['url']
	title = BODY['title']

	return [LinkMessage(
	    to=message.from_user,
	    chat_id=message.chat_id,
	    url=url,
	    title=title,
	    keyboards=[SuggestedResponseKeyboard(
	        responses=build_keyboard()
	    )]
	)]

def handle_message(message):

	CONVO_TYPE = conversation_type(message)

	# Determine key needed for reply
	event = message.body

	if message.type not in ('start-chatting', 'text'):
		event = 'Unknown'
	
	if message.type == 'start-chatting':
		event = 'Subscribe'
	
	if message.body in HEY_OPTIONS:
		event = 'Hey'
	
	try:
		BODY = random.choice(CONTENT[event[CONVO_TYPE]])
	except Exception as e:
		event = 'Help'
		BODY = random.choice(CONTENT[event[CONVO_TYPE]])


	if event == "News":
		return link_reply(BODY)
	if event == "Subscribe":
		return start_chatting_reply()
	else:
		return text_reply(BODY)


def handle_message(message):
	# Msgs other than text or welcome
	if message.type not in ('start-chatting', 'text'):
		reply = basic_reply(message, 'That is quite lovely, but I only respond to text.')
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

	if mention:
		main_reply(message)

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

