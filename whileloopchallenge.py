import random

print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while  loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
i = 0
random_number = random.randint(1, 100)
max_guesses = 5

while i < max_guesses:
    guess_number = int(input("Guess a number between 1-100: "))
    i+=1 # iterate
    if guess_number == random_number:
        print("You win!!")
    elif guess_number < random_number:
        print("Too low, try again")
    else:
        print("Too high, try again")

if i == max_guesses and guess_number != random_number:
    print(f"You lose, the number was {random_number}")
