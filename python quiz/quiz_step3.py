import random
import csv

def random_key():
    # find all the keys
    keys = words.keys()
    keys = list(keys)
    random_key = random.choice(keys)
    return random_key

def read_data_from_file(file_name):
    with open(file_name) as csv_file:
        # csv_file is the file handler
        # lines are all the lines from file
        lines = csv.reader(csv_file)
        for data_list in lines:
            question = data_list[0]
            answer = data_list[1]
            words[question] = answer

words = { }


data_files_path = "spanish/"

# ask the user for quiz name
# open the file with name <data_files_path><quiz_name>.csv
# example: spanish/quiz1.csv
quiz_name = input("Pick a Quiz [quiz1, quiz2, quiz3] ")
word_file = data_files_path + quiz_name + ".csv"
read_data_from_file(word_file)

random_answer = random_key()
random_question = words[random_answer]

user_answer = input("Word for " + random_question + ": ")
if (user_answer == random_answer):
    print("correct")
else:
    print ("incorrect")