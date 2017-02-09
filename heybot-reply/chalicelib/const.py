BASIC = [
    {'msg':"how are you?"},
	{'msg':'I miss you.'},
	{'msg':"what are you up to?"},
    {'msg':"im bored..."},
    {'msg':"when's the last time I said I love you?"},
    {'msg':"when are you free?"},
    {'msg':"want to video chat?"},
    {'msg':'what are you doing this weekend?'},
    {'msg':"I made this graph of how this conversation is going. " +u"\U0001F4C9"},
    {'msg':"how about we play truth or dare?"},
    {'msg':"who's lurking in here?"}
        
]

INTROS = [
    {'msg':"where are you guys from?"},
    {'msg':"is anyone here single?"},
    {'msg':"what have I missed?"},
    {'msg':"how is everyone!"},
    {'msg':"what do you all like to listen to?"},
    {'msg':"how old is everyone?"}
]

NEWS = [
{'title': "Make Love Not Walls", 'url': 'http://bbc.in/2lsP1z0', 'msg':'did you hear that Trump is building a wall?'},
{'title': "Nintendo Switch", 'url': 'http://bit.ly/2lmtECQ', 'msg':'did you see that Nintendo is launching a new console on March 3rd?'},
{'title': "Teens Leaving Facebook", 'url': 'http://wapo.st/2lsXBxC', 'msg':'did you hear teens are leaving Facebook?'},
{'title': "The Dangers of 'Dripping'", 'url': 'http://usat.ly/2ktY3gJ', 'msg': "do you know what 'dripping' is and why it's dangerous?"},
{'title': "What Drake Thinks About Trump", 'url': 'http://bit.ly/2kQyeIV', 'msg':"did you hear Drake's recent slam on Trump?"},
{'title': "Silicon Valley's Legal Action Against Trump", "url": 'http://ind.pn/2kQxtPW', 'msg': "did you see the companies that are taking legal action on Trump's immigration ban?"}
]

FACTS = [
{'msg':"apparently 'cherophobia' is the fear of fun."},
{'msg':"did u know bikinis and tampons invented by men?"},
{'msg':"I heard average person's yearly fast food intake will contain 12 pubic hairs."},
{'msg':"did you know humans share 50% of their DNA with bananas?"},
{'msg':"did you know Trump is the oldest president to assume office?"}
]

CONVO_SPARK = [
    {'msg':"two truths and a lie. Ready? Go!"},
	{'msg':'have you ever got into big trouble with your parents?'},
	{'msg':'what is your spirit animal?'},
	{'msg':'what is the weirdest thing you have ever eaten?'},
	{'msg':'do you have any pets?'},
	{'msg':'do you have any siblings?'},
	{'msg':'what would you do if you did not have to work?'},
	{'msg':'what would you do if you had a million dollars?'},
	{'msg':'what did / do you want to be when you grow up?'},
	{'msg':"what's your favorite movie?"},
	{'msg':"what was your most embarrasing moment?"},
	{'msg':'what is your hidden talent?'},
	{'msg':'if you could have one super power, what would it be?'},
	{'msg':'what are you scared of most?'},
	{'msg':'do you like country music?'},
	{'msg':'would you ever get a tattoo?'},
	{'msg':'what are you passionate about?'},
	{'msg':"what is the one thing you can't live without?"},
	{'msg':"do you think true love exists?"},
	{'msg':"whats the one thing you'd wish to own"},
	{'msg':"what was your favorite TV show as a kid?"},
	{'msg':"if you were a vegetable, what would you be?"}
	]

PICK_UP = [
	{'msg':"my beard is growing its own beard, whats your name?"},
	{'msg':"girl is your name Wifi ? Because I'm feeling a connection!"},
	{'msg':'you are almost as hot as my mom.'},
	{'msg':'you look exactly like my future ex-wife.'},
	{'msg':"is your dad a preacher? Cause girl you're a blessing."},
  	{'msg':'you are hotter than the bottom of my laptop.'},
	{'msg':'you look fabulous...for your age.'},
	{'msg':'what time do you have to be back in heaven?'},
	{'msg':'A/S/L?'},
	{'msg':"guess who's no longer on his parents cell phone bill?"},
	{'msg':"do you play Quidditch? Because you look like a Keeper."},
	{'msg':"are you Google? Because you're everything I've been searching for."},
	{'msg':"on a scale of one to America, how free are you tonight?"},
	{'msg':"treat me like a pirate and gimme that booty."},
	{'msg':"titanic... Thats my ice-breaker."},
	{'msg':"what came first, the chicken or the egg?"},
	{'msg':"I think I live next door to you!"},
	{'msg':"havn't we met here before?"},
	{'msg':"I don't want to be too forward, but what is your name?"},
	{'msg':"so how does this work, are we married now?"},
	{'msg':"if I was drowning would you give me mouth to mouth?"},
	{'msg':"I think I love you more than I've ever loved myself."},
	{'msg':"I have scars and tattoos, and make a mean grilled cheese."},
	{'msg':"is your middle name Gillette? Because you're the best a man can get."},
	{'msg':u"\U0001F374" + ' ' + u"\U0001F374" + ' ' + u"\U0001F374" + " I've got all these forks and knives, all I need is a little spoon."},
	]

POTENTIAL_SRS = [(3, BASIC), (3, INTROS), (5, NEWS), (3, CONVO_SPARK), (4, PICK_UP), (2, FACTS)]
SR_LIST = [sr['msg'] for b in [BASIC, INTROS, FACTS, CONVO_SPARK, PICK_UP] for sr in b]