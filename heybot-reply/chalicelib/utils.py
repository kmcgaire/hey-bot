import random
from kik.messages import TextResponse

def conversation_type(message):
	if len(set(message.participants)) > 2:
		return 'group'
	else:
		return '1v1'

def build_keyboard(HEY_OPTIONS:
	HEY = random.choice(HEY_OPTIONS)
	RESPONSES = [HEY, "Small Talk", "Flirt", "Questions", "News"]
	return [TextResponse(r) for r in RESPONSES]


# Logging Helpers
def buildExtraData(reply, event_name):
	extraData = {"event_name": event}
	
	TYPE = reply[0].type
	if event_name == "News":
		REPLY_DATA = [("title", reply[0].title), ('url':reply[0].url), ("reply_type", TYPE)]
	else:
		REPLY_DATA = [("reply_body", reply[0].body), ("reply_type", TYPE)]

	extraData["reply_data"] = REPLY_DATA

	return extraData

def log_metric(in_message, out_message):

    if in_message.type != 'text':
        in_message.body = None
    
    extraData = buildExtraData(out_message, event)
    # Quick Metric Calcs
    n_participants = len(set(in_message.participants))
    # Misclassifies 2 person groups
    is_group = bool(n_participants > 2)
    
    return json.dumps(OrderedDict([("incoming_timestamp", in_message.timestamp),
                                    ("user_jid", in_message.from_user),
                                    ("incoming_type",in_message.type), 
                                    ("event_name", extraData['event_name']),
                                    ("is_mention", bool(in_message.mention)),
                                    ("incoming_body", in_message.body),
                                    ("reply_data", OrderedDict(extraData['reply_data'])),
                                    ("is_grp", is_group),
                                    ("n_participants", n_participants),
                                    ("participants", in_message.participants)]))