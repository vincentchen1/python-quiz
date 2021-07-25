import random
import csv

def random_key(words):
    # find all the keys
    keys = words.keys()
    keys = list(keys)
    random_key = random.choice(keys)
    return random_key

def read_data_from_file(words, file_name):
    with open(file_name) as csv_file:
        # csv_file is the file handler
        # lines are all the lines from file
        lines = csv.reader(csv_file)
        for data_list in lines:
            question = data_list[0]
            answer = data_list[1]
            words[question] = answer