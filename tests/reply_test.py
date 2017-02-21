import sys
import json

from kik.messages import *
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
sys.path.append('heybot-reply/chalicelib')

from reply_utils import CONTENT
from message_handler import handle_message

non_mention_1v1 = {
    "expected_reply": CONTENT['Help'].replies,
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

message_tests = [non_mention_1v1]


def generate_reply(msg):
    message = messages_from_json([msg['message']])[0]
    return messages_from_json([handle_message(message)[0][0].to_json()])[0], msg['expected_reply']


def test_reply():
    for m in message_tests:
        message, expectation = generate_reply(m)
        print message, expectation
        assert message.body in expectation
