# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.
import random
how_many = int(input("How many people are entering the raffle? (at least 3)"))
prize = 3
name_list = []
prize_list = []

if how_many >= 3:
  for _ in range(how_many):
    name = input("What is your name? (At least 3)").capitalize()
    name_list.append(name)
else:
  print("Error, must be at least 3 names")
print(name_list)  

for _ in range(prize):
  prize_name = input("Prize name: ").capitalize()
  prize_list.append(prize_name)
print(prize_list)

random_winner = random.sample(name_list, prize)
winner_dict = {}

for i, prize in enumerate(prize_list):
  winner_dict.update({random_winner[i]: prize})
print(winner_dict)