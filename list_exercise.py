# Example lists
friends = ["lisa", "jisoo", "jennie", "rose", "giselle", "karina", "ninging", "winter"]
cars = [911,130,328,535,740,308]

print(friends)
friends.sort() # sort in ascending order
friends.sort(reverse=True) # sort in descending order
friends.reverse() # Reverse a string
print(friends)


# find minimum, maximum and sum of list
print(min(cars))
print(max(cars))
print(sum(cars))

# Add new friends
friends.append("Yeji") # Add at the end
friends.insert(4, "Nayeon") #insert at position 4, after Rose
print(friends)

# Combine friends and cars list
friends.extend(cars)
print(friends)

# Remove
friends.remove("Yeji") #remove completely
friends.pop() #Remove the last index, add it to memory
print(friends)

# Clear lists - empty list
# friends.clear()

# Delete completely
# del friends

# copy lists
copy_friends = friends[:]
copy_friends1 = friends.copy()
copy_friends2 = list(friends)