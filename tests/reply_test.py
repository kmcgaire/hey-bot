import sys
import timeit

from kik.messages import *

sys.path.append('/Users/rkelly/Projects/heybot/heybot-reply/chalicelib/')

from reply_utils import CONTENT
from message_handler import handle_message

help_1v1 = {
    "Name": "help_1v1",
    "expected_reply": CONTENT['Help'].replies['1v1'],
    "message": {
                "chatId": "0ee6d46753bfa6ac2f089149959363f3f59ae62b10cba89cc426490ce38ea92d",
                "id": "0115efde-e54b-43d5-873a-5fef7adc69fd",
                "type": "text",
                "from": "rmdkelly",
                "participants": ["rmdkelly"],
                "body": "omg r u real?",
                "timestamp": 1439576628405,
                "readReceiptRequested": True,
                "mention": None,
                "metadata": None
            }
}

help_grp = {
    "Name": "help_grp",
    "expected_reply": CONTENT['Help'].replies['group'],
    "message": {
                "chatId": "0ee6d46753bfa6ac2f089149959363f3f59ae62b10cba89cc426490ce38ea92d",
                "id": "0115efde-e54b-43d5-873a-5fef7adc69fd",
                "type": "text",
                "from": "rmdkelly",
                "participants": ["rmdkelly", "cacolve"],
                "body": "omg r u real?",
                "timestamp": 1439576628405,
                "readReceiptRequested": True,
                "mention": None,
                "metadata": None
            }
}

hey_group = {
    "Name": "hey_group",
    "expected_reply": CONTENT['Hey'].replies['group'],
    "message": {
                "chatId": "0ee6d46753bfa6ac2f089149959363f3f59ae62b10cba89cc426490ce38ea92d",
                "id": "0115efde-e54b-43d5-873a-5fef7adc69fd",
                "type": "text",
                "from": "rmdkelly",
                "participants": ["rmdkelly", "cacolve", ".joelc"],
                "body": "Hey",
                "timestamp": 1439576628405,
                "readReceiptRequested": True,
                "mention": None,
                "metadata": None
            }
}

message_tests = [help_1v1, help_grp, hey_group,]


# message = messages_from_json([help_1v1['message']])[0]
# import cProfile
# pr = cProfile.Profile()
# pr.enable()
# handle_message(message)
# pr.disable()
# pr.print_stats(sort='time')


def generate_reply(msg):
    message = messages_from_json([msg['message']])[0]
    return messages_from_json([handle_message(message)[0][0].to_json()])[0], msg['expected_reply'],\
        min(timeit.Timer(lambda: handle_message(message)).repeat(repeat=10, number=1000))


def test_reply():
    print '\n'
    for m in message_tests:
        message, expectation, duration = generate_reply(m)
        print "{}: {} \n".format(m['Name'], duration)
        assert message.body in expectation
