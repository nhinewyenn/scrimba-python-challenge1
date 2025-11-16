# Lambdas functions
def f(x): return x + 5
f = lambda x: x +5
print(f(2))


def strip_spaces(str):
    return ''.join(str.split(' '))
#write equivalent lambda and insert Lambda here
strip_spaces1 = lambda str: "".join(str.split(" "))   
print(strip_spaces1('Monty Pythons Flying Circus')) 


def join_list_no_duplicates(list_a,list_b):
    return list(set(list_a + list_b))

list_1 = [1,2,3,4]
list_2 = [3,4,5,6,7]
#write lambda below
join_list_no_duplicates1 = lambda list_a, list_b: list(set(list_a + list_b))
print(join_list_no_duplicates(list_1,list_2))



