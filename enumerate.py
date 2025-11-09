"""Enumerate
enumerate() function adds a counter to each item in a list or any other iterable,
- returns a list of tuples containing the index position and the element for each element of the iterable.
- turn iterable into something we can loop through using indexes (each item comes with its number - starting from 0)
"""

friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

for numb, frd in enumerate(friends):
    print(numb, frd)

for numb, frd in enumerate(friends, 1): #start at 1 instead of 0
    print(frd) 