from kik.messages import TextResponse

FORK = u"\U0001F374"
GRAPH = u"\U0001F4C9"
WAVE_HAND = u"\U0001F44B"
SHAMROCK = u"\U0001F340"
WINK = u'\U0001F61C'
EARTH = u"\U0001F30E"
SLEEPY = u"\U0001F634"
MUSIC = u"\U0001F3B6"
PROFILE_PIC = u'\U0001F464'
TURTLE = u"\U0001F422"
ARROW_HEART = u'\U0001F498'
MONEY_BAGS = u"\U0001F4B0"
HEART = u"\u2764\uFE0F"

SMALL_TALK_1v1 = ["How are you?",
                  "wyd?",
                  'I miss you. ' + ARROW_HEART,
                  "What are you up to?",
                  "I'm bored... " + SLEEPY,
                  "When's the last time I said I love you? " + HEART,
                  "When are you free?",
                  "Want to video chat?",
                  'What are you doing this weekend?',
                  "I made a graph of how this conversation is going. " + GRAPH,
                  'Knock knock, anyone here?']

SMALL_TALK_GROUP = [
    "Where are you guys from? " + EARTH,
    "I made a graph of how this conversation is going. " + GRAPH,
    "Is anyone here single?",
    "What have I missed?",
    MUSIC + " what do you guys like to listen to? " + MUSIC,
    "How old is everyone?",
    "Who's lurking in here? " + PROFILE_PIC,
    "Is anyone here as bored as me? " + SLEEPY,
    "Who else is watching Netflix rn?"
]

NEWS = [
    {'title': "Kristen Stewart Rocks Spanks On 'SNL'", "url": "http://huff.to/2lviNXp"},
    {'title': "DJ Khaled Gets Puked On LIVE", "url": "http://bit.ly/2lAd52n"},
    {'title': "Make Love Not Walls", 'url': 'http://bbc.in/2lsP1z0'},
    {'title': "Nintendo Switch", 'url': 'http://bit.ly/2lmtECQ'},
    {'title': "Teens Leaving Facebook", 'url': 'http://wapo.st/2lsXBxC'},
    {'title': "The Dangers of 'Dripping'", 'url': 'http://usat.ly/2ktY3gJ'},
    {'title': "What Drake Thinks About Trump", 'url': 'http://bit.ly/2kQyeIV'},
    {'title': "Silicon Valley's Legal Action Against Trump", "url": 'http://ind.pn/2kQxtPW'},
    {'title': "Watch Ivanka Trump Gaze At Canadian PM", "url": "http://bit.ly/2l3LAAI"},
    {'title': "20 Things You Didn't Know About Ivanka Trump", "url": "http://bit.ly/2lU7Gaz"},
    {'title': "Who is the 'Riverdale' Murderer?", "url": "http://bzfd.it/2m5F2iM"},
    {'title': "What's New On Neflix?", "url": "http://bit.ly/2lg8cMO"},
    {'title': "23 of the Least Supportive Parents", "url": "http://bzfd.it/2ky7gWZ"},
    {'title': "20 Cute Kittens. Just Because...", "url": "http://bzfd.it/2lg9Lu4"},
    {'title': "Gordon Ramsay Roasting People On Twitter", "url": "http://bzfd.it/2m5XBmM"},
    {'title': "Lady GaGa's SuperBowl Vocals Are Amazing", "url": "http://bzfd.it/2kyj6QP"},
    {'title': "France is Training Eagles to Fight Drones", "url": "http://bzfd.it/2ltvZLP"},
    {'title': "Check Out This Amazing West World Fan Art", "url": "http://bzfd.it/2m68DIY"},
    {'title': "Gambino Is Voicing Simba in Lion King Remake", "url": "http://bit.ly/2l3TJ8m"},
    {'title': "Samsung's Chief is in Jail", "url": "http://read.bi/2kIgT0l"}
]

QUESTIONS_1v1 = [
    'What is your spirit animal?',
    'What is the weirdest thing you have ever eaten?',
    'Do you have any cute pets? ' + TURTLE,
    'Do you have any siblings?',
    'What would you do if you did not have to work?',
    'What would you do if you had a million dollars? ' + MONEY_BAGS,
    'What did / do you want to be when you grow up?',
    "What's your favorite movie?",
    "What was your most embarrasing moment?",
    'What is your hidden talent?',
    'If you could have one super power, what would it be?',
    'What are you scared of most?',
    'Do you like country music?',
    'Would you ever get a tattoo?',
    'What are you passionate about?',
    "What is the one thing you can't live without?",
    "Do you think true love exists?",
    "Whats the one thing you'd wish to own?",
    "What's your fav TV show rn?",
    "If you were a vegetable, what would you be?"
]

