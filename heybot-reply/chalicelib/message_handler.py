from reply_utils import *

def handle_message(message):
    event_name = parse_event_name(message)

    # Reply Logic
    try:
        reply = CONTENT[event_name]
        return reply.reply(message), event_name
    except Exception as e:
        event_name = 'Help'
        reply = CONTENT[event_name]
        return reply.reply(message), event_name
