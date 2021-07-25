import random

def random_key():
    # find all the keys, 'keys' now in a SET data structure
    keys = words.keys()
    # convert 'keys' to LIST
    keys = list(keys)
    # randomly select a key from 'keys'
    random_key = random.choice(keys)
    return random_key

words = {
    "red" : "rojo",
    "blue" : "azul",
    "water" : "aqua",
    "sky" : "cielo",  
    "love" : "amor",  
}

random_answer = random_key()
random_question = words[random_answer]

user_answer = input("Word for " + random_question + ": ")
user_answer = user_answer.strip()
if (user_answer == random_answer):
    print("correct")
else:
    print ("incorrect")