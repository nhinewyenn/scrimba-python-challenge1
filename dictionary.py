movie = {
  'title' : 'Life of Brian',
  'year' : 1979,
  'cast' : ['John','Eric','Michael','George','Terry'] 
}
movie["title"] = "Dune" #update movie title 
movie["budget"] = 350000 # add another key called budget into the dictionary
# Update all value from dictionary
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
print(movie["title"]) #this will get the value of title key
print(movie)

# Loop through dictionary
for key, value in movie.items():
    print("key", key)
    print("value", value)


python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# membership test
print("Arthur" in holy_grail)

if "Arthur" not in python:
    print("He is not here")

people = {}
people1 = {}
people2 = {}

# Update dictionary method 1
people.update(python) # python dictionary will be in people
people.update(holy_grail) #holy grail will be in people
print(people.items)

# method 2
for groups in (python, life_of_brian):
    people1.update(groups) #python and life of brian will be in people1
print(people1.items) # .items will turn the dictionary into a tuple

# method3
people2 = {**python, **holy_grail, **life_of_brian}
print(people2)

print("Total sum of the ages:", sum(people2.values()))