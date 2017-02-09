import random
from kik.messages import TextResponse

def select_new_srs(potential_responses):
	'''
	potential_responses: a list of all response categories
	'''
	random_selection = []
	for i in potential_responses:
		random_selection.extend(random.sample(i[1], i[0]))
    	return [TextResponse(i['msg']) for i in random_selection]