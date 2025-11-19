# COMPREHENSION
# Basically, for loops with less code
numbers = [1,2,3,4,5,6,7,8,9]
new_list = []

for num in numbers:
    new_list.append(num * num)
print(new_list)

# give me a list with num for each num in numbers if num is even
new_list1 = [num for num in numbers if num % 2 == 0]
print(new_list1)

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
letter_num_list = []
for letter in "spam":
    for num in range(4):
        letter_num_list.append((letter,num))
print(letter_num_list)
letter_num_list1 =[(letter, num) for letter in "spam" for num in range(4)]

# Dictionary comprehensions
movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']
print(list(zip(movies, year, strict=False)))
# give me a dict('movies': year) for each movies, year in zip(movies, year)

movie_dict = {}
for movie, yr in zip(movies, year, strict=False):
    movie_dict.update({movie: yr})
print("MOVIE DICTIONARY", movie_dict)

# for movie from 1980 and up
movie_dict_compr = {(movie, yr) for movie, yr in zip(movies, year, strict=False) if yr > 1980}
print("MOVIE DICTIONARY COMPREHENSION", movie_dict_compr)