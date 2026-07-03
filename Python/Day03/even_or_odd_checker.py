print("=" * 40)
print("         Even or Odd Checker         ")
print("=" * 40)
print()

# Edge cases
# 1. we cannot stop the user from entering or warn them if they enter alphabets or special characters

user_num = input("Enter a number: ").strip()
print()

if user_num == "":
    print("No input - Please retry again with valid whole number.\n")
else:
    blank_finder = user_num.find(" ")
    if blank_finder != -1:
        print("Blank space between numbers - Please retry again with valid whole number.\n")
    else:
        dot_finder = user_num.find(".")
        if dot_finder != -1:
            print("Decimal number input - Please retry again with valid whole number.\n")
        else:
            integer_user_num = int(user_num)
            if integer_user_num % 2 == 0:
                print(f"The number {integer_user_num} is Even.\n")
            else:
                print(f"The number {integer_user_num} is Odd.\n")

print("Thank You for using Even or Odd Checker!\n")         