# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens 
#    - total cost
#    - games available

customer_name = "john"
number_of_passes = 10
token_per_pass = 10
price_per_pass = 20.5
token_required = 5

total_token = number_of_passes * token_per_pass      # total tokens earned
total_cost = number_of_passes * price_per_pass        # total money spent
games_available = total_token // token_required       # how many full games can be played

print("Arcade day pass")
print("Customer name", customer_name)
print("Passes bought", number_of_passes)
print("Total tokens", total_token)
print("Total costs", total_cost)
print("Games available", games_available)


# User input
name = input("What is your name")
print(name)