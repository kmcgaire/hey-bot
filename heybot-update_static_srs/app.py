from chalice import Chalice
import logging
import requests
import json

from chalicelib import BOT_USERNAME, BOT_API_KEY, WEBHOOK
from chalicelib import select_new_srs
from chalicelib import POTENTIAL_SRS


app = Chalice(app_name='heybot-update_static_sr')
app.debug = True

@app.route('/', methods=['GET'])
def index():
    return {'hello': 'world'}


def update_srs(event, context):
	requests.post(
	    'https://api.kik.com/v1/config',
	    auth=(BOT_USERNAME, BOT_API_KEY),
	    headers={
	        'Content-Type': 'application/json'
	    },
	    data=json.dumps({
	        'webhook': WEBHOOK,
	        'features': {
	            'receiveReadReceipts': False, 
	            'receiveIsTyping': False, 
	            'manuallySendReadReceipts': False, 
	            'receiveDeliveryReceipts': False
	        }, 
	        'staticKeyboard': {
	            'type': 'suggested', 
	            'responses': select_new_srs(POTENTIAL_SRS)
	        }
	    })
	    )