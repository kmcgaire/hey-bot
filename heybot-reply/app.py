from kik.messages import *
from kik import KikApi
from chalice import Chalice

from collections import OrderedDict
import requests
import json
import datetime

from chalicelib import BOT_USERNAME, BOT_API_KEY
from chalicelib import handle_message

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

    out_messages, extraData = handle_message(message)

    try:
        kik.send_messages(out_messages)
    except Exception as e:
        app.log.error("Message Error: {}".format(e))

    try:
        print log_metric(message, extraData)
    except Exception as e:
        try:
            print app.log.error("Custom Logging Failed! Error: {}, Message: {}, Response:{}, extraData:{}".format(e, message, out_messages, extraData))
        except Exception as e:
            print app.log.error("Something Really Went Wrong: {}".format(e))
    
    return '', 200



def log_metric(in_message, extraData):
    if in_message.type not in ('start-chatting', 'text'):
        in_message.body = None
    
    # Quick Metric Calcs (Happens After Message Send)
    n_participants = len(set(in_message.participants))
    # Mis classes 2 person groups
    is_group = bool(n_participants > 2)
    
    return json.dumps(OrderedDict([("incoming_timestamp", in_message.timestamp),
                                    ("user_jid", in_message.from_user),
                                    ("incoming_type",in_message.type), 
                                    ("action_type", extraData['action_type']),
                                    ("is_mention", bool(in_message.mention)),
                                    ("incoming_body", in_message.body),
                                    ("reply_data", OrderedDict(extraData['reply_data'])),
                                    ("is_grp", is_group),
                                    ("n_participants", n_participants),
                                    ("participants", in_message.participants)]))


# metrics handler

# emoji_pattern = re.compile(
#     u"(\ud83d[\ude00-\ude4f])|"  # emoticons
#     u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
#     u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
#     u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
#     u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
#     "+", flags=re.UNICODE)

# import boto3
# client = boto3.client('cloudwatch')

# def custom_event(msg):

#     client.put_metric_data(
#             Namespace='Custom Metrics',
#             MetricData=[
#                 {
#                     'MetricName': 'heybot',
#                     'Dimensions': [
#                         {
#                             'Name': 'from_user',
#                             'Value': msg.from_user
#                         },
#                         {
#                             'Name': 'body',
#                             'Value': emoji_pattern.sub(r'E', msg.body) #no emoji
#                         },
#                         {
#                             'Name': 'is_mention',
#                             'Value': str(msg.mention)
#                         },
#                     ],
#                     "Value":1,
#                     "Unit": 'Count'
#                 },
#             ]
        # )