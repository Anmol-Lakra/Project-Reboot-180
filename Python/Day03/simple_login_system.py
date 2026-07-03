print("*" * 40)
print("         Simple Login System         ")
print("*" * 40)
print()

# Edge cases:
# 1. Numbers/special characters can be used in username

is_login_checker = False
is_username_correct = False
is_password_correct = False
username_password_false = True

print("Create your Username and Password:")
correct_username = input("Create username: ").strip()
if correct_username == "":
    print("Username cannot be blank - Please enter valid Username.\n")
    username_password_false = False
else:    
    correct_password = input("Create password: ")
    print()

    print("Sign in using your Username and Password: ")
    username = input("Enter your username: ")
    if username == "":
        print("No input - Please enter your Username.\n")
        username_password_false = False
    else:    
        password = input("Enter your password: ")
        print()


        if username == correct_username:
            is_username_correct = True
            is_login_checker = True
            username_password_false = False
        if password == correct_password:
            is_password_correct = True
            is_login_checker = True
            username_password_false = False

if is_login_checker:
    if is_username_correct:
        if is_password_correct:
            print("Login Successful")
            print(f"Welcome {correct_username}\n")
        else:
            print("Wrong Password\n")
    else:
        print("Wrong Username\n")


if username_password_false:
        print("Wrong Username")
        print("Wrong Password\n")

  

print("Thank You for using Simple Login System\n")
