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

# ask the user for quiz type
print("Quiz Types: sat, spanish")
quiz_type = input("Enter quiz type: ")
data_files_path = quiz_type + "/"

# randomly select a file
random_file_num = random.randrange(1,3)
random_file_num = str(random_file_num)
word_file = data_files_path + "quiz" + random_file_num + ".csv"
read_data_from_file(word_file)

random_answer = random_key()
random_question = words[random_answer]

user_answer = input("Word for " + random_question + ": ")
if (user_answer == random_answer):
    print("correct")
else:
    print ("incorrect")