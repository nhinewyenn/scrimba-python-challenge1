names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = "Hi, this is your party invitation "

"""print out invitation for each friends using for loops
- 2 names variable above
- add 2 extra names to the list using input box
- printout 1 invitation to each friends per line
- Name should be properly capitalised
* Might need 2 for loops for this exercise
"""

names.extend(names1)

for i in range(2):
    names.append(input("Please enter a name here: "))

for name in names:
    proper_name = name.lower().title()
    print(msg + proper_name)
