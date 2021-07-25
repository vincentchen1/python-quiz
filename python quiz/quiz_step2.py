import random
import csv

def read_data_from_file(file_name):
    with open(file_name) as csv_file:
        # csv_file is the file handler
        # lines are all the lines from file
        lines = csv.reader(csv_file)
        for data_list in lines:
            question = data_list[0]
            question = question.strip()
            answer = data_list[1]
            answer = answer.strip()
            words[question] = answer

def random_key():
    # find all the keys
    keys = words.keys()
    keys = list(keys)
    random_key = random.choice(keys)
    return random_key

words = { }
word_file = "spanish/quiz1.csv"
read_data_from_file(word_file)

random_answer = random_key()
random_question = words[random_answer]

user_answer = input("Word for " + random_question + ": ")
user_answer = user_answer.strip()
if (user_answer == random_answer):
    print("correct")
else:
    print ("incorrect")