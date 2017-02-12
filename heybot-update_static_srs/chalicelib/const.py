FORK = u"\U0001F374" 
GRAPH = u"\U0001F4C9"
WAVE_HAND = u"\U0001F44B"

BASIC_1v1 = ["how are you?",
'I miss you.',
"what are you up to?",
"im bored...",
"when's the last time I said I love you?", 
"when are you free?", 
"want to video chat?", 
'what are you doing this weekend?', 
"I made a graph of how this conversation is going. " + GRAPH, 
'knock knock, anyone here?']

BASIC_GROUP = [
"where are you guys from?",
"anyone want to play truth or dare?",
"is anyone here single?",
"what have I missed?",
"what do you guys like to listen to?",
"how old is everyone?",
"who's lurking in here?",
"is anyone here as bored as me?",
"who else is watching Netflix rn?"
]

NEWS = {
"did you see Kristen Stewart Rocked Spanx as a sress on 'SNL'?":{'title':"Kristen Stewart Rocks Spanks On 'SNL'", "url":"http://huff.to/2lviNXp"},
"did you see DJ Khaled's son puked on him at the red carpet?":{'title':"DJ Khaled Gets Puked On LIVE", "url":"http://bit.ly/2lAd52n"},
"did you hear that Trump is building a wall?": {'title': "Make Love Not Walls", 'url': 'http://bbc.in/2lsP1z0'},
"did you see that Nintendo is launching a new console on March 3rd?": {'title': "Nintendo Switch", 'url': 'http://bit.ly/2lmtECQ'},
"did you hear teens are leaving Facebook?": {'title': "Teens Leaving Facebook", 'url': 'http://wapo.st/2lsXBxC'},
"do you know what 'dripping' is and why it's dangerous?": {'title': "The Dangers of 'Dripping'", 'url': 'http://usat.ly/2ktY3gJ'},
"did you hear Drake's recent slam on Trump?": {'title': "What Drake Thinks About Trump", 'url': 'http://bit.ly/2kQyeIV'},
"did you see the companies that are taking legal action on Trump's immigration ban?": {'title': "Silicon Valley's Legal Action Against Trump", "url": 'http://ind.pn/2kQxtPW'}}

FACTS = [
"apparently 'cherophobia' is the fear of fun.",
"did u know bikinis and tampons were invented by men?",
"I heard average person's yearly fast food intake will contain 12 pubic hairs.",
"did you know humans share 50% of their DNA with bananas?",
"did you know Trump is the oldest president to assume office?"
]

QUESTIONS_1v1 = [
'what is your spirit animal?',
'what is the weirdest thing you have ever eaten?',
'do you have any pets?',
'do you have any siblings?',
'what would you do if you did not have to work?',
'what would you do if you had a million dollars?',
'what did / do you want to be when you grow up?',
"what's your favorite movie?",
"what was your most embarrasing moment?",
'what is your hidden talent?',
'if you could have one super power, what would it be?',
'what are you scared of most?',
'do you like country music?',
'would you ever get a tattoo?',
'what are you passionate about?',
"what is the one thing you can't live without?",
"do you think true love exists?",
"whats the one thing you'd wish to own",
"what was your favorite TV show as a kid?",
"if you were a vegetable, what would you be?"
]

QUESTIONS_GRP = [
'everyone name your spirit animal?',
'what is the weirdest thing everyones eaten?',
'anyone have a pet?',
'anyone have siblings?',
"what would you guys do if you didn't have to work?",
'what would you guys do if you had a million dollars?',
"everyone name your favorite movie!",
"I dare anyone to say their most embarrasing moment!",
'anyone have a hidden talent?',
'everyone name the super power they wish they had!',
'everyone say their biggest fears!',
'anyone like country music?',
'who would get a tattoo?',
"what can't you guys live without?",
"does anyone believe in true love here?",
"everyone name your favorite TV show!",
"if you guys were vegetables, what would you be?"
]

PICK_UP_1v1 = [
"my beard is growing its own beard, whats your name?",
"girl is your name Wifi ? Because I'm feeling a connection!",
'you are almost as hot as my mom.',
'you look exactly like my future ex-wife.',
"is your dad a preacher? Cause girl you're a blessing.",
'you are hotter than the bottom of my laptop.',
'you look fabulous...for your age.',
'what time do you have to be back in heaven?',
'A/S/L?',
"interested in a man that pays his own cell phone bill?",
"do you play Quidditch? Because you look like a Keeper.",
"are you Google? Because you're everything I've been searching for.",
"on a scale of one to America, how free are you tonight?",
"treat me like a pirate and gimme that booty.",
"titanic... Thats my ice-breaker.",
"what came first, the chicken or the egg?",
"I think I live next door to you!",
"havn't we met here before?",
"I don't want to be too forward, but what is your name?",
"so how does this work, are we married now?",
"if I was drowning would you give me mouth to mouth?",
"I think I love you more than I've ever loved myself.",
"I have scars and tattoos, and make a mean grilled cheese.",
"is your middle name Gillette? Because you're the best a man can get.",
FORK + ' ' + FORK + ' ' + FORK + " I've got all these forks and knives, do you want to be my little spoon?"
]

PICK_UP_GROUP = [
"my beard is growing its own beard, anyone wanna DM?",
"any girls named WiFi? Because I'm feeling a connection!",
'you guys are almost as hot as my moms.',
'one of you looks exactly like my future ex-wife.',
"anyones dad a preacher? Cause you're a blessing.",
'you guys are hotter than the bottom of my laptop.',
"you all look fabulous...for your age.",
'what time do you guys have to be back in heaven?',
'A/S/L?',
"anyone interested in a man that pays his own cell phone bill?",
"does anyone play Quidditch? Because you'll be my Keeper.",
"are you guys Google? Because you're everything I've been searching for.",
"on a scale of one to America, how free are y'all tonight?",
"treat me like a pirate and gimme that booty.",
"titanic... Thats my ice-breaker.",
"what came first, the chicken or the egg?",
"I think I live next door to you ^^",
"I don't want to be too forward, but what's everyones name?",
"so how does this work, are we all married now?",
"if I was drowning who would give me mouth to mouth?",
"I think I love you all more than I've ever loved myself.",
"I have scars and tattoos, and make a mean grilled cheese. Anyone interested?",
"anyone here named Gillette? Because you're the best a man can get.",
FORK + ' ' + FORK + ' ' + FORK + " I've got all these forks and knives, anyone want to be my little spoon?"
]

LUCKY = ["hey!", "I'm feeling lucky.", WAVE_HAND]

POTENTIAL_SRS = [(1, LUCKY), 
				(4, BASIC_1v1), (4, BASIC_GROUP),
				(3, NEWS.keys()),
			    (2, QUESTIONS_GRP),
				(4, PICK_UP_GROUP), 
				(2, FACTS)]