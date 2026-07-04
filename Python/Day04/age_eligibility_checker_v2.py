print("=" * 40)
print("     Age Eligibility Checker Ver.2        ")
print("=" * 40)
print()

# Edge cases:
# 1. User can enter alphabets/special characters instead of age
# 2. Use can enter blank
# 3. User can give space between the age digit
# 4. User can enter decimal digits instead of whole numbers
# 5. User can give negative age
# 6. User can give age which is too big (say 150 which is not possible)
# 7. User enters exactly 18.
# 8. User enters age above 150.
# 9. User enters age 0.

user_name = input("Enter your name: ").strip().title()
if user_name == "":
    print("Invalid Name - Please give a valid name.\n")
else:
    user_age = input("Enter your age: ").strip()
    print() 

    if user_age == "":
        print("Invalid age - Please enter your valid age.\n")
    elif user_age.find(" ") != -1:
        print("Age cannot have space between them - Please enter your valid age.\n")
    elif user_age.find(".") != -1:
        print("Decimal age is not accepted - Please enter age in whole numbers.\n")
    else:

        user_age = int(user_age)
        print(f"Hello {user_name}")
        if user_age >= 150 or user_age < 0:
            print("Your age is Invalid\n")
        elif user_age < 18:
            print("Sorry! you are not eligible to vote yet.")
            print(f"You will be able to vote after {18-user_age} year/s!\n")
        else:
            print("Congratulations! You are eligible to vote.\n")  

print("Thank You for using Age Eligibility Checker Ver.2\n")                  