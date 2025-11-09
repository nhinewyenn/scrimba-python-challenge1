#Sets - Exercise
#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
new_friends_set = set()

# 1 and 2
if "Eric" in friends and "John" in friends:
    new_friends_set = friends.union(my_friends)
print(new_friends_set)

# 3 and 4
print(friends.intersection(my_friends)) # name in both sets
print(friends.difference(my_friends)) # name only in friends
print(friends.symmetric_difference(my_friends)) #show name only in one of the list

# new car list
new_cars = list(set(cars))
print(new_cars)