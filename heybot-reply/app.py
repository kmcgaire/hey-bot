from kik.messages import *
from kik import KikApi
import logging
from chalice import Chalice

import requests
import json

from chalicelib import BOT_USERNAME, BOT_API_KEY
from chalicelib import handle_message

app = Chalice(app_name='heybot')
# app.debug = True
app.log.setLevel(logging.INFO)


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

    app.log.info('Processing message: {}'.format(message.to_json()))

    outgoing_messages = handle_message(message)

    if outgoing_messages:
        app.log.info('Outgoing messages: {}'.format([m.to_json() for m in outgoing_messages]))
        # custom_event(message.body)

    if outgoing_messages:
        kik.send_messages(outgoing_messages)

	return '', 200

# metrics handler

# import boto3
# client = boto3.client('cloudwatch')

# def custom_event(event_id):
#     client.put_metric_data(
#             Namespace='Custom Metrics',
#             MetricData=[
#                 {
#                     'MetricName': event_id,
#                     'Dimensions': [
#                         {
#                             'Name': 'USER_EVENT',
#                             'Value': 'SUCCESS'
#                         },
#                     ],
#                     'Value': 1.0,
#                     'Unit': 'Count'
#                 },
#             ]
#         )
