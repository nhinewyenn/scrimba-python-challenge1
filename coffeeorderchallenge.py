# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price 

total = 0
drink_count = 0

while True:
    customer_name = input("What's your name?: ")
    if customer_name == "done":
        break
        
    drinks = input("Please choose between latte, americano or espresso: ")
    if drinks == "latte":
        drink_count +=1
        total += 3.50
        print(f"{customer_name}, your latte is ready")
    elif drinks == "espresso":
        drink_count +=1
        total += 2.50
        print(f"{customer_name}, your espresso is ready")
    elif drinks == "americano":
        drink_count +=1
        total += 3.00
        print(f"{customer_name}, your americano is ready")
    else:
        print("Please choose one of the 3 option stated")
        continue

print(f"Total drink made: {drink_count}")
print("Total price: " + str(total))