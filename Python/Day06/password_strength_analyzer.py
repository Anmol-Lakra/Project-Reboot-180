print("=" * 35)
print("     Password Strength Analyzer")
print("=" * 35)
print()

# Edge cases:
# 1. User can enter a blank
# 2. User can enter blank space in between password

input_validator = True
while input_validator:
    user_password = input("Enter a password: ").strip()
    if user_password == "":
        print("Invalid password - password cannot be blank.\n")
    elif user_password.find(" ") != -1:
        print("Invalid password - do not use space in password.\n")
    else:
        input_validator = False
        print()

length_counter = 0
upper_case_counter = 0
lower_case_counter = 0
digit_counter = 0
special_character_counter = 0

for char in user_password:
    length_counter += 1
    if char.isupper():
        upper_case_counter += 1
    elif char.islower():
        lower_case_counter += 1
    elif char.isdigit():
        digit_counter += 1
    else:
        special_character_counter += 1

# Password Analysis
print("Password Analysis:\n")    
print(f"Length              :           {length_counter}")
print(f"Uppercase Letters   :           {upper_case_counter}")
print(f"Lowercase Letters   :           {lower_case_counter}")
print(f"Digits              :           {digit_counter}")
print(f"Special Characters  :           {special_character_counter}\n")

if length_counter >= 8 and upper_case_counter >= 1 and lower_case_counter >= 1 and digit_counter >= 1 and special_character_counter >= 1:
    print("Password Strength   :            Strong\n")
else:
    print("Password strength   :            Weak\n")

    # Bonus Challenge:
    print("Reasons:")
    if length_counter < 8:
        print("* Password is too short")
    if upper_case_counter == 0:
        print("* Missing uppercase letters")
    if lower_case_counter == 0:
        print("* Missing lowercase letters")
    if digit_counter == 0:
        print("* Missing digits")
    if special_character_counter == 0:
        print("* Missing special characters")
    
    print()

print("Thank you for using Password Strength Analyzer\n")
    



        
    