print("=" * 43)
print("     Password Retry System - Version 1       ")
print("=" * 43)
print()

# Edge Cases
# 1. User can input space at the begining or the end of the password
# 2. User can input nothing

correct_password = "Python123"

user_attempt = 1
access_granted = False
while user_attempt <= 3:

    user_password = input("Enter password: ").strip()

    if user_password == "":
        # Blank passwords are treated as invalid input.
        # They do NOT consume one of the three login attempts.
        print("\nInvalid Password - Please do not enter blank password.")
        print(f"Attempts Remaining: {4-user_attempt}\n") 
        continue
    elif user_password == correct_password:
        access_granted = True
        break
    else:
        print("\nIncorrect Password") 
               

    print(f"Attempts Remaining: {3-user_attempt}\n") 
    user_attempt = user_attempt + 1

if access_granted:
    print("Access Granted!\n")
else:
    print("Account Locked!\n")  

print("Thank You for using Password Retry System - Version 1\n")