# 📱 Phone Number Formatter
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

phone_input = input("Please enter your number: ").strip()
phone_format = phone_input.replace(".", " ").replace("-", " ").replace(",", " ").split()
merge = "".join(phone_format)

if len(merge) == 10 and merge.isdigit():
    first_three = merge[0:3]
    mid_three = merge[3:6]
    last_digits = merge[6:10]
    print(f"({first_three}) {mid_three}-{last_digits}")
else:
    print("Please enter exactly 10 digits.")