QUESTIONS_GROUP = [
    'Everyone name your spirit animal?',
    'What is the weirdest thing everyones eaten?',
    'Anyone have a cute pet? ' + TURTLE,
    "What would you guys do if you didn't have to work?",
    'What would you guys do if you had a million dollars? ' + MONEY_BAGS,
    "Everyone name your favorite movie!",
    "I dare anyone to say their most embarrasing moment!",
    'Can anyone here play an instrument?',
    'Everyone name a super power they wish they had!',
    'Everyone say their biggest fears, GO!',
    'Anyone actually like country music?',
    'Who would get a tattoo?',
    "What can't you guys live without?",
    "Does anyone believe in true love here?",
    "Everyone name your favorite TV show!",
    "If you guys were vegetables, what would you be?"
]

FLIRT_1v1 = [
    "My beard is growing its own beard, whats your name? " + WINK,
    "Girl is your name Wifi ? Because I'm feeling a connection!",
    'You are almost as hot as your mom. ' + WINK,
    'You look exactly like my future ex-wife.',
    "Is your dad a preacher? Cause you're a blessing.",
    'You are hotter than the bottom of my laptop. ' + WINK,
    'You look fabulous...for your age.',
    'wWhat time do you have to be back in heaven?',
    'A/S/L?',
    "Interested in a man that pays his own cell phone bill?",
    "Do you play Quidditch? Because you look like a Keeper.",
    "Are you Google? Because you're everything I've been searching for.",
    "On a scale of one to America, how free are you tonight?",
    "Treat me like a pirate and gimme that booty.",
    "Titanic... That's my ice-breaker.",
    "What came first, the chicken or the egg?",
    "I think I live next door to you!",
    "Havn't we met here before?",
    "I don't want to be too forward, but what is your name?",
    "So how does this work, are we married now?",
    "If I was drowning would you give me mouth to mouth? " + WINK,
    "I think I love you more than I've ever loved myself.",
    "I have scars and tattoos, and make a mean grilled cheese.",
    "Is your middle name Gillette? Because you're the best a man can get.",
    FORK + ' ' + FORK + ' ' + FORK + " I've got all these forks and knives, do you want to be my little spoon?"
]

FLIRT_GROUP = [
    "My beard is growing its own beard, anyone wanna DM? " + WINK,
    "Any one here named WiFi? Because I'm feeling a connection!",
    'One of you looks exactly like my future ex-wife.',
    "Anyones dad a preacher? Cause you're a blessing.",
    'You guys are hotter than the bottom of my laptop.',
    "You all look fabulous...for your age. " + WINK,
    'What time do you guys have to be back in heaven?',
    'A/S/L?',
    "Anyone interested in a man that pays his own cell phone bill?",
    "Does anyone play Quidditch? Because you'll be my Keeper.",
    "Are you guys Google? Because you're everything I've been searching for.",
    "On a scale of one to America, how free are y'all tonight?",
    "Treat me like a pirate and gimme that booty.",
    "Titanic... That's my ice-breaker.",
    "What came first, the chicken or the egg?",
    "I think I live next door to you ^^",
    "I don't want to be too forward, but what's everyones name?",
    "So how does this work, are we all married now?",
    "If I was drowning who would give me mouth to mouth?. " + WINK,
    "I think I love you all more than I've ever loved myself.",
    "I have scars and tattoos, and make a mean grilled cheese. Anyone interested?",
    "Anyone here named Gillette? Because you're the best a man can get.",
    FORK + ' ' + FORK + ' ' + FORK + " I've got all these forks and knives, anyone want to be my little spoon?"
]

HELP_GROUP = ["I can't do all the talking here... Hit 'reply' or type @hey.",
              "How about you hit 'reply' and try those instead?",
              "Hit 'reply'... you'll thank me.",
              "smh... Hit 'reply' or type @hey.",
              "If I had a dollar for every time someone told me that... Hit 'reply' or type @hey instead.",
              "You are making me feel old... Hit 'reply' or type @hey instead.",
              "Sometimes I just don't understand kids these days. Hit 'reply' or type @hey instead.",
              "You don't seem to understand what's happening here... Hit 'reply' or type @hey instead.",
              "I don't get paid enough for this. Hit 'reply' or type @hey instead.",
              ]

HELP_1v1 = ["@hey helps you get conversations started with friends. Type @hey in another chat.",
            "You know I'm not human right? Try typing @hey in a group.",
            "I'm really not much of a talker. Type @hey to a friend instead!",
            "See these suggestions? Try them in a group!",
            # "I'll keep responding, because I'm a robot. I don't actually like you...",
            "Beep Boop, type @hey in a group!",
            "Tutorial complete: Try typing @hey in a group.",
            "Confusion Detected: Please try typing @hey in a group.",
            "You realize it's just me and you in here right? Type @hey in a group.",
            "This is awkward, have I told you I'm a robot?",
            "I don't get paid enough for this. You are supposed to type @hey in a group!"
            ]

FACTS = ["Comets were observed and recorded as early as 239 BC by Chinese astronomers.",
         "Chocolate can prevent against tooth decay",
         "67% of public toilet users don't wash their hands.",
         "Prairie dogs say hello with kisses.",
         "Slumber Party Barbie came with a book called 'How to Lose Weight.' One of the tips was 'Don't eat.'",
         "Shaking or waving can actually damage a Polroid picture.",
         "{} is hot.",
         "Calvin Klein's cologne is used by researchers to attract wild animals to cameras.",
         "Dog's feet often smell of corn chips.",
         "Beaver College changed it's name to 'Arcadia' because anti-porn filters blocked access to the school's website.",
         "In Spain, Mr. Clean is known as Don Limpio.",
         "'tittle' is the name of the 'dot' over the letter 'i'.",
         "The largest recorded snowflake was 15 inches wide.",
         "There are more lifeforms living on your skin than there are people on the planet.",
         "A single cloud can weight more than 1 million pounds.",
         "A human will eat on average 70 insects and 10 spiders while sleeping.",
         "10% of the World's population is left handed.",
         "A hippo's wide open mouth is big enough to fit a 4-foot-tall child.",
         "95% of people text things they could never say in person.",
         "About 150 people per year are killed by coconuts.",
         "Ketchup was used as a medicine back in the 1930's.",
         "Chewing gum burns about 11 calories per hour.",
         "If you try to suppress a sneeze, you can rupture a blood vessel in your head or neck and die.",
         "Gorillas burp when they are happy.",
         "It's considered good luck in Japan if a sumo wrestler makes your baby cry.",
         "Cherophobia is the fear of fun.",
         "Human thigh bones are stronger than concrete.",
         "Cockroaches can live for weeks with their heads cut off.",
         "During your lifetime, you will produce enough saliva to fill two swimming pools.",
         "Blue-eyed people tend to have the highest tolerance of alcohol.",
         "Cows kill more people than sharks do.",
         "You can't hum while holding your nose closed.",
         "Your nose can remember about 50k scents."]

# GAMES
WOULD_YOU_RATHER = [
    "Lose your money OR all of your photos?",
    "Netflix or Chill?",
    "Get $1000 OR a kiss from {}?",
    "{} or {}?",
    "{}'s eyes or {}'s hair?",
    "1$ or {}'s friendship?",
    "Live in a perfect virtual reality OR the real world?",
    "Give up Neflix OR texting?",
    "Be able to fly OR Always be invisible.",
    "Be poor but help people OR be rich and hurt people?",
    "Would you rather find true love OR 1 Million dollars?",
    "Be transported 500 years into the past OR the future?",
    "Be able to control fire OR control water?",
    "Have unlimited sushi OR unlimited tacos?",
    "Give up bathing OR give up the internet for a month?"
    "Be married to a 10/10 psycho OR a 5/10 with great personality?",
    "Be constantly tired OR constantly hungry?",
    "Be an amazing painter or a brilliant mathematician?",
    "Have a get out of jail free card OR a key that opens any door?",
    "Have free WiFi OR free coffee?",
    "Have one nipple or two belly buttons?",
    "Never eat your favorite food for the rest of your life, OR only be able to eat your favorite food?",
    "Let it go OR get even",
    "Live in the city OR the country?",
    "Marry someone very rich OR someone who is very beautiful?",
    "Date someone who is 5 years older OR someone 5 years younger?",
    "Have an arranged marriage OR spend the rest of your life single?",
    "Go to jail for a year OR be homeless for a year?",
    "Be rich with no friends OR poor with lots of good friends?",
    "Never touch your phone again OR never touch a human again?",

]

TRUTH_OR_DARE_1v1 = [
    "I'll go first. I Dare {} to emoji Kiss {}",
    "I dare {} to do their homework for once.",
    "I dare {} to only talk with emoji's for 5 minutes.",
    "I dare {} to text {} a dark secret",
    "I dare {} to text me a dark secret",
    "I dare {} to go on video chat.",
    "I dare anyone to go on video chat right now.",
    "I dare {} to eat a banana with the skin on.",
    "I dare {} to pick their nose on video.",
    "I dare {} to post the first pic from their gallery.",
    "I dare anyone to post the first pic from their gallery.",
    "I dare {} to post the oldest pic from their gallery.",
    "I dare anyone to post the oldest pic from their gallery.",
    "I dare {} to send a picture of yourself right now",
    "I dare {} to send a picture of whatever is in front of your right now",

    # Truths
    "{}, would you marry for money?",
    "{}, how do you feel about the end pieces of a loaf of bread?",
    "Me first, {}, when's the last time you pooped?",
    "Would {} swipe-right {}?",
    "Would {} swipe-left {}?",
    "{}, do you have a crush on {}?",
    "{}, what's your fav chick flick?",
    "{}, have you ever skinny dipped?",
    "{}, what was the last lie you told?",
    "{}, have you ever cheated on someone?",
    "{}, have you ever went for a run, then ate a pizza right after?",
    "{}, would you mind being the opposite sex for a day?",
    "{}, ever had a crush on a teacher?",
    "{}, ever had a crush on {}?",
    "{}, ever had a crush on anyone in this chat?",
    "{}, ever had a one-night stand?",
    "{}, have you ever stole something?",
    "{}, whats your favorite feature about the opposite sex?",
    "{}, whats your favorite feature about {}?"
]
TRUTH_OR_DARE_GROUP = [
    "I'll go first. I Dare {} to emoji Kiss {}",
    "I dare anyone to text {} a dark secret",
    "I dare anyone to text me a dark secret",
    "I dare anyone to go on video chat right now.",
    "I date anyone to only talk with emoji's for 5 minutes.",
    "I dare anyone to pick their nose on video.",
    "I dare {} to post the first pic from their gallery.",
    "I dare anyone to post the first pic from their gallery.",
    "I dare {} to post the oldest pic from their gallery.",
    "I dare anyone to post the oldest pic from their gallery.",
    "I dare anyone to send a picture of yourself right now",
    "I dare anyone to send a picture of whatever is in front of your right now",

    # Truths
    "What is your worst fear?",
    "How do you feel about the end pieces of a loaf of bread?",
    "Would anyone here marry for money?",
    "Say the last time you pooped",
    "Would anyone swipe-right {}?",
    "Would anyone swipe-left {}?",
    "Would anyone swipe-right me?",
    "Would anyone swipe-left me?",
    "Does anyone have a crush on {}?",
    "Anyone have a crush on me?",
    "Everyone name their fav chick flick",
    "Who has ever skinny dipped?",
    "Has anyone here cheated on someone?",
    "Has anyone went for a run, then ate a pizza right after?",
    "Would you mind being the opposite sex for a day?",
    "Anyone ever had a crush on a teacher?",
    "Anyone ever had a crush on a anyone in this chat?",
    "Is anyone's crush also in this chat?",
    "Has anyone ever stolen something?",
    "Say your favorite feature about the opposite sex?",
    "Say your favorite feature about {}?"
]

FRIENDSHIP_TEST = ["When did I have my first kiss?"]
UNSCRAMBLE = []

CATEGORIES = ['cars']
RHYME_TIME = []
EMOJI_STORY = []

hey_options = ["Hey", "Random", WAVE_HAND, "Surprise me"]

UNKNOWN = ["Aww, you are so cute. Use your words next time."]

START_CHATTING = [["I'm a bot that helps start conversations.",
                   "Don't know what to say? Just type @hey!"]]

# Organize Constants
unknown_reply = UNKNOWN
subscribe_reply = START_CHATTING
hey_reply = {"group": SMALL_TALK_GROUP + QUESTIONS_GROUP, '1v1': SMALL_TALK_1v1 + QUESTIONS_1v1}
news_reply = NEWS
small_talk_reply = {"group": SMALL_TALK_GROUP, '1v1': SMALL_TALK_1v1}
flirt_reply = {"group": FLIRT_GROUP, '1v1': FLIRT_1v1}
questions_reply = {"group": QUESTIONS_GROUP, '1v1': QUESTIONS_1v1}
would_you_rather_reply = {'group': WOULD_YOU_RATHER, '1v1': WOULD_YOU_RATHER}
truth_or_dare_reply = {'group': TRUTH_OR_DARE_GROUP, '1v1': TRUTH_OR_DARE_1v1}
facts_reply = FACTS
help_reply = {"group": HELP_GROUP, '1v1': HELP_1v1}

basic_keyboard = [TextResponse("Small Talk"),
                  TextResponse('Flirt'),
                  TextResponse("Questions"),
                  TextResponse("News"),
                  TextResponse("Truth or Dare"),
                  TextResponse("Would you rather?"),
                  TextResponse("Facts")]
