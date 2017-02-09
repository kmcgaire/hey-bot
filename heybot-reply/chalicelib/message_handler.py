import random
import re
import copy

from kik.messages import SuggestedResponseKeyboard, TextMessage, LinkMessage

from sr_selector import select_new_srs
from const import SR_LIST, POTENTIAL_SRS, NEWS

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

def basic_reply(message, response_body):

    return [TextMessage(
        to=message.from_user,
        chat_id=message.chat_id,
        body=response_body, 
        keyboards=[SuggestedResponseKeyboard(
            responses=select_new_srs(POTENTIAL_SRS)
        )]
    )]

def link_reply(message, NEWS_LINKS):

	for news in NEWS_LINKS:
		if news['msg'] == message.body:
			url   = news['url']
			title = news['title']

	return [LinkMessage(
	    to=message.from_user,
	    chat_id=message.chat_id,
	    url=url,
	    title=title,
	    keyboards=[SuggestedResponseKeyboard(
	        responses=select_new_srs(POTENTIAL_SRS)
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
	if message.body == '':
		return basic_reply(message, random.choice(SR_LIST))
	# Don't reply 
	if message.mention and message.body in SR_LIST:
		return None

	# Replies to News or SR's with Links
	if message.body in [r['msg'] for r in NEWS]:
		return link_reply(message, NEWS)

	# Fallback to help
	else:
		return basic_reply(message, "@hey doesn't reply, it just helps start conversations!")

