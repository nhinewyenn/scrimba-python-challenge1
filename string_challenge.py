msg='welcome to Python 101: Strings'

# Extract msg string to create new string
get_1 = msg[18] #1
welcome = msg[:7] # welcome
to = msg[8:10] # to
extracted_msg = f"{get_1} {welcome} ring {to} tyler".title()
print(extracted_msg)


# Reverse a string
reverse_extracted_msg = extracted_msg[::-1]
print(reverse_extracted_msg)


# Multiline string
multiline = """This is a multiline string
this is the next row of the multiline string
another row of the multiline string"""
print(multiline)


# Find and replace string
print(msg.find("Python")) # index 11
print(msg.replace("Python", "JavaScript")) #welcome to JavaScript 101: Strings

# Check if python exist
print("Python" in msg) # True as we have not globally change Python into Javascript yet, it is only a print statement
print("Python" not in msg) #False