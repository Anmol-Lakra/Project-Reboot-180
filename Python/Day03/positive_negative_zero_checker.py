print("=" * 40)
print("     Positive/Negative/Zero Checker      ")
print("=" * 40)
print()

# Edge cases:
# alphabets/special characters cannot be checked and warned

mistake_flag = 0

user_number = input("Enter a number: ").strip()
print()

if user_number == "":
    print("No number given - Please give a number\n")
    mistake_flag = 1
else:
    blank_locator = user_number.find(" ")
    if blank_locator != -1:
        print("No blank spaces between numbers allowed - try again.\n")    
        mistake_flag = 1
    else:
        if  user_number.find(".") != -1:
            user_number = float(user_number)
        else:
            user_number = int(user_number)


if mistake_flag == 0:
    if user_number > 0:
        print(f"The number {user_number} is Positive\n")
    elif user_number < 0:
        user_number = str(user_number)
        print(f"The number {user_number} is Negative\n")    
    else:
        print("The number is Zero\n")


print("Thank You for using Positive/Negative/Zero Checker!\n")

