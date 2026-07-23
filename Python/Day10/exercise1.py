# Edge cases:
# 1. User can enter multiple dots and the program will not be able to handle as 
#    we are not using try/except
# 2. Floating-point calculations may display values like
#    31.359999999999996 because of how computers store decimal numbers.
# 3. We will learn formatting and rounding later.

def print_title():
    print("=" * 40)
    print("     Exercise 1 - Square of numbers")
    print("=" * 40)
    print()

def get_number():
    while True:
        user_input = input("Enter a number: ").strip()
        if user_input == "":
            print("Invalid input - please enter a number.\n")
            continue
        elif "." in user_input:
            user_input = float(user_input)
        elif not user_input.isdigit():
            print("Invalid input - please enter a number.\n")
            continue
        else:
            user_input = int(user_input)

        break 

    return user_input  

def calculate_square(number):
    square = number * number

    return square

def print_result(number, result):
    print(f"The square of {number}  :   {result}\n")



def main():
    print_title()
    user_input = get_number()
    square_of_number = calculate_square(user_input)
    print_result(user_input, square_of_number)

    print("Thank You for using Square of numbers.\n")


main()