# Tuples
# A list you can't change - indexing and function similar to list
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2])
print(friends_tuple[2])


# Sets - very fast unordered list, remove any duplicates inside
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends)
print(friends_tuple)
print(friends_set) # will remove duplicates value - Eric
print(friends_set.intersection(my_friends_set)) # find similar value in both set =. Eric, Graham
print(friends_set.difference(my_friends_set)) # Value in friend set that dont exist in my friend set (John, michael, terry)
print(friends_set.union(my_friends_set)) # combine both set together

# Set empty lists, tuples or sets
#empty Lists
empty_list = []
empty_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = set()