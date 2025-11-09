# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("What is your name?")
distance = input("How many km have you traveled in km?")
print(f"Hi {name.capitalize()}")
print(f"You have traveled {distance}km")
convert_km = float(distance) / 1.609
print(f"You have traveled {convert_km} miles")
