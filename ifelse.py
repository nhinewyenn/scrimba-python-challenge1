# Conditional - if/else statement

is_raining = True
is_cold = True

print("good morning")

if is_raining and not is_cold:
    print("Bring an umbrella")
elif is_raining and is_cold:
    print("Bring an umbrella and a jacket")
elif is_cold and not is_raining:
    print("Bring a jacket")
else:
    print("optional")

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

is_temp = False
operator = input("Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ")

if operator in ["f"]:
    celsius = float(input("Input your temperature number: "))
    fahrenheit = celsius * 9/5 +32
    print(f"It is {celsius} degree or {fahrenheit} fahrenheit")
else:
    first_number = float(input("Your first number: "))
    second_number = float(input("Your second number: "))
    if operator in ["-"]:
        print(first_number - second_number)
    elif operator in ["+"]:
        print(first_number + second_number)
    elif operator in ["*"]:
        print(first_number * second_number)
    elif operator in ["/"]:
        print(first_number / second_number)
    else:
        print("Invalid input")
