import random
import quiz_common

words = { }

# ask the user for quiz type
print("Quiz Types: sat, spanish")
quiz_type = input("Enter quiz type: ")
data_files_path = quiz_type + "/"

# randomly select a file
random_file_num = random.randrange(1,3)
random_file_num = str(random_file_num)
word_file = data_files_path + "quiz" + random_file_num + ".csv"
quiz_common.read_data_from_file(words, word_file)

random_answer = quiz_common.random_key(words)
random_question = words[random_answer]

user_answer = input("Word for " + random_question + ": ")
if (user_answer == random_answer):
    print("correct")
else:
    print ("incorrect")