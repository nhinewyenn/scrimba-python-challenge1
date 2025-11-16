nums = [1,2,3,4] 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']
# nums, names and letters are the same index and length
# zip is going to match them together
combo = list(zip(nums, letters, names, strict=False))
print(combo) #turn into a list of tuples

# unzip
num, let, name = zip(*combo, strict=False)
print(num, let, name)