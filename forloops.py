# Looping through each letter
for letter in "Blackpink":
    print(letter)


# Looping through range of number
for i in range(1, 10):
    print(i)

# Looping through an array
groups = ["Twice", "Blackpink", "Red Velvet", "Aespa"]
for group in groups:
    if group == "Red Velvet":
        print(f"Found {group}")
        break # This will stop after finding red velvet, aespa will not be called
      
# Nested for loops
for g in groups:
    for number in [1,2]:
        print(g, number)