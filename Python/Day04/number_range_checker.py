print("=" * 40)
print("         Number Range Checker        ")
print("=" * 40)
print()

# Edge Cases:
# 1. User can just press enter
# 2. User can enter blank space 
# 3. User can enter alphabets/special characters
# 4. User can enter gap between numbers
# 5. User can enter decimal numbers
# 6. User can input negative numbers
# 7. User can enter exact 0
# 8. User can input exact 1
# 9. User can input exact 100
# 10. User can input exact 101
# 11. User can have blank space between the start and the end 

user_number = input("Enter a number: ").strip()

if user_number == "":
    print("Invalid number - Please enter valid number.\n")
elif user_number.find(" ") != -1:
    print("Number cannot have gaps in between - Please enter valid number.\n")
else:
    print()

    if user_number.find(".") != -1:
        user_number = float(user_number)
    else:
        user_number = int(user_number)

    if user_number > 100:
        print(f"The number {user_number} exceeds the maximum limit.\n")
    elif user_number <= 0:
        print(f"The number {user_number} is below the minimum limit.\n")
    else:
        print(f"The number {user_number} is within the valid range.\n")

print("Thank You for using Number Range Checker.\n")
        



