from kik.messages import *
from kik import KikApi
from chalice import Chalice

from collections import OrderedDict
import requests
import json
import datetime

from chalicelib import BOT_USERNAME, BOT_API_KEY
from chalicelib import handle_message, log_metric

app = Chalice(app_name='heybot')
app.debug = True

kik = KikApi(BOT_USERNAME, BOT_API_KEY)

@app.route('/', methods=['GET'])
def index():
    return {'hello': 'world'}

ALLOWED_MESSAGE_TYPES = [TextMessage, LinkMessage, PictureMessage, ScanDataMessage, StartChattingMessage, StickerMessage, VideoMessage]

@app.route('/tasks/incoming', methods=['POST'])
def incoming():

    message = messages_from_json([app.current_request.json_body['messages'][0]])[0]

    if not isinstance(message, tuple(ALLOWED_MESSAGE_TYPES)):
        app.log.info('Ignoring non allowed message of type {}'.format(message.type))
        return '', 200

    if message.from_user not in message.participants:
        app.log.info('Ignoring message from bot {}'.format(message.from_user))
        return '', 200

    if message.mention and message.mention != BOT_USERNAME:
        app.log.info('Dropping message mentioning {}'.format(message.mention))
        return '', 200

    out_messages, event = handle_message(message)

    if out_messages:
        try:
            kik.send_messages(out_messages)
        except Exception as e:
            app.log.error("Message Handler Error: {}, Message {}, Response {}".format(e, message.to_json()), out_messages)

    try:
        print log_metric(message, out_messages, event)
    except Exception as e:
        try:
            print app.log.error("Custom Logging Failed! Error: {}, Message: {}, Response:{}, extraData:{}".format(e, message, out_messages, extraData))
        except Exception as e:
            print app.log.error("Something Really Went Wrong: {}".format(e))
    
    return '', 200
