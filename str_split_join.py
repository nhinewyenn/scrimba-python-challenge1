# String - split and join lesson
msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split()) # separate the msg string into a list
print(csv.split(",")) # split into the comma
print(msg.replace(" ", "")) #replace spaces with no spaces


#* EXERCISE
csv2 = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list2 = ['Exercise: fill me with names']
print(friends_list2)

# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
# 1st - manipulate csv2 list so that there's no weird syntax
clean_csv = csv2.replace(",", " ").replace(";", " ").replace(":", " ")

# 2 - clear friend list and extend csv2 
friends_list2.clear()
friends_list2.extend(clean_csv.split())
print(friends_list2)
