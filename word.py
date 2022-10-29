import random

class words:
    """responsibility:
    to horld a list of 10 words and chose a word randomly.
 behaviors:
    -choose random word
 state:
    list of 10 words
--------------------------------
    (attributes)
    word_list: 10 words 

    (methods)
    get_random_word() 
    _init_(self) """


    def __init__(self):

        self.words_list = ("mother", "prayer","paper", "clean", "father",
        "play", "magic", "family", "game", "experience" )

    def get_random_word(self):

        random_word = random.choice(self.words_list)
        return random_word
    