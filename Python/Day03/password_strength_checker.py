print("=" * 42)
print("         Password Strength Checker       ")
print("=" * 42)
print()

# Edge cases:
# 1. we cannot check if how many alphabets, numbers and integers are being entered to
#    consider determine if it is strong password taking all the mix of everything

user_password = input("Please enter your password: ").strip()
print()

if user_password == "":
    print("Do not use a blank password - it is very unsafe.\n")
elif user_password.find(" ") != -1:
    print("Don't keep space in password - it is not a healthy practice.\n")
else:
    length_of_password = len(user_password)
    if length_of_password < 6:
        print(f"Password Length         -       {length_of_password}")
        print(f"Password Strength       -       Weak Password\n")
    elif length_of_password < 10:
        print(f"Password Length         -       {length_of_password}")
        print(f"Password Strength       -       Medium Password\n")
    elif length_of_password >= 10:
        print(f"Password Length         -       {length_of_password}")
        print(f"Password Strength       -       Strong Password\n")

print("Thank you for using Password Strength Checker!\n")          
