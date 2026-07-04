print("=" * 40)
print("         Improved Login System       ")
print("=" * 40)
print()

# Edge cases:
# 1. The user name can be enetred with numbers/special characters
# 2. User presses Enter without typing anything.
# 3. Username contains spaces.
# 4. Password is blank.
# 5. Username is incorrect.
# 6. Password is incorrect.
# 7. Both username and password are incorrect.
# 8. Username is case-sensitive.
# 9. Password is case-sensitive.

correct_username = "Lucky"
correct_password = "python123"

entered_username = input("Enter user name: ").strip()
if entered_username == "":
    print("Invalid Username - Please enter proper Username\n")
elif entered_username.find(" ") != -1:
    print("Username cannot have blank space between the name - try again\n")    
else:    
    entered_password = input("Enter password: ")
    print()
 
    if entered_password == "":
        print("Password cannot be blank - Please enter proper Password\n")
    else:

        # CODE TO PREDICT INVALID USERNAME OR PASSWORD
        # if entered_username == correct_username and enetred_password == correct_password:
        #     print("Login Successful!\n")
        # else:
        #     print("Invalid Username or Password.\n") 



        # CODE FOR DETAILED REPORT ON IF EITHER USERNAME OR PASSWORD IS WRONG
        if entered_username == correct_username and entered_password == correct_password:
            print("Login Successful!\n")
        else:
            if entered_username != correct_username and entered_password != correct_password:
                print("Both Username and Password are incorrect.\n") 
            elif entered_username != correct_username:
                print("Username is incorrect.\n")
            elif entered_password != correct_password:
                print("Password is incorrect.\n")    
               


print("Thank you for using Improved Login System.\n")    