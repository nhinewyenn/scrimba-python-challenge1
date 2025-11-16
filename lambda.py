def square(x):
    return x*x
  
# How to write this in lambda function
square1 = lambda x: x*x

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
monty_python.sort(key = lambda name: name.split(" ")[-1]) #last name order


# Lambdas function inside a function
def func(n):
    return lambda a: a*n

doubler = func(2)
print(doubler(3)) #6