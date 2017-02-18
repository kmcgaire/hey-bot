import random
import json
import re
from collections import OrderedDict

from kik.messages import TextResponse


def conversation_type(message):
    if len(set(message.participants)) > 2:
        return 'group'
    else:
        return '1v1'


def build_keyboard(HEY_OPTIONS, extraResponses = False):
    HEY = random.choice(HEY_OPTIONS)
    RESPONSES = [HEY, "Small Talk", "Flirt", "Questions", "News", "Truth or Dare", "Would you rather?", "Facts"]

    if extraResponses:
        RESPONSES += extraResponses

    return [TextResponse(r) for r in RESPONSES]


def sub_in_users(message, body):
    n_subs = len(re.findall('{}', body))
    # Don't do more work then you have to
    if n_subs == 0:
        return body

    users = ['@'+user for user in message.participants]
    sub_users = [random.choice(users) for _ in xrange(n_subs)]
    # sub_users = random.sample(users, n_subs)

    return body.format(*sub_users)


# Logging Helpers
def buildExtraData(reply, event_name):
    extraData = {"event_name": event_name}

    msg_type = reply[0].type
    if event_name == "News":
        reply_data = [("title", reply[0].title), ('url', reply[0].url), ("reply_type", msg_type)]
    else:
        reply_data = [("reply_body", reply[0].body), ("reply_type", msg_type)]

    extraData["reply_data"] = reply_data

    return extraData


def log_metric(in_message, out_message, event):
    if in_message.type != 'text':
        in_message.body = None

    extraData = buildExtraData(out_message, event)
    # Quick Metric Calcs
    n_participants = len(set(in_message.participants))
    # Misclassifies 2 person groups
    is_group = bool(n_participants > 2)

    return json.dumps(OrderedDict([("incoming_timestamp", in_message.timestamp),
                                   ("user_jid", in_message.from_user),
                                   ("incoming_type", in_message.type),
                                   ("event_name", extraData['event_name']),
                                   ("is_mention", bool(in_message.mention)),
                                   ("incoming_body", in_message.body),
                                   ("reply_data", OrderedDict(extraData['reply_data'])),
                                   ("is_grp", is_group),
                                   ("n_participants", n_participants),
                                   ("participants", in_message.participants)]))
