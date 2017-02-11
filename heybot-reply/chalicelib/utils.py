import random
from kik.messages import TextResponse

ORDER_SAMPLE = [1, 5, 3, 5, 4, 2]

def select_random_srs(potential_responses):
	'''
	potential_responses: a list of all response categories
	'''
	x = zip(ORDER_SAMPLE, potential_responses)
	random_selection = []
	for i in x:
		random_selection.extend(random.sample(i[1], i[0]))
    	return [TextResponse(j) for j in random_selection]