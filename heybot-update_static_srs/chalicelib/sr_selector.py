import random

def select_new_srs(potential_responses):
	'''
	potential_responses: a list of all response categories
	'''
	random_selection = []
	for i in potential_responses:
		random_selection.extend(random.sample(i[1], i[0]))
	return [{'body':i['msg'], 'type':'text'} for i in random_selection]