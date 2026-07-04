print("=" * 42)
print("   Password Strength Checker Version 3    ")
print("=" * 42)
print()

# Edge cases:
# 1. User can press enter and enter nothing
# 2. User can give space on the front and end of the password
# 3. User can give space between the password (which can be allowed as it's password)
# 4. User can enter correct password but in wrong case
# 6. What can be the maximum number of digits a strong password can have                                              

user_password = input("Enter a password: ").strip()
if user_password == "":
    print("Password cannot be blank - Please enter valid password.\n")
else:
    print()

    length_of_password = len(user_password)
    print(f"Length of password      :       {length_of_password}")

    if length_of_password > 15:
        print(f"Status                  :       Invalid password length.")
        print("Note: Password length should be more than 0 or equal to or less than 15.\n")
    elif length_of_password < 4:
        print("Status                  :       Weak Password!")
        print("Warning! Your account is at risk.\n")
    elif length_of_password < 6:    
        print("Status                  :       Medium Password!")
        print("Okay! Your account is at Medium Risk.\n")
    else:
        print("Status                  :       Strong Password!")
        print("Congratulations! Your account is secure.\n")    

print("Thank You for using Password Strength Checker Version 3.\n")