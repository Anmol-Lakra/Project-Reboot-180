print("=" * 40)
print("         Countdown Timer Vesion 1        ")
print("=" * 40)
print()

# Edge Cases:
# 1. User can input  0
# 2. User can input a blank
# 3. User can input a "-"
# 4. User can input a negative number
# 5. User can input alphabets
# 6. User can input special characters
# 7. User can input decimal numbers intead of whole numbers
# 8. Users can input numbers with spaces between them


starting_number = input("Enter a starting number: ").strip()

if starting_number == "":
    print("\nInvalid number - Please enter valid number\n")

elif starting_number == "-":
    print("\nInvalid number - Please enter valid number\n")

elif starting_number[0] == "-":
    print("\nNo negative numbers allowed - Please enter positive whole numbers\n")

elif starting_number.find(" ") != -1:
    print("\nNo spaces between numbers allowed - Please enter valid number\n")         

elif starting_number.find(".") != -1:
    print("\nDecimal numbers not allowed - Please enter whole numbers\n")

else:

    print()
    starting_number = int(starting_number)

    if starting_number == 0:
        print("Zero cannot be the starting number - Please enter a non-zero starting number\n")

    else:

        while starting_number >= 1:
            print(starting_number)
            starting_number = starting_number - 1
        print("\nTime's UP!\n")


print("Thank you for using Countdown Timer Version 1.\n")
