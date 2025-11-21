# Math tutor project
#import modules
# ask how many questions user wants
#set score start at zero
#loop through number of questions
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score 
from  random import randrange as r
import time
questions_play = int(input("how many questions do you want to play (number only)?"))
highest_number = int(input("What's the highest number you want to practice to?"))
question_answered = 0
score = 0

while True:
    num1 = r(1,highest_number)
    num2 = r(1,highest_number)
    answer = num1 * num2
    questions = int(input(f"{num1} * {num2} = ?"))

    if question_answered == questions_play:
        print(f"Thank you for playing, your score is: {score}/{question_answered}! You completed the game in {time.time()}")
        break

    if questions == answer:
        score += 1
        question_answered += 1
        print("Correct!! the answer is", answer)
    else:
        print("Incorrect answer, please try again :(")